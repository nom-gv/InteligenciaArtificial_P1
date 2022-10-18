# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona.csv', sep=';', encoding='latin-1')
data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
data

print(data)
#Reemplazamos los valores perdidos con la media de cada columna
import numpy as np
import graphviz
from sklearn import tree
from sklearn.impute import SimpleImputer
X = data.iloc[:, 12:17].values
y = data.iloc[:, 0].values


imputer = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
imputer = imputer.fit(X[:,0:5])
X[:, 0:5] = imputer.transform(X[:,0:5])



clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['Estado Civil','Edad','Nivel edu'],  
                     class_names=["Mujer","Hombre"],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("RangoEdu") 


dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['Sexo','Estado Civil','Zona'],  
                     class_names=["Alfabetizado","No alfabetizado"],  
                     filled=True, rounded=True,  
                     special_characters=True)

graph = graphviz.Source(dot_data)  
graph.render("RangoAlfabetizados") 
