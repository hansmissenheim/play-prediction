import matplotlib as mpl
import mplcatppuccin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

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
