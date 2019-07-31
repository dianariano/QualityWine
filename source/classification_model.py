import numpy as np
import pandas as pd
from sklearn.preprocessing import *
from train_test_df import split_Df
from confusion_matrix import confMatrix
from sklearn.naive_bayes import GaussianNB
from evaluation_model import evaluationModel


def classificationModel(df_wine):

    le = LabelEncoder()
    df_wine['type_category']=le.fit_transform(df_wine['type'])

    #Defining the splits for categories. 1–4 will be poor quality, 5–6 will be average, 7–10 will be great
    bins = [1,4,6,10]

    #0 for low quality, 1 for average, 2 for great quality
    quality_labels=['0','1','2']
    df_wine['quality_categorical'] = pd.cut(df_wine['quality'], bins=bins, labels=quality_labels, include_lowest=True)

    output = df_wine['quality']
    output1 = df_wine['quality_categorical']
    features = df_wine.drop(['type','density','quality'], axis=1)

    features_train, features_test, label_train, label_test = split_Df(features, output)
    #features_train1, features_test1, label_train1, label_test1 = split_Df(features, output1)

    #Create a Gaussian Classifier
    model = GaussianNB()

    # Train the model using the training sets
    model.fit(standarSize(features_train),label_train)

    #Predict Output
    predicted = model.predict(standarSize(features_test))

    return label_test, predicted

def standarSize(data):

    scaler = StandardScaler().fit(data)
    rescaledX = scaler.transform(data)

    return rescaledX