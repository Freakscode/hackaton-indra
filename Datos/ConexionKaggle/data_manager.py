"""
Aquí irá el código para el tratamiento inicial de los datos (limpieza, transformación, etc.)
"""

import os
import pandas as pd

def load_data():
    """
    Carga los datos de entrenamiento y testeo
    """
    data_train = pd.read_csv(os.path.join('datos_hackaton', 'train_data.csv'))
    data_test = pd.read_csv(os.path.join('datos_hackaton', 'test_data.csv'))
    return data_train, data_test

def show_data(data_train, data_test):
    """
    Muestra los datos de entrenamiento y testeo
    """
    print("Datos de entrenamiento:")
    print(data_train.head())
    print("\nDatos de testeo:")
    print(data_test.head())
    
def data_transformation(data_train):
    """
    Transforma los datos, por ejemplo, codifica las variables categóricas a numéricas y elimina las columnas que no se usarán
    """
    print("Nombre de las columnas:")
    print(data_train.columns)
    ## Variables categóricas
    print("Variables categóricas:")
    print(data_train.select_dtypes(include=['object']).columns)
    ## Variables numéricas
    print("Variables numéricas:")
    print(data_train.select_dtypes(include=['int64', 'float64']).columns)
    ## Definir método de codificación de variables categóricas
    def encode_data(data_train):
        cat = data_train.select_dtypes(include=['object']).columns
        data_train = pd.get_dummies(data_train, columns=cat)
        print("Existen datos categoricos en el dataset?")
        print(data_train.select_dtypes(include=['object']).columns)
        return data_train
    data_train  = encode_data(data_train)

    return


