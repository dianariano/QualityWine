import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plot_histograms import *


__author__ = 'Diana Riano'

def isObject(column):
    return column.dtype == object

def change2Numeric(df_column, typeCol):

    df_column = pd.to_numeric(df_column, errors = 'coerce').fillna('NaN')
    df_column = df_column.astype(typeCol)

    return df_column

def eda(data):

    nameColumns = data.columns.tolist()
    columnsObject= [column for column in nameColumns if isObject(data[column])]
    print('Lista de colunas que são de tipo texto no dataset: ' + str(columnsObject))

    for column in columnsObject:
        if column != 'type':
            typeCol = float
            data[column] = change2Numeric(data[column], typeCol)

    dataWithoutDup = data.drop_duplicates()
    dataWithoutNA = dataWithoutDup.dropna()
    count_novalid = data.shape[0] - dataWithoutNA.shape[0]
    df_wine = dataWithoutNA 

    print('Numero de linhas não validas no dataset :  \n' + str(count_novalid) +' \n')
    print('Tipos de dados do dataset que se usara na analisis exploratoria :  \n' + str(df_wine.dtypes) + ' \n')
    print('Descrição matematica das colunas numericas no dataset de vinho :  \n ' + str(df_wine.describe()) + ' \n')
    
    plotHistograms(nameColumns[:4], df_wine)
    plotHistograms(nameColumns[4:8], df_wine)
    plotHistograms(nameColumns[8:12], df_wine)
    
    plt.hist(df_wine[nameColumns[-1]], density=True, histtype='bar', label=nameColumns[-1])
    plt.legend(prop={'size': 10})
    plt.show()

    return df_wine