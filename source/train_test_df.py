from sklearn.model_selection import train_test_split

def split_Df(features, label):
        
    X_train, X_test, y_train, y_test = train_test_split(features, 
                                        label, test_size = 0.2, 
                                        random_state = 0)
    
    print("Para o modelo de treino serão usados 80% dos dados do dataset e para test 20%.")
    print("O set de treino tem {} amostras.".format(X_train.shape[0]))
    print("O set de test tem {} amostras.".format(X_test.shape[0]))

    return X_train, X_test, y_train, y_test