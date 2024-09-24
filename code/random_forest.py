import os
import pickle

def load_model(model):
    path_data = os.path.join('data', 'models')
    filepath = os.path.join(path_data, model)

    with open(filepath, 'rb') as model:
        rnd_forest = pickle.load(model)
    
    return rnd_forest

def predict(X, model ='RANDOM_FOREST_Extracted_BPM_full_file_model.pkl'):
    print("Calculating random forest predictions...")
    rnd_forest = load_model(model)
    X = X.drop(columns=['melspectogram'])
    return rnd_forest.predict_proba(X)