Press `Ctrl+Shift+V` in VSCode to preview the markdown.

# Classification Report for RANDOM_FOREST_NO_LEAKAGE

__Hamming Loss__ = 0.5295698924731183

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.56 | 0.39 | 0.46 | 61 |
| hiphop | 0.45 | 0.56 | 0.50 | 62 |
| jazz | 0.67 | 0.58 | 0.62 | 62 |
| latin | 0.37 | 0.45 | 0.41 | 60 |
| pop | 0.45 | 0.30 | 0.36 | 66 |
| rock | 0.41 | 0.54 | 0.47 | 61 |
|  |
| accuracy | 0.47 | 372 |
| macro | avg | 0.49 | 0.47 | 0.47 | 372 |
| weighted | avg | 0.49 | 0.47 | 0.47 | 372 |


![Image](..\evaluation\images\confusion_matrix_RANDOM_FOREST_NO_LEAKAGE2.png)


# Classification Report for CROPPED_IMAGES_SMALL (no more data leakage)

__Hamming Loss__ = 0.7849462365591398

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.11 | 0.14 | 0.12 | 28 |
| hiphop | 0.33 | 0.19 | 0.25 | 36 |
| jazz | 0.18 | 0.21 | 0.19 | 29 |
| latin | 0.38 | 0.48 | 0.43 | 27 |
| pop | 0.24 | 0.11 | 0.15 | 36 |
| rock | 0.14 | 0.20 | 0.16 | 30 |
|  |
| accuracy | 0.22 | 186 |
| macro | avg | 0.23 | 0.22 | 0.22 | 186 |
| weighted | avg | 0.23 | 0.22 | 0.21 | 186 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES_SMALL3.png)


# Classification Report for CROPPED_IMAGES_SMALL (but with Data Leakage)

__Hamming Loss__ = 0.6777777777777778

| precision | recall | f1-score | support |
| --- | --- | --- | --- |
|  |
| funk | 0.29 | 0.54 | 0.38 | 13 |
| hiphop | 0.38 | 0.38 | 0.38 | 13 |
| jazz | 0.19 | 0.20 | 0.19 | 15 |
| latin | 0.33 | 0.38 | 0.36 | 13 |
| pop | 0.50 | 0.31 | 0.38 | 16 |
| rock | 0.33 | 0.20 | 0.25 | 20 |
|  |
| accuracy | 0.32 | 90 |
| macro | avg | 0.34 | 0.34 | 0.32 | 90 |
| weighted | avg | 0.34 | 0.32 | 0.32 | 90 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES_SMALL2.png)


# Classification Report for CROPPED_IMAGES (but with Data Leakage)

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