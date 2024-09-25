# GrooveLens

**GrooveLens** is a study project for the course audio data science at University of Applied Sciences Düsseldorf and detects the genre of a drum beat recording. The model is trained on the [Groove MIDI Dataset](https://magenta.tensorflow.org/datasets/groove) and combines predictions of a convolutional neural network, based on the front-end of [musicnn](https://github.com/jordipons/musicnn), and a random forest classifier.

## Table of Contents

- [GrooveLens](#groovelens)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Knerten0815/GrooveLens
    cd GrooveLens
    ```

2. Install with conda using the provided ``conda_env_cpu.yml`` file. 
    ```bash
    conda env create -f conda_env_cpu.yml
    ```

    Windows users can run the model on their GPU for better performance when using the ``conda_env_gpu_windows.yml`` file instead. 

3. Download the model files from [here](https://fhd.sharepoint.com/:u:/t/GeoCougher/EXtLhl6SuUNEobNJPG8ZZsABpdeIw7mlaiTu82cEWfJubQ?e=B3i9DU) and extract the contents to the root folder.
4. If you want to train the model yourself, download the [Groove MIDI Dataset](https://magenta.tensorflow.org/datasets/groove) and extract the files to a ``Datasets`` folder in the root directory.
5. If you only want to evaluate the model and skip the preprocessing, you can download the CSV file wih the extracted audio features and the generated spectograms from [here](https://fhd.sharepoint.com/:u:/t/GeoCougher/ESW0npAsNc5FqD1C8cuNDZgBg4i-Tt4ISpRhM5lW7AX78w?e=mi5MU7). Extract the contents to the root folder.

Your folder structure should look something like this:
```plaintext
GrooveLens/
├── code/
│   ├── ...
├── data/
│   ├── models/
│   │   ├── ...
├── Datasets/
│   ├── groove/
│   │   ├── ...
│   ├── spectrums_grayscale/
│   │   ├── ...
├── evaluation/
│   ├── ...
├── Notebooks/
|   ├── data_balanced_processed_new.csv
│   ├── ...
├── Utility/
│   ├── ...
├── ...
```

## Usage

1. Activate the conda environment:
    ```bash
    conda activate groovelens
    ```

2. Run the model on a drum recording using the following command:
    ```bash
    python ./main.py --file path/to/your/file.wav
    ```

    You can also use the arguments ``--start`` and ``--end`` to specify wich part of the audio file you want to classify. Use the ``--sampling_rate`` argument if your files sampling rate is not 44100 Hz.
