import os
import re
import time
import mido
import reaper_python as RPR

midi_dir = "Datasets/groove"
# Directory to save the audio files
output_dir = "Datasets/converted"
# Log file to keep track of processed files
log_file_path = "Datasets/logs"

# Function to get tempo and time signature from filename
def get_tempo_and_time_signature_from_filename(filename):
    parts = filename.split('_')
    if len(parts) >= 4:
        try:
            tempo = int(parts[2])  # Extract the tempo (3rd position in 0-based index)
        except ValueError:
            tempo = None
    else:
        tempo = None

    time_signature_match = re.search(r'(\d+-\d+)\.mid$', filename)
    if time_signature_match:
        time_signature = time_signature_match.group(1).replace('-', '/')
    else:
        time_signature = "4/4"  # Default to 4/4 if not found

    return tempo, time_signature

# Function to set project time signature
def set_time_signature(time_signature):
    measures, beats = map(int, time_signature.split('/'))
    RPR.SetTempoTimeSigMarker(0, -1, -1, -1, -1, 0, measures, beats, True)

# Function to get the length of a MIDI file in seconds
def get_midi_length_in_seconds(midi_path):
    mid = mido.MidiFile(midi_path)
    return mid.length

# Function to record and save audio
def record_and_save_audio(filename, output_dir, duration):
    # Start recording
    RPR.OnRecord()
    # Wait for the recording to finish
    time.sleep(duration)
    # Stop recording
    RPR.OnStopButton()

    # Save project as audio file
    audio_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + ".wav")
    RPR.Main_SaveProject(audio_filename, 0)

# Function to clear the imported MIDI data from the track
def clear_imported_midi_data():
    track = RPR.GetTrack(0, 0)  # Get the first track
    item_count = RPR.CountTrackMediaItems(track)
    for i in range(item_count):
        item = RPR.GetTrackMediaItem(track, i)
        RPR.DeleteTrackMediaItem(track, item)

# Function to check if a file has been processed
def has_been_processed(filename):
    if not os.path.exists(log_file_path):
        return False
    with open(log_file_path, 'r') as log_file:
        processed_files = log_file.read().splitlines()
    return filename in processed_files

# Function to log a processed file
def log_processed_file(filename):
    with open(log_file_path, 'a') as log_file:
        log_file.write(filename + '\n')

counter = 0
# Process each MIDI file
for midi_file in os.listdir(midi_dir):
    if midi_file.endswith(".mid") and not has_been_processed(midi_file):
        midi_path = os.path.join(midi_dir, midi_file)
        
        # Load MIDI file into Reaper
        RPR.InsertMedia(midi_path, 0)

        # Get tempo and time signature from filename
        tempo, time_signature = get_tempo_and_time_signature_from_filename(midi_file)
        if tempo:
            # Set project tempo
            RPR.CSurf_OnTempoChange(tempo)
        
        # Set project time signature
        set_time_signature(time_signature)

        # Get MIDI length in seconds
        midi_length = get_midi_length_in_seconds(midi_path)

        # Record and save audio
        record_and_save_audio(midi_file, output_dir, midi_length)

        # Clear the imported MIDI data from the track
        clear_imported_midi_data()

        # Log the processed file
        log_processed_file(midi_file)
        counter += 1
        
        if counter > 5:
            break
