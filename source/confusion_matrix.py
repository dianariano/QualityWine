import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def confMatrix(predict, test):

    mat = confusion_matrix(predict, test)
    names = np.unique(predict)
    sns.heatmap(mat, annot=True, cbar=False, 
                xticklabels = names, yticklabels= names)
    plt.xlabel('Truth')
    plt.ylabel('Predicted')
    plt.show()

    return mat