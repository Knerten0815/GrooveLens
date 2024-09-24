Press `Ctrl+Shift+V` in VSCode to preview the markdown.


# Classification Report for UPDATED_ARCHITECTURE4

__Hamming Loss__ = 0.5860215053763441

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.37 | 0.25 | 0.30 | 28 |
| hiphop | 0.42 | 0.42 | 0.42 | 36 |
| jazz | 0.54 | 0.24 | 0.33 | 29 |
| latin | 0.41 | 0.74 | 0.53 | 27 |
| pop | 0.40 | 0.47 | 0.43 | 36 |
| rock | 0.42 | 0.37 | 0.39 | 30 |
|  |
| accuracy |  |  | 0.41 | 186 |
| macro | avg | 0.43 | 0.41 | 0.40 | 186 |
| weighted | avg | 0.42 | 0.41 | 0.40 | 186 |


![Image](..\evaluation\images\confusion_matrix_UPDATED_ARCHITECTURE4.png)


# Classification Report for UPDATED_ARCHITECTURE

__Hamming Loss__ = 0.6666666666666666

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.17 | 0.18 | 0.17 | 28 |
| hiphop | 0.52 | 0.44 | 0.48 | 36 |
| jazz | 0.33 | 0.59 | 0.42 | 29 |
| latin | 0.52 | 0.59 | 0.55 | 27 |
| pop | 0.29 | 0.06 | 0.09 | 36 |
| rock | 0.17 | 0.20 | 0.18 | 30 |
|  |
| accuracy |  |  | 0.33 | 186 |
| macro | avg | 0.33 | 0.34 | 0.32 | 186 |
| weighted | avg | 0.33 | 0.33 | 0.31 | 186 |


![Image](..\evaluation\images\confusion_matrix_UPDATED_ARCHITECTURE.png)


# Classification Report for CROPPED_IMAGES_SMALL (no more data leakage)

__Hamming Loss__ = 0.7849462365591398

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.11 | 0.14 | 0.12 | 28 |
| hiphop | 0.33 | 0.19 | 0.25 | 36 |
| jazz | 0.18 | 0.21 | 0.19 | 29 |
| latin | 0.38 | 0.48 | 0.43 | 27 |
| pop | 0.24 | 0.11 | 0.15 | 36 |
| rock | 0.14 | 0.20 | 0.16 | 30 |
|  |
| accuracy  |  | | 0.22 | 186 |
| macro | avg | 0.23 | 0.22 | 0.22 | 186 |
| weighted | avg | 0.23 | 0.22 | 0.21 | 186 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES_SMALL3.png)


# Classification Report for CROPPED_IMAGES_SMALL (but with Data Leakage)

__Hamming Loss__ = 0.6777777777777778

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.29 | 0.54 | 0.38 | 13 |
| hiphop | 0.38 | 0.38 | 0.38 | 13 |
| jazz | 0.19 | 0.20 | 0.19 | 15 |
| latin | 0.33 | 0.38 | 0.36 | 13 |
| pop | 0.50 | 0.31 | 0.38 | 16 |
| rock | 0.33 | 0.20 | 0.25 | 20 |
|  |
| accuracy |  |  | 0.32 | 90 |
| macro | avg | 0.34 | 0.34 | 0.32 | 90 |
| weighted | avg | 0.34 | 0.32 | 0.32 | 90 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES_SMALL2.png)


# Classification Report for CROPPED_IMAGES (but with Data Leakage)

__Hamming Loss__ = 0.7111111111111111

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.27 | 0.31 | 0.29 | 13 |
| hiphop | 0.16 | 0.23 | 0.19 | 13 |
| jazz | 0.40 | 0.27 | 0.32 | 15 |
| latin | 0.24 | 0.38 | 0.29 | 13 |
| pop | 0.44 | 0.44 | 0.44 | 16 |
| rock | 0.33 | 0.15 | 0.21 | 20 |
|  |
| accuracy |  |  | 0.29 | 90 |
| macro | avg | 0.31 | 0.30 | 0.29 | 90 |
| weighted | avg | 0.31 | 0.29 | 0.29 | 90 |


![Image](..\evaluation\images\confusion_matrix_CROPPED_IMAGES.png)

# Classification Report for UNBALANCED_DATA & UNCROPPED_IMAGES

__Hamming Loss__ = 0.6029411764705882

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.43 | 0.55 | 0.48 | 29 |
| hiphop | 0.00 | 0.00 | 0.00 | 6 |
| jazz | 0.00 | 0.00 | 0.00 | 2 |
| latin | 0.50 | 0.20 | 0.29 | 10 |
| pop | 0.00 | 0.00 | 0.00 | 2 |
| rock | 0.33 | 0.47 | 0.39 | 19 |
|  |
| accuracy |  |  | 0.40 | 68 |
| macro | avg | 0.21 | 0.20 | 0.19 | 68 |
| weighted | avg | 0.35 | 0.40 | 0.36 | 68 |


![Image](..\evaluation\images\confusion_matrix_UNCROPPED_IMAGES.png)