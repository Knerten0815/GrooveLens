from code import process_file
from code import cnn_predict
from code import random_forest_predict
import argparse
import shutil
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict the genre of a drum beat.')
    parser.add_argument('--file', type=str, help='Path to the audio file')
    parser.add_argument('--start', type=float, default=0, help='Start time in seconds. Default is 0.')
    parser.add_argument('--end', type=float, default=None, help='End time in seconds. Default is None, which means the end of the track.')
    parser.add_argument('--sampling_rate', type=int, default=44100, help='Sampling rate in Hz. Default is 44100.')

    args = parser.parse_args()

    # extract features and generate temporary spectograms images
    feature_df = process_file(args.file, args.sampling_rate, args.start, args.end)
    # predict based on spectograms
    cnn_propabilities = cnn_predict()   #funk', 'hiphop', 'jazz', 'latin', 'pop', 'rock'
    # delete all the tempory spectograms
    shutil.rmtree('temp')
    # predict based on extracted features
    rf_propabilities = random_forest_predict(feature_df)    #'funk', 'hiphop', 'jazz', 'latin', 'pop', 'rock'
    
    # sum up the probabilities
    probs = rf_propabilities + cnn_propabilities
    probs = np.sum(probs, axis=0)
    final_prediction = np.argmax(probs)
    
    genres = ['funk', 'hiphop', 'jazz', 'latin', 'pop', 'rock']
    
    print("\nFinal Prediction: ")
    print(f"That's a typical \033[92m{genres[final_prediction]}\033[0m beat!")

