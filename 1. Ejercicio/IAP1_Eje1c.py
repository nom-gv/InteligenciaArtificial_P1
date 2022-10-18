
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona.csv', sep=';', encoding='latin-1')

data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
data

#GRAFICOS PARA REALIZAR EL EJERCICIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets


Filtro=data[data['Nivel edu']==0].index
Data_E=data.drop(Filtro)
Data_E['Nivel edu']=pd.to_numeric(Data_E['Nivel edu'])

sns.set(style="ticks")
#Obtenemos los niveles de educacion segun la edad de cada sexo
sns.lmplot(x='Nivel edu', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de educacion segun la edad de cada zona
sns.lmplot(x='Nivel edu', y='Edad', col='Zona', hue='Zona', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de educacion segun la edad de embarazos
sns.lmplot(x='Nivel edu', y='Edad', col='Embarazo', hue='Embarazo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de educacion segun la edad de personas procediente de algun pueblo
sns.lmplot(x='Nivel edu', y='Edad', col='Pueblo', hue='Pueblo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenermos los niveles de educacion segun el estado civil de cada sexo
sns.lmplot(x='Nivel edu', y='Estado Civil', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenermos los niveles de educacion segun el estado civil de cada zona
sns.lmplot(x='Nivel edu', y='Estado Civil', col='Zona', hue='Zona', data=Data_E,  height=6, ci=None, palette="muted");

#Realizamos la matriz de disperción de la edad y los niveles de educacion
Data_Bil = pd.DataFrame(Data_E, columns=['Sexo', 'Edad', 'Nivel edu'])

sns.pairplot(Data_Bil, hue='Sexo')  
plt.show()


Filtro=data[data['Prox Nivel ed']==0].index
Data_E=data.drop(Filtro)
Data_E['Prox Nivel ed']=pd.to_numeric(Data_E['Prox Nivel ed'])
print(Data_E.head(n=10))
sns.set(style="ticks")
#Obtenemos los niveles proximos de educacion segun la edad de cada sexo
sns.lmplot(x='Prox Nivel ed', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles proximos de educacion segun la edad de cada zona
sns.lmplot(x='Prox Nivel ed', y='Edad', col='Zona', hue='Zona', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles proximos de educacion segun la edad de embarazos
sns.lmplot(x='Prox Nivel ed', y='Edad', col='Embarazo', hue='Embarazo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles proximos de educacion segun la edad de personas procediente de algun pueblo
sns.lmplot(x='Prox Nivel ed', y='Edad', col='Pueblo', hue='Pueblo', data=Data_E,  height=6, ci=None, palette="muted");



Filtro=data[data['Estado Civil']==0].index
Data_E=data.drop(Filtro)
Data_E['Estado Civil']=pd.to_numeric(Data_E['Estado Civil'])
#Obtenemos el estado civil por edad de cada sexo
sns.lmplot(x='Estado Civil', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos el estado civil por edad de cada zona
sns.lmplot(x='Estado Civil', y='Edad', col='Zona', hue='Zona', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos el estado civil por edad de cada mujer embarazada
sns.lmplot(x='Estado Civil', y='Edad', col='Embarazo', hue='Embarazo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos el estado civil por edad de cada persona procediente de algun pueblo
sns.lmplot(x='Estado Civil', y='Edad', col='Pueblo', hue='Pueblo', data=Data_E,  height=6, ci=None, palette="muted");


#REALIZAMOS LA EXTRACCIÓN DE LOS DATOS DE LUGAR DE RECIDENCIA PARA CADA SEXO POR RANGO DE EDAD
grupo_edad = pd.cut(data['Edad'], bins=[0, 20, 40, 60, np.inf])
grupo_edad

data2 = data
data2['Sexo'] = data2['Sexo'].replace({1: "Hombre", 2: "Mujer"})
data2['Lugar 5 años'] = data2['Lugar 5 años'].replace({1: "Aqui", 2: "En otro lugar", 3: "En el exterior", 4:"Aun no habia nacido"})

dataC = pd.crosstab(grupo_edad, [data2['Sexo'], data['Lugar 5 años']])
#Obtenemos la gráfica de linea para el rango de edad y los datos recidencia hace 5 años de los sexos
dataC.plot(kind='line', figsize=(10, 5))
#Obtenemos la gráfica de barras para el rango de edad y los datos recidencia hace 5 años los sexos
dataC.plot(kind='barh', figsize=(10, 6))
#Obtenemos la gráfica de histograma para el rango de edad y los datos recidencia hace 5 años  de los sexos
dataC.plot(kind='hist', figsize=(10, 5))
#Obtenemos la gráfica de area para el rango de edad y los datos recidencia hace 5 años de los sexos
dataC.plot(kind='area', figsize=(10, 5))
#Obtenemos las gráficas de pastel para los rangos de edad para los datos recidencia hace 5 años de ambos sexos
dataC.plot(kind='pie', subplots=True, figsize=(20,20), autopct='%1.1f%%')
#Obtenemos las gráficas de barras para los rangos de edad para los datos recidencia hace 5 años  de ambos sexos
dataC.plot(subplots=True, figsize=(6,10), kind='bar');


#REALIZAMOS LA EXTRACCION DE LOS DATOS DE ALFABETIZADOS PARA CADA SEXO POR RANGO DE EDAD
grupo_edad = pd.cut(data['Edad'], bins=[0, 20, 40, 60, np.inf])
grupo_edad

data2 = data
data2['Sexo'] = data2['Sexo'].replace({1: "Hombre", 2: "Mujer"})
data2['Leer y Escribir'] = data2['Leer y Escribir'].replace({0: "No corresponde", 1: "Si", 2: "No"})

dataC = pd.crosstab(grupo_edad, [data2['Sexo'], data['Leer y Escribir']])
#Obtenemos la gráfica de linea para el rango de edad y los datos de alfabetizacion de los sexos
dataC.plot(kind='line', figsize=(10, 5))
#Obtenemos la gráfica de barras para el rango de edad y los datos de alfabetizacion los sexos
dataC.plot(kind='barh', figsize=(10, 6))
#Obtenemos la gráfica de histograma para el rango de edad y los datos de alfabetizacion de los sexos
dataC.plot(kind='hist', figsize=(10, 5))
#Obtenemos la gráfica de area para el rango de edad y los datos de alfabetizacion de los sexos
dataC.plot(kind='area', figsize=(10, 5))
#Obtenemos las gráficas de pastel para los rangos de edad para los datos de alfabetizacion de ambos sexos
dataC.plot(kind='pie', subplots=True, figsize=(20,20), autopct='%1.1f%%')
#Obtenemos las gráficas de barras para los rangos de edad para los datos de alfabetizacion de ambos sexos
dataC.plot(subplots=True, figsize=(6,10), kind='bar');

