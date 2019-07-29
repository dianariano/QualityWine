import sys
from pyspark import SparkContext
from pyspark import SparkConf
from create_dataframe import *
from exploratory_data import *
from pyspark.sql import SparkSession
# from jobs.ALSModel import *

__author__ = 'Diana Riano'

def main():


    #spark = SparkSession.builder.appName("Wine Quality").getOrCreate()
    #sc = spark.sparkContext.setLogLevel("ERROR")
    
    sourcefile = './data/winequality.csv'

    df_file = df_create(sourcefile)
    eda(df_file) 


    print('Python %s on %s' % (sys.version, sys.platform))
    #spark.stop()

if __name__ == "__main__":
    main()