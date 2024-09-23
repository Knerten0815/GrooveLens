import pandas as pd
import numpy as np
import os
import librosa
import matplotlib.pyplot as plt
from tqdm import tqdm

def generate_spectogram(mel_spect, filesuffix):
    os.makedirs('temp', exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(500 / 100, 200 / 100))

    librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time', cmap='gray')
    
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_axis_off()
    fig.subplots_adjust(left=0, bottom=0, right=0.1, top=0.1, wspace=0, hspace=0)
    plt.tight_layout(pad=0)
    plt.savefig(f'temp/spectogram-{filesuffix}.png', format='png')
    plt.close('all')

def audio_feature_extraction(y, sr, stft, n_fft, hop_length):
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)
    mel_spect = librosa.power_to_db(mel_spect, ref=np.max)
    
    # Berechnung der Merkmale
    onset_env_mean = onset_env.mean()
    onset_env_std = onset_env.std()
    
    # Berechnen des STFT und des Spectral Flux
    spectral_flux = np.sqrt(np.mean((np.diff(stft, axis=1))**2, axis=0))
    spectral_flux_mean = spectral_flux.mean()
    spectral_flux_std = spectral_flux.std()
    
    bpm_extracted, beats = librosa.beat.beat_track(y=y, sr=sr, start_bpm=110, hop_length=hop_length)
    if isinstance(bpm_extracted, np.ndarray):
        bpm_extracted = float(bpm_extracted[0])

    # Reduziere n_mels und passe fmax an, um leere Filter zu vermeiden
    n_mels = 40
    fmax = sr / 2
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels, fmax=fmax)
    mfcc_mean = mfcc.mean()
    mfcc_std = mfcc.std()

    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)
    spectral_contrast_mean = spectral_contrast.mean()
    spectral_contrast_std = spectral_contrast.std()

    tonnetz = librosa.feature.tonnetz(y=y, sr=sr, hop_length=hop_length)
    tonnetz_mean = tonnetz.mean()
    tonnetz_std = tonnetz.std()

    rms = librosa.feature.rms(y=y, frame_length=n_fft, hop_length=hop_length)
    rms_mean = rms.mean()
    rms_std = rms.std()

    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)
    spectral_centroid_mean = spectral_centroid.mean()
    spectral_centroid_std = spectral_centroid.std()

    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length)
    spectral_bandwidth_mean = spectral_bandwidth.mean()
    spectral_bandwidth_std = spectral_bandwidth.std()

    spectral_flatness = librosa.feature.spectral_flatness(y=y, n_fft=n_fft, hop_length=hop_length)
    spectral_flatness_mean = spectral_flatness.mean()
    spectral_flatness_std = spectral_flatness.std()

    tempogram = librosa.feature.tempogram_ratio(y=y, sr=sr)
    tempogram_mean = librosa.feature.tempogram_ratio(y=y, sr=sr).mean()
    tempogram_std = librosa.feature.tempogram_ratio(y=y, sr=sr).std()
    
    return {
        'onset_strengths': onset_env,
        'onset_frames': onset_frames,
        'melspectogram': mel_spect,
        'bpm_extracted': bpm_extracted,
        'onset_env_mean': onset_env_mean,
        'onset_env_std': onset_env_std,
        'spectral_flux_mean': spectral_flux_mean,
        'spectral_flux_std': spectral_flux_std,
        'mfcc_mean': mfcc_mean,
        'mfcc_std': mfcc_std,
        'spectral_contrast_mean': spectral_contrast_mean,
        'spectral_contrast_std': spectral_contrast_std,
        'tonnetz_mean': tonnetz_mean,
        'tonnetz_std': tonnetz_std,
        'rms_mean': rms_mean,
        'rms_std': rms_std,
        'spectral_centroid_mean': spectral_centroid_mean,
        'spectral_centroid_std': spectral_centroid_std,
        'spectral_bandwidth_mean': spectral_bandwidth_mean,
        'spectral_bandwidth_std': spectral_bandwidth_std,
        'spectral_flatness_mean': spectral_flatness_mean,
        'spectral_flatness_std': spectral_flatness_std,
        'tempogram_mean': tempogram_mean,
        'tempogram_std': tempogram_std
    }

def process_sample(y, sr, filesuffix):
    # librosa magic
    n_fft = min(1024, len(y))
    hop_length = n_fft // 2
    stft = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
    
    features = audio_feature_extraction(y, sr, stft, n_fft, hop_length)
    generate_spectogram(features['melspectogram'], filesuffix)
    
    return pd.Series(features)

def process_file(file, sampling_rate, start, end):
    try:
        if(end is None):
            y, sr = librosa.load(file, sr=sampling_rate)
            duration = librosa.get_duration(y=y, sr=sr)
        else:
            duration = end-start
            y, sr = librosa.load(file, sr=sampling_rate, offset=start, duration=duration)
    except Exception as e:
        print(f"Error loading {file}: {e}")
        return
    
    feature_df = pd.DataFrame(columns=['onset_strengths', 'onset_frames', 'melspectogram', 'bpm_extracted',
                                       'onset_env_mean', 'onset_env_std',
                                       'spectral_flux_mean', 'spectral_flux_std',
                                       'mfcc_mean', 'mfcc_std',
                                       'spectral_contrast_mean', 'spectral_contrast_std',
                                       'tonnetz_mean', 'tonnetz_std', 
                                       'rms_mean', 'rms_std',
                                       'spectral_centroid_mean', 'spectral_centroid_std',
                                       'spectral_bandwidth_mean', 'spectral_bandwidth_std',
                                       'spectral_flatness_mean', 'spectral_flatness_std',
                                       'tempogram_mean', 'tempogram_std'])
    
    print(f"Processing {file}. Duration: {duration}")
    for i in tqdm(range(0, int(duration)-2, 3)):
        y_slice = y[i*sr:(i+3)*sr]
        features = process_sample(y_slice, sr, i)
        feature_df = pd.concat([feature_df, features.to_frame().T], ignore_index=True)
    
    return feature_df