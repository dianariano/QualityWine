import numpy as np
import pandas as pd
from sklearn import metrics

def evaluationModel(output, out_pred):

    return metrics.accuracy_score(output, out_pred)