Press `Ctrl+Shift+V` in VSCode to preview the markdown.

# Classification Report for RANDOM_BASELINE

__Hamming Loss__ = 0.8222222222222222

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.06 | 0.07 | 0.06 | 28 |
| hiphop | 0.25 | 0.17 | 0.20 | 36 |
| jazz | 0.00 | 0.00 | 0.00 | 29 |
| latin | 0.10 | 0.07 | 0.08 | 27 |
| pop | 0.27 | 0.25 | 0.26 | 36 |
| rock | 0.11 | 0.17 | 0.13 | 30 |
|  |
| accuracy ||  | 0.13 | 186 |
| macro | avg | 0.13 | 0.12 | 0.12 | 186 |
| weighted | avg | 0.14 | 0.13 | 0.13 | 186 |


![Image](..\evaluation\images\confusion_matrix_RANDOM_BASELINE.png)


# Classification Report for ALL_5S_BASELINE

__Hamming Loss__ = 0.7777777777777778

|   | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|  |  |  |  |
| funk | 0.00 | 0.00 | 0.00 | 28 |
| hiphop | 0.00 | 0.00 | 0.00 | 36 |
| jazz | 0.00 | 0.00 | 0.00 | 29 |
| latin | 0.00 | 0.00 | 0.00 | 27 |
| pop | 0.00 | 0.00 | 0.00 | 36 |
| rock | 0.16 | 1.00 | 0.28 | 30 |
|  |
| accuracy ||  | 0.16 | 186 |
| macro | avg | 0.03 | 0.17 | 0.05 | 186 |
| weighted | avg | 0.03 | 0.16 | 0.04 | 186 |


![Image](..\evaluation\images\confusion_matrix_ALL_5S_BASELINE.png)