# from pyspark.sql import SparkSession
# from pyspark.sql import SQLContext
# from pyspark.sql.types import *
# from pyspark.sql.functions import *
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

    #spark = SparkSession.builder.appName("Video Recomendation").getOrCreate()
    #sc = spark.sparkContext

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
    print('tipos de dados do dataset que se usara na analisis exploratoria :  \n' + str(df_wine.dtypes) + ' \n')
    print('Descrição matematica das colunas numericas no dataset de vinho :  \n ' + str(df_wine.describe()) + ' \n')

    plotHistograms(nameColumns, df_wine)
    

    return dataWithoutDup