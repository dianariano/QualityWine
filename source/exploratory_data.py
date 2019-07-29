# from pyspark.sql import SparkSession
# from pyspark.sql import SQLContext
# from pyspark.sql.types import *
# from pyspark.sql.functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


__author__ = 'Diana Riano'

def eda(data):

    #spark = SparkSession.builder.appName("Video Recomendation").getOrCreate()
    #sc = spark.sparkContext

    infoData =  data.info()
    nameColumns = data.columns.tolist()
    dataWithoutDup = data.drop_duplicates()
    countDuplicates = [i for i in range(data) if data.duplicated()[i] == True]
    
    for column in nameColumns:
        column['values'] = data[column].unique()
        column['max'] = data[column].max()
        print()
    data.head()



    df_eda.describe().show()


    return df_eda