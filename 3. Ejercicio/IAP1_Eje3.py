# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona_comas.csv', encoding='latin-1')
data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
print(data)

#OneHotEncoder
#Codifica informacion para convertirla en codificacion binaria
df = data
df['Zona'] = preprocessing.OneHotEncoder().fit_transform(df[['Zona']]).toarray()
df['Sexo'] = preprocessing.OneHotEncoder().fit_transform(df[['Sexo']]).toarray()
df['Leer y Escribir'] = preprocessing.OneHotEncoder().fit_transform(df[['Leer y Escribir']]).toarray()
df['Sum y Mul'] = preprocessing.OneHotEncoder().fit_transform(df[['Sum y Mul']]).toarray()
df['Matricula'] = preprocessing.OneHotEncoder().fit_transform(df[['Matricula']]).toarray()
print(df)

#MinMax
#Escalar las caracteristicas para que se encuentren entre valor minimo y maximo
num_cols = df.select_dtypes(include=['int64','float64','int32'])
for col in num_cols:
    df[col] = preprocessing.MinMaxScaler().fit_transform(df[[col]])
print(df)


data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona.csv', sep=';', encoding='latin-1')
data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
df = data


#Standaridize
#Estandariza un conjundo de datos a lo largo de cualquier eje
matriz = np.array(df)
matriz = preprocessing.KBinsDiscretizer(matriz)
print(matriz)



'''matriz_salida_normalize = preprocessing.scale(matriz)
print('')
print(matriz_salida_normalize)

matriz_salida_minmaxscaler = preprocessing.MinMaxScaler(matriz)
#X_train_minmax = matriz_salida_minmaxscaler.fit_transform(matriz)
print('')
print(matriz_salida_minmaxscaler)'''
