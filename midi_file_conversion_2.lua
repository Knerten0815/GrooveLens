-- Reaper Lua script for processing MIDI files

-- Directory containing the MIDI files
local midi_dir = "/Users/vinni/Desktop/Code/Audio Data Science/StyleExtraction/Datasets/groove/drummer1/eval_session"
-- Directory to save the audio files
local output_dir = "/Users/vinni/Desktop/Code/Audio Data Science/StyleExtraction/Datasets/converted"
-- Maximum number of test runs
local max_test_runs = 5

-- Function to get tempo and time signature from filename
function get_tempo_and_time_signature_from_filename(filename)
    local parts = {}
    for part in string.gmatch(filename, "[^_]+") do
        table.insert(parts, part)
    end
    local tempo = tonumber(parts[3])
    local time_signature_match = string.match(filename, "(%d+-%d+)%.mid$")
    local time_signature = time_signature_match and string.gsub(time_signature_match, "-", "/") or "4/4"
    return tempo, time_signature
end

-- Function to set project tempo
function set_project_tempo(tempo)
    if tempo then
        reaper.CSurf_OnTempoChange(tempo)
    else
        debug_msg("Invalid tempo value")
    end
end

-- Function to set project time signature
function set_time_signature(time_signature)
    if time_signature then
        local measures, beats = time_signature:match("(%d+)/(%d+)")
        if measures and beats then
            reaper.SetTempoTimeSigMarker(0, -1, -1, -1, -1, 0, tonumber(measures), tonumber(beats), true)
        else
            debug_msg("Invalid time signature format")
        end
    else
        debug_msg("Invalid time signature value")
    end
end

-- Function to load MIDI file into Reaper
function load_midi_file(midi_path)
    reaper.InsertMedia(midi_path, 0)
end

-- Function to start recording
function start_recording()
    reaper.Main_OnCommand(40044, 0)  -- Transport: Go to start of project
    reaper.Main_OnCommand(1013, 0)   -- Transport: Record
end

-- Function to stop recording
function stop_recording()
    reaper.Main_OnCommand(1016, 0)  -- Transport: Stop
end

-- Function to wait for a specified duration in seconds
function wait(duration)
    local start_time = reaper.time_precise()
    while reaper.time_precise() - start_time < duration do
        reaper.defer(function() end)
    end
end

-- Function to get the length of a MIDI file in seconds
function get_midi_length_in_seconds(midi_path)
    local source = reaper.PCM_Source_CreateFromFile(midi_path)
    if source then
        local length = reaper.GetMediaSourceLength(source)
        reaper.PCM_Source_Destroy(source)
        return length
    else
        return 0
    end
end

-- Function to save the project with the recorded audio
function save_project_as(audio_filename)
    reaper.GetSetProjectInfo_String(0, "RENDER_FILE", audio_filename, true)
    reaper.Main_OnCommand(41824, 0)  -- File: Render project, using the most recent render settings
end

-- Function to record and save audio
function record_and_save_audio(filename, output_dir, duration)
    reaper.Main_OnCommand(1013, 0)  -- Start recording
    local start_time = reaper.time_precise()
    local function wait_until_end()
        if reaper.time_precise() - start_time < duration then
            reaper.defer(wait_until_end)
        else
            reaper.Main_OnCommand(1016, 0)  -- Stop recording
            local audio_filename = output_dir .. "/" .. filename:gsub("%.mid$", "_converted.wav")
            save_project_as(audio_filename)
            debug_msg("Finished recording and saved audio as: " .. audio_filename)
        end
    end
    wait_until_end()
end

-- Function to clear the imported MIDI data from the track
function clear_imported_midi_data()
    local track = reaper.GetTrack(0, 0)
    local item_count = reaper.CountTrackMediaItems(track)
    for i = item_count - 1, 0, -1 do
        local item = reaper.GetTrackMediaItem(track, i)
        reaper.DeleteTrackMediaItem(track, item)
    end
end

-- Function to recursively find MIDI files
function find_midi_files(dir, file_list)
    local p = io.popen('find "' .. dir .. '" -type f -name "*.mid"')
    for file in p:lines() do
        table.insert(file_list, file)
    end
end

-- Ensure necessary directories exist
function ensure_directory_exists(dir)
    local p = io.popen('[ -d "' .. dir .. '" ] && echo "exists"')
    local result = p:read("*a")
    p:close()
    if result:find("exists") then
        return true
    else
        os.execute('mkdir -p "' .. dir .. '"')
        return true
    end
end

-- Ensure necessary directories exist
ensure_directory_exists(midi_dir)
ensure_directory_exists(output_dir)

-- Counter for the number of test runs
local test_run_counter = 0

-- Debug function to show message boxes for debugging
function debug_msg(msg)
    reaper.ShowMessageBox(msg, "Debug Message", 0)
end

-- Show a message box to indicate the start of the script
debug_msg("Starting script...")

-- List to hold all MIDI files
local midi_files = {}

-- Find all MIDI files recursively
find_midi_files(midi_dir, midi_files)

-- Process each MIDI file
for _, midi_path in ipairs(midi_files) do
    local midi_file = midi_path:match("([^/]+)$")
    debug_msg("Checking file: " .. midi_file)

    if test_run_counter >= max_test_runs then
        debug_msg("Maximum test runs reached. Stopping script.")
        break
    end

    -- Extract tempo and time signature
    local tempo, time_signature = get_tempo_and_time_signature_from_filename(midi_file)
    if not tempo then
        debug_msg("Skipping file due to invalid tempo: " .. midi_file)
        goto continue
    end
    if not time_signature then
        debug_msg("Skipping file due to invalid time signature: " .. midi_file)
        goto continue
    end

    -- Set project tempo and time signature
    set_project_tempo(tempo)
    set_time_signature(time_signature)

    -- Load MIDI file and start recording
    load_midi_file(midi_path)
    reaper.Main_OnCommand(40042, 0) -- Transport: Go to start of project
    start_recording()

    -- Wait for the length of the MIDI file
    local midi_length = get_midi_length_in_seconds(midi_path)
    wait(midi_length)

    -- Stop recording
    stop_recording()

    -- Save the recorded project as a single WAV file
    local output_file_path = output_dir .. "/" .. midi_file:gsub("%.mid$", "_converted.wav")
    save_project_as(output_file_path)

    -- Clear tracks and go to the start of the project
    clear_imported_midi_data()
    reaper.Main_OnCommand(40042, 0) -- Transport: Go to start of project

    -- Increment the test run counter and check if the maximum has been reached
    test_run_counter = test_run_counter + 1
    if test_run_counter >= max_test_runs then
        debug_msg("Maximum test runs reached. Stopping script.")
        break
    end

    ::continue::
end

debug_msg("Script finished.")
‚