import os
import pickle

def load_model(model):
    path_data = os.path.join('data', 'models')
    filepath = os.path.join(path_data, model)

    print(f"Loading model from {filepath}")
    with open(filepath, 'rb') as model:
        rnd_forest = pickle.load(model)
    
    return rnd_forest

def predict(X, model ='RANDOM_FOREST_Extracted_BPM_full_file_model.pkl'):
    rnd_forest = load_model(model)
    X = X.drop(columns=['melspectogram'])
    return rnd_forest.predict_proba(X)

#print(X_train.columns)
#    'bpm_extracted', 'onset_env_mean', 'onset_env_std', 'mfcc_mean',
#    'mfcc_std', 'spectral_flux_mean', 'spectral_flux_std',
#    'spectral_contrast_mean', 'spectral_contrast_std', 'tonnetz_mean',
#    'tonnetz_std', 'rms_mean', 'rms_std', 'spectral_centroid_mean',
#    'spectral_centroid_std', 'spectral_bandwidth_mean',
#    'spectral_bandwidth_std', 'spectral_flatness_mean',
#    'spectral_flatness_std', 'tempogram_mean', 'tempogram_std'