from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType, TimestampType
import numpy as np
import pandas as pd

__author__ = 'Diana Riano'

def df_create(sourcefile):

    #spark = SparkSession.builder.appName("Wine Quality").getOrCreate()

    df_File = pd.read_csv(sourcefile, sep=';')

    print("O dataframe dos dados do arquivo foi criado.")
    print("Preview do dataframe criado:")
    print(str(df_File.head()))

    return (df_File)