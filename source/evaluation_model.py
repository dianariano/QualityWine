import numpy as np
import pandas as pd
from sklearn import metrics

def evaluationModel(output, out_pred):

    precision = metrics.precision_score(output, out_pred, average = 'macro')
    accuracy = metrics.accuracy_score(output, out_pred)
    
    return precision, accuracy