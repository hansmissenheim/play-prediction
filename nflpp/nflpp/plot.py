import matplotlib as mpl
import mplcatppuccin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import auc, confusion_matrix, roc_curve

mpl.style.use("mocha")


AXIS_LABELS = ["Pass", "Run"]
Array = pd.Series | np.ndarray


def plot_confusion_matrix(targets: Array, predictions: Array):
    cm = confusion_matrix(targets, predictions)
    plt.imshow(cm, interpolation="nearest")

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Play Call")
    plt.ylabel("True Play Call")
    plt.xticks([0, 1], AXIS_LABELS)
    plt.yticks([0, 1], AXIS_LABELS)

    for i in range(2):
        for j in range(2):
            plt.text(j, i, cm[i, j], horizontalalignment="center")

    plt.show()


def plot_roc_curve(targets: Array, probs: Array):
    y_score = probs[:, 1]
    false_positive_rate, true_positive_rate, _ = roc_curve(targets, y_score)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    curve_label = f"ROC curve (area = {roc_auc:.2f})"
    plt.plot(false_positive_rate, true_positive_rate, lw=2, label=curve_label)
    plt.fill_between(false_positive_rate, true_positive_rate, alpha=0.25)
    plt.plot([0, 1], [0, 1], lw=2, linestyle="--")

    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.xlim([-0.005, 1])
    plt.ylim([0, 1.01])

    plt.show()
