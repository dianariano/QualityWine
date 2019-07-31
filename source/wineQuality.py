import sys
from create_dataframe import *
from exploratory_data import eda
from classification_model import *

__author__ = 'Diana Riano'

def wineQuality():
    
    print('Python %s on %s' % (sys.version, sys.platform))
    
    for param in sys.argv :
       
        try:
            sourcefile = param
        
        except:
            sourcefile = '../data/winequality.csv'

        print('Arquivo csv que contem os dados do dataset de vinhos: '+ sourcefile)

    df_file = df_create(sourcefile)
    df_wine = eda(df_file) 
    out_test, data_predicted = classificationModel(df_wine)
    confMatrix(data_predicted, out_test)
    precision, accuracy = evaluationModel(out_test, data_predicted)
    
    print("Accuracy para modelo considerando 10 categorias: " + str(accuracy*100) + '%\n' )
    print("Precisão para modelo considerando 10 categorias: " + str(precision*100) + '%\n' 

if __name__ == "__main__":
    wineQuality()

