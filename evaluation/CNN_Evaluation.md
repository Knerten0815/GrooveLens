Press `Ctrl+Shift+V` in VSCode to preview the markdown.

# Classification Report for RANDOM_FOREST

__Hamming Loss__ = 0.37916666666666665

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.48 | 0.54 | 0.51 | 39 |
| hiphop | 0.68 | 0.66 | 0.67 | 38 |
| jazz | 0.59 | 0.75 | 0.66 | 32 |
| latin | 0.61 | 0.57 | 0.59 | 40 |
| pop | 0.72 | 0.86 | 0.78 | 42 |
| rock | 0.67 | 0.41 | 0.51 | 49 |
|  |
| accuracy | 0.62 | 240 |
| macro | avg | 0.62 | 0.63 | 0.62 | 240 |
| weighted | avg | 0.63 | 0.62 | 0.61 | 240 |


![Image](..\evaluation\images\confusion_matrix_RANDOM_FOREST.png)



# Classification Report for BALANCED_DATA & CROPPED_IMAGES

__Hamming Loss__ = 0.7111111111111111

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.27 | 0.31 | 0.29 | 13 |
| hiphop | 0.16 | 0.23 | 0.19 | 13 |
| jazz | 0.40 | 0.27 | 0.32 | 15 |
| latin | 0.24 | 0.38 | 0.29 | 13 |
| pop | 0.44 | 0.44 | 0.44 | 16 |
| rock | 0.33 | 0.15 | 0.21 | 20 |
|  |
| accuracy | 0.29 | 90 |
| macro | avg | 0.31 | 0.30 | 0.29 | 90 |
| weighted | avg | 0.31 | 0.29 | 0.29 | 90 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES.png)

# Classification Report for UNBALANCED_DATA & UNCROPPED_IMAGES

__Hamming Loss__ = 0.6029411764705882

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.43 | 0.55 | 0.48 | 29 |
| hiphop | 0.00 | 0.00 | 0.00 | 6 |
| jazz | 0.00 | 0.00 | 0.00 | 2 |
| latin | 0.50 | 0.20 | 0.29 | 10 |
| pop | 0.00 | 0.00 | 0.00 | 2 |
| rock | 0.33 | 0.47 | 0.39 | 19 |
|  |
| accuracy | 0.40 | 68 |
| macro | avg | 0.21 | 0.20 | 0.19 | 68 |
| weighted | avg | 0.35 | 0.40 | 0.36 | 68 |


![Image](..\evaluation\images\confusion_matrix_UNCROPPED_IMAGES.png)

# Classification Report for RANDOM_BASELINE

__Hamming Loss__ = 0.8222222222222222

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.15 | 0.15 | 0.15 | 13 |
| hiphop | 0.24 | 0.31 | 0.27 | 13 |
| jazz | 0.07 | 0.07 | 0.07 | 15 |
| latin | 0.15 | 0.15 | 0.15 | 13 |
| pop | 0.17 | 0.19 | 0.18 | 16 |
| rock | 0.29 | 0.20 | 0.24 | 20 |
|  |
| accuracy | 0.18 | 90 |
| macro | avg | 0.18 | 0.18 | 0.18 | 90 |
| weighted | avg | 0.18 | 0.18 | 0.18 | 90 |


![Image](..\evaluation\images\confusion_matrix_RANDOM_BASELINE.png)


# Classification Report for ALL_5S_BASELINE

__Hamming Loss__ = 0.7777777777777778

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.00 | 0.00 | 0.00 | 13 |
| hiphop | 0.00 | 0.00 | 0.00 | 13 |
| jazz | 0.00 | 0.00 | 0.00 | 15 |
| latin | 0.00 | 0.00 | 0.00 | 13 |
| pop | 0.00 | 0.00 | 0.00 | 16 |
| rock | 0.22 | 1.00 | 0.36 | 20 |
|  |
| accuracy | 0.22 | 90 |
| macro | avg | 0.04 | 0.17 | 0.06 | 90 |
| weighted | avg | 0.05 | 0.22 | 0.08 | 90 |


![Image](..\evaluation\images\confusion_matrix_ALL_5S_BASELINE.png)