from sklearn.metrics import multilabel_confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, hamming_loss
import seaborn as sns

def evaluate_model(model, X_validation, y_validation):
    y_predicted = model.predict(X_validation)
    
    print("Classification Report:")
    print(classification_report(y_validation, y_predicted, target_names=y.columns))
    
    print("\nHamming Loss:", hamming_loss(y_validation, y_predicted))

def plot_confusion_matrix(conf_matrix, labels, selected_labels):
    fig, ax = plt.subplots(2, 5, figsize=(20, 6))
    for axes, label in zip(ax.flatten(), selected_labels):
        matrix = conf_matrix[labels.index(label)]
        sns.heatmap(matrix, annot=True, ax=axes, fmt='d', cmap='vlag')
        axes.set_title(f'{label} Confusion Matrix')
        axes.set_xlabel('Predicted Values')
        axes.set_ylabel('True Values')
    plt.tight_layout()
    plt.show()