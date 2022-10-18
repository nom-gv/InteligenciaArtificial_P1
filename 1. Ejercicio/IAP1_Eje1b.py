
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona.csv', sep=';', encoding='latin-1')

data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
data

#Importar Librerias para realizar el Ejercicio
import pandas as pd
import numpy as np

#CALCULO DEL PRIMER CUARTIL DE LOS DATOS
print("\n\nCALCULO DEL PRIMER CUARTIL DE TODAS LAS COLUMNAS\n")

Q1 = data['Zona'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas se encuentra en una zona urbana
print("Calculo del primer cuartil de zona:",Q1)

Q1 = data['Sexo'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas es hombre
print("Calculo del primer cuartil de sexo:",Q1)

Q1 = data['Edad'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas se encuentra entre las edades de 0 a 14
print("Calculo del primer cuartil de edad:",Q1)

Q1 = data['Relacion'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas son el jefe/a del hogar 
print("Calculo del primer cuartil de relacion:",Q1)

Q1 = data['Estado Civil'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas son solteros/as
print("Calculo del primer cuartil de estado civil:",Q1)

Q1 = data['Lugar 5 años'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas vivian en el mismo lugar hace 5 años
print("Calculo del primer cuartil de lugar de residencia hace 5 años:",Q1)

Q1 = data['Pueblo'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas pertenecen a un pueblo indigena originario campesino o afro boliviano
print("Calculo del primer cuartil de pertenencia a un pueblo:",Q1)

Q1 = data['Seguro Salud'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas esta registrado/a al sistema único de salud
print("Calculo del primer cuartil de seguro salud:",Q1)

Q1 = data['Embarazo'].quantile(.25)
#Obtenemos que hasta el 25% de personas no corresponden a esta seccion (por ser hombre)
print("Calculo del primer cuartil de embarazos:",Q1)

Q1 = data['Leer y Escribir'].quantile(.25)
#Obtenemos que personas que no corresponden por ser muy pequeños y personas que saben leer y escribir conforman hasta el 25% 
print("Calculo del primer cuartil de alfabetifados:",Q1)

Q1 = data['Sum y Mul'].quantile(.25)
#Obtenemos que personas que no corresponden por ser muy pequeños y personas que saben sumar y multiplicar conforman hasta el 25% 
print("Calculo del primer cuartil de conocimiento en operaciones basicas:",Q1)

Q1 = data['Nivel edu'].quantile(.25)
#Obtenemos que hasta el 25% de personas se encuentran entre los siguientes niveles de educacion: no corresponde, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, y del sistema escolar antiguo el nivel basico o intermedio
print("Calculo del primer cuartil de nivel maximo de educacion:",Q1)

Q1 = data['Matricula'].quantile(.25)
#Obtenemos que personas que no corresponden por ser muy pequeños y personas que se encuentran matriculadas en algun curso conforman hasta el 25% 
print("Calculo del primer cuartil de matriculacion a algun curso:",Q1)

Q1 = data['Prox Nivel ed'].quantile(.25)
#Obtenemos que hasta el 25% de personas encuestadas no dio el curso a incribirse o matricularse este año
print("Calculo del primer cuartil de proximo nivel de educacion:",Q1)

Q1 = data['Ocupacion'].quantile(.25)
#Obtenermos que hasta el 25% de personas encuestadas no corresponden a ninguna ocupacion
print("Calculo del primer cuartil de ocupacion actual:",Q1)


#CALCULO DEL PERCENTIL 90 Y 95 DE LOS DATOS
print("\n\nCALCULO DEL PERCENTIL 90 y 95 DE TODAS LAS COLUMNAS\n")

Q90 = data['Zona'].quantile(.90)
Q95 = data['Zona'].quantile(.95)
#Obtenemos que el 90% y 95% de personas pertenecen a zonas urbanas y rurales
print("Calculo del Percentil 90 y 95 de zona:", Q90, Q95)

Q90 = data['Sexo'].quantile(.90)
Q95 = data['Sexo'].quantile(.95)
#Obtenemos que el 90% y 95% de personas se encuentran entre sexo femenino y masculino
print("Calculo del Percentil 90 y 95 de sexo:", Q90, Q95)

Q90 = data['Edad'].quantile(.90)
Q95 = data['Edad'].quantile(.95)
#Obtenemos que el 90% se encuentra entre 0 y 61 años, y que el 95% se encuentra entre 0 y 69 años
print("Calculo del Percentil 90 y 95 de edad:", Q90, Q95)

Q90 = data['Relacion'].quantile(.90)
Q95 = data['Relacion'].quantile(.95)
#Obtenemos que hasta el 90% de personas se encuentra entre las siguientes relaciones: Jefe/a del hogar, Esposa/o o convivente, Hijo/a o entenado/a
#Tambien obtenemos que hasta el 95% de personas se encuentra entre las siguientes relaciones: Jefe/a del hogar, Esposa/o o convivente, Hijo/a o entenado/a, Hijo/a adoptado, Yerno o nuera, Hermano/a o cuñado/a
print("Calculo del Percentil 90 y 95 de relacion:", Q90, Q95)

Q90 = data['Estado Civil'].quantile(.90)
Q95 = data['Estado Civil'].quantile(.95)
#Obtenemos que hasta el 90% de personas se encuentra Soltero/a, Casado/a o es Conviviente o concubino/a
#Tambien obtenemos que hasta el 95% de personas se encuentra Soltero/a, Casado/a, es conviviente o concubino/a, es separado/a o divorciado/a
print("Calculo del Percentil 90 y 95 de estado civil:", Q90, Q95)

Q90 = data['Lugar 5 años'].quantile(.90)
Q95 = data['Lugar 5 años'].quantile(.95)
#Obtenemos que hasta el 90% de personas vivia en el mismo lugar y en otro lugar del pais
#Tambien obtenemos que hasta el 95% de personas vivia en el mismo lugar, en otro lugar del pais, en el exterior o aun no habia nacido
print("Calculo del Percentil 90 y 95 de lugar de residencia hace 5 años:", Q90, Q95)

Q90 = data['Pueblo'].quantile(.90)
Q95 = data['Pueblo'].quantile(.95)
#Obtenemos que hasta el 90% de personas pertenece o no a un pueblo indigena originario campesion o afro americano
#Tambien obtenemos que hasta el 95% de personas pertenece o no a un pueblo indigena originario campesion o afro americano
print("Calculo del Percentil 90 y 95 de pertenencia a un pueblo:", Q90, Q95)

Q90 = data['Seguro Salud'].quantile(.90)
Q95 = data['Seguro Salud'].quantile(.95)
#Obtenemos que hasta el 90% de personas puede estar registrada en alguno seguro de salud o no puede estarlo
#Obtenemos que hasta el 95% de personas puede estar registrada en alguno seguro de salud o no puede estarlo
print("Calculo del Percentil 90 y 95 de seguro salud:", Q90, Q95)

Q90 = data['Embarazo'].quantile(.90)
Q95 = data['Embarazo'].quantile(.95)
#Obtenemos que hasta el 90% de personas no pertenece a esta columna por su genero, o si esta o puedo estar embarazada o no se encuentra embarazada
#Obtenemos que hasta el 95% de personas no pertenece a esta columna por su genero, o si esta o puedo estar embarazada o no se encuentra embarazada
print("Calculo del Percentil 90 y 95 de embarazos:", Q90, Q95)

Q90 = data['Leer y Escribir'].quantile(.90)
Q95 = data['Leer y Escribir'].quantile(.95)
#Obtenemos que hasta el 90% de personas no pertenece por la edad o puede leer y escribir
#Obtenemos que hasta el 95% de personas no pertenece por la edad, puede leer y escribir; y no puede leer y escribir
print("Calculo del Percentil 90 y 95 de alfabetifados:", Q90, Q95)

Q90 = data['Sum y Mul'].quantile(.90)
Q95 = data['Sum y Mul'].quantile(.95)
#Obtenemos que hasta el 90% de personas no pertenece por la edad o puede sumar y multiplicar
#Obtenemos que hasta el 95% de personas no pertenece por la edad, puede sumar y multiplicar; y no puede sumar y multiplicar
print("Calculo del Percentil 90 y 95 de conocimiento en operaciones basicas:", Q90, Q95)

Q90 = data['Nivel edu'].quantile(.90)
Q95 = data['Nivel edu'].quantile(.95)
#Obtenemos que hasta el 90% de personas se encuentra entre los siguientes niveles de educacion: No corresponde por la edad, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, Del sistema antiguo: basico, intermedio y medio, 
#del sistema escolar actual: primaria y secundaria, de educacion de adultos: educacion basica de adultos y centro de educacion medio de adultos, de educacion alternativa y especial: educacion juvenil alternativa, educacion primaria de adultos, 
#educacion secundaria de adultos, programacion nacioal post albatizacion, educacion especial, de educacion superios: normal, univesidad

#Obtenemos que hasta el 95% de personas se encuentra entre los siguientes niveles de educacion: No corresponde por la edad, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, Del sistema antiguo: basico, intermedio y medio, 
#del sistema escolar actual: primaria y secundaria, de educacion de adultos: educacion basica de adultos y centro de educacion medio de adultos, de educacion alternativa y especial: educacion juvenil alternativa, educacion primaria de adultos, 
#educacion secundaria de adultos, programacion nacioal post albatizacion, educacion especial, de educacion superios: normal, univesidad, postgrado diplomado, postgrado maestria, postgrado doctorado, tecnico de universidad
print("Calculo del Percentil 90 y 95 de nivel maximo de educacion:", Q90, Q95)

Q90 = data['Matricula'].quantile(.90)
Q95 = data['Matricula'].quantile(.95)
#Obtenemos que hasta el 90% de personas o no le corresponde una matriculacion, o si se incribio o matriculo a un curso o no lo hizo
#Obtenemos que hasta el 95% de personas o no le corresponde una matriculacion, o si se incribio o matriculo a un curso o no lo hizo 
print("Calculo del Percentil 90 y 95 de matriculacion a algun curso:", Q90, Q95)

Q90 = data['Prox Nivel ed'].quantile(.90)
Q95 = data['Prox Nivel ed'].quantile(.95)
#Obtenemos que hasta el 90% de personas se encontrara entre los siguientes niveles de educacion: No corresponde por la edad, curso de alfabeticacion, del sistema escolar actual: educacion inicial o pre-escolar, primaria, secundaria, 
#de EDUCACION ALTERNATIVA Y ESPECIAL: educacion primaria de adultos

#Obtenemos que hasta el 95% de personas se encontrara entre los siguientes niveles de educacion: No corresponde por la edad, curso de alfabeticacion, del sistema escolar actual: educacion inicial o pre-escolar, primaria, secundaria, 
#de EDUCACION ALTERNATIVA Y ESPECIAL: educacion primaria de adultos, Educacion secundaria de adultos, programa nacional de post alfabetizacion, educacion especial; DE EDUCACION SUPERIOR: Normal o universidad
print("Calculo del Percentil 90 y 95 de proximo nivel de educacion:", Q90, Q95)

Q90 = data['Ocupacion'].quantile(.90)
Q95 = data['Ocupacion'].quantile(.95)
#Obtenemos que hasta el 90% de personas tiene las siguiente ocupaciones: No corresponde por la edad, Obrero/Empleado, Empleador/a socio que si recibe salario, Trabajador/a por cuenta propia
#Obtenemos que hasta el 95% de personas tiene las siguiente ocupaciones: No corresponde por la edad, Obrero/Empleado, Empleador/a socio que si recibe salario, Trabajador/a por cuenta propia, Empleador/a o socio/a que no recibe salario, 
#Cooperativista de produccion, Trabajador/a familiar sin remuneracion
print("Calculo del Percentil 90 y 95 de ocupacion actual:", Q90, Q95)