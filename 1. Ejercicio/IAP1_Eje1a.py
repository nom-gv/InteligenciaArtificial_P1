
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetPersona/main/Dataset_persona.csv', sep=';', encoding='latin-1')

data = pd.DataFrame(data, columns=['Zona','Sexo','Edad','Relacion','Estado Civil','Lugar 5 años','Pueblo','Seguro Salud','Embarazo','Leer y Escribir','Sum y Mul','Nivel edu','Matricula','Prox Nivel ed','Ocupacion'])
data

#FUNCIONES PARA REALIZAR EL EJERCICIO
#Para obtener los cuartiles
def cuartil(c, qn):
    valores = pd.to_numeric(data[c],errors='coerce').to_list()
    val = [x for x in valores if True]
    val.sort()
    
    cv = len(val)
    if cv%2 == 0:
        q = (int((qn*cv)/4))
        if qn == 2:
            Q1 = (val[q-1] + val[q])/2
        elif (cv/2)%2 == 0:
            Q1 = (val[q-1] + val[q])/2
        else:
            Q1 = float(val[q])
    else:
        q = (int((qn*(cv+1))/4))-1
        if qn != 2 and (int(cv/2))%2 == 0:
            Q1 = (val[q] + val[q+1])/2
        else:
            Q1 = float(val[q])
 
    return Q1

#Para Percentiles
def percentil(columna,nc):
    valores = pd.to_numeric(data[columna],errors='coerce').to_list()
    val = [x for x in valores if True]
    val.sort()
    
    #Posicion del percentil
    P1 = int((nc*len(val))/100)
    
    if(len(val)%2 == 0):
        Q1 = (val[P1] + val[P1+1])/2
    else:
        Q1 = float(val[P1])
    return Q1


#CALCULO DEL PRIMER CUARTIL DE LOS DATOS
print("\n\nCALCULO DEL PRIMER CUARTIL DE TODAS LAS COLUMNAS\n")

#Obtenemos que hasta el 25% de personas encuestadas se encuentra en una zona urbana
print("Calculo del primer cuartil de zona:",cuartil('Zona',1))

#Obtenemos que hasta el 25% de personas encuestadas es hombre
print("Calculo del primer cuartil de sexo:",cuartil('Sexo',1))

#Obtenemos que hasta el 25% de personas encuestadas se encuentra entre las edades de 0 a 14
print("Calculo del primer cuartil de edad:",cuartil('Edad',1))

#Obtenemos que hasta el 25% de personas encuestadas son el jefe/a del hogar 
print("Calculo del primer cuartil de relacion:",cuartil('Relacion',1))

#Obtenemos que hasta el 25% de personas encuestadas son solteros/as
print("Calculo del primer cuartil de estado civil:",cuartil('Estado Civil',1))

#Obtenemos que hasta el 25% de personas encuestadas vivian en el mismo lugar hace 5 años
print("Calculo del primer cuartil de lugar de residencia hace 5 años:",cuartil('Lugar 5 años',1))

#Obtenemos que hasta el 25% de personas encuestadas pertenecen a un pueblo indigena originario campesino o afro boliviano
print("Calculo del primer cuartil de pertenencia a un pueblo:",cuartil('Pueblo',1))

#Obtenemos que hasta el 25% de personas encuestadas esta registrado/a al sistema único de salud
print("Calculo del primer cuartil de seguro salud:",cuartil('Seguro Salud',1))

#Obtenemos que hasta el 25% de personas no corresponden a esta seccion (por ser hombre)
print("Calculo del primer cuartil de embarazos:",cuartil('Embarazo',1))

#Obtenemos que personas que no corresponden por ser muy pequeños y personas que saben leer y escribir conforman hasta el 25% 
print("Calculo del primer cuartil de alfabetifados:",cuartil('Leer y Escribir',1))

#Obtenemos que personas que no corresponden por ser muy pequeños y personas que saben sumar y multiplicar conforman hasta el 25% 
print("Calculo del primer cuartil de conocimiento en operaciones basicas:",cuartil('Sum y Mul',1))

#Obtenemos que hasta el 25% de personas se encuentran entre los siguientes niveles de educacion: no corresponde, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, y del sistema escolar antiguo el nivel basico o intermedio
print("Calculo del primer cuartil de nivel maximo de educacion:",cuartil('Nivel edu',1))

#Obtenemos que personas que no corresponden por ser muy pequeños y personas que se encuentran matriculadas en algun curso conforman hasta el 25% 
print("Calculo del primer cuartil de matriculacion a algun curso:",cuartil('Matricula',1))

#Obtenemos que hasta el 25% de personas encuestadas no dio el curso a incribirse o matricularse este año
print("Calculo del primer cuartil de proximo nivel de educacion:",cuartil('Prox Nivel ed',1))

#Obtenermos que hasta el 25% de personas encuestadas no corresponden a ninguna ocupacion
print("Calculo del primer cuartil de ocupacion actual:",cuartil('Ocupacion',1))


#CALCULO DEL PERCENTIL 90 Y 95 DE LOS DATOS
print("\n\nCALCULO DEL PERCENTIL 90 y 95 DE TODAS LAS COLUMNAS\n")

#Obtenemos que el 90% y 95% de personas pertenecen a zonas urbanas y rurales
print("Calculo del Percentil 90 y 95 de zona:", percentil('Zona',90), percentil('Zona', 95))

#Obtenemos que el 90% y 95% de personas se encuentran entre sexo femenino y masculino
print("Calculo del Percentil 90 y 95 de sexo:", percentil('Sexo',90), percentil('Sexo', 95))

#Obtenemos que el 90% se encuentra entre 0 y 61 años, y que el 95% se encuentra entre 0 y 69 años
print("Calculo del Percentil 90 y 95 de edad:", percentil('Edad',90), percentil('Edad', 95))

#Obtenemos que hasta el 90% de personas se encuentra entre las siguientes relaciones: Jefe/a del hogar, Esposa/o o convivente, Hijo/a o entenado/a
#Tambien obtenemos que hasta el 95% de personas se encuentra entre las siguientes relaciones: Jefe/a del hogar, Esposa/o o convivente, Hijo/a o entenado/a, Hijo/a adoptado, Yerno o nuera, Hermano/a o cuñado/a
print("Calculo del Percentil 90 y 95 de relacion:", percentil('Relacion',90), percentil('Relacion', 95))

#Obtenemos que hasta el 90% de personas se encuentra Soltero/a, Casado/a o es Conviviente o concubino/a
#Tambien obtenemos que hasta el 95% de personas se encuentra Soltero/a, Casado/a, es conviviente o concubino/a, es separado/a o divorciado/a
print("Calculo del Percentil 90 y 95 de estado civil:", percentil('Estado Civil',90), percentil('Estado Civil', 95))

#Obtenemos que hasta el 90% de personas vivia en el mismo lugar y en otro lugar del pais
#Tambien obtenemos que hasta el 95% de personas vivia en el mismo lugar, en otro lugar del pais, en el exterior o aun no habia nacido
print("Calculo del Percentil 90 y 95 de lugar de residencia hace 5 años:", percentil('Lugar 5 años',90), percentil('Lugar 5 años', 95))

#Obtenemos que hasta el 90% de personas pertenece o no a un pueblo indigena originario campesion o afro americano
#Tambien obtenemos que hasta el 95% de personas pertenece o no a un pueblo indigena originario campesion o afro americano
print("Calculo del Percentil 90 y 95 de pertenencia a un pueblo:", percentil('Pueblo',90), percentil('Pueblo', 95))

#Obtenemos que hasta el 90% de personas puede estar registrada en alguno seguro de salud o no puede estarlo
#Obtenemos que hasta el 95% de personas puede estar registrada en alguno seguro de salud o no puede estarlo
print("Calculo del Percentil 90 y 95 de seguro salud:", percentil('Seguro Salud',90), percentil('Seguro Salud', 95))

#Obtenemos que hasta el 90% de personas no pertenece a esta columna por su genero, o si esta o puedo estar embarazada o no se encuentra embarazada
#Obtenemos que hasta el 95% de personas no pertenece a esta columna por su genero, o si esta o puedo estar embarazada o no se encuentra embarazada
print("Calculo del Percentil 90 y 95 de embarazos:", percentil('Embarazo',90), percentil('Embarazo', 95))

#Obtenemos que hasta el 90% de personas no pertenece por la edad o puede leer y escribir
#Obtenemos que hasta el 95% de personas no pertenece por la edad, puede leer y escribir; y no puede leer y escribir
print("Calculo del Percentil 90 y 95 de alfabetifados:", percentil('Leer y Escribir',90), percentil('Leer y Escribir', 95))

#Obtenemos que hasta el 90% de personas no pertenece por la edad o puede sumar y multiplicar
#Obtenemos que hasta el 95% de personas no pertenece por la edad, puede sumar y multiplicar; y no puede sumar y multiplicar
print("Calculo del Percentil 90 y 95 de conocimiento en operaciones basicas:", percentil('Sum y Mul',90), percentil('Sum y Mul', 95))

#Obtenemos que hasta el 90% de personas se encuentra entre los siguientes niveles de educacion: No corresponde por la edad, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, Del sistema antiguo: basico, intermedio y medio, 
#del sistema escolar actual: primaria y secundaria, de educacion de adultos: educacion basica de adultos y centro de educacion medio de adultos, de educacion alternativa y especial: educacion juvenil alternativa, educacion primaria de adultos, 
#educacion secundaria de adultos, programacion nacioal post albatizacion, educacion especial, de educacion superios: normal, univesidad

#Obtenemos que hasta el 95% de personas se encuentra entre los siguientes niveles de educacion: No corresponde por la edad, ninguno, curso alfabetizacion, educacion inicial o pre-escolar, Del sistema antiguo: basico, intermedio y medio, 
#del sistema escolar actual: primaria y secundaria, de educacion de adultos: educacion basica de adultos y centro de educacion medio de adultos, de educacion alternativa y especial: educacion juvenil alternativa, educacion primaria de adultos, 
#educacion secundaria de adultos, programacion nacioal post albatizacion, educacion especial, de educacion superios: normal, univesidad, postgrado diplomado, postgrado maestria, postgrado doctorado, tecnico de universidad
print("Calculo del Percentil 90 y 95 de nivel maximo de educacion:", percentil('Nivel edu',90), percentil('Nivel edu', 95))

#Obtenemos que hasta el 90% de personas o no le corresponde una matriculacion, o si se incribio o matriculo a un curso o no lo hizo
#Obtenemos que hasta el 95% de personas o no le corresponde una matriculacion, o si se incribio o matriculo a un curso o no lo hizo 
print("Calculo del Percentil 90 y 95 de matriculacion a algun curso:", percentil('Matricula',90), percentil('Matricula', 95))

#Obtenemos que hasta el 90% de personas se encontrara entre los siguientes niveles de educacion: No corresponde por la edad, curso de alfabeticacion, del sistema escolar actual: educacion inicial o pre-escolar, primaria, secundaria, 
#de EDUCACION ALTERNATIVA Y ESPECIAL: educacion primaria de adultos

#Obtenemos que hasta el 95% de personas se encontrara entre los siguientes niveles de educacion: No corresponde por la edad, curso de alfabeticacion, del sistema escolar actual: educacion inicial o pre-escolar, primaria, secundaria, 
#de EDUCACION ALTERNATIVA Y ESPECIAL: educacion primaria de adultos, Educacion secundaria de adultos, programa nacional de post alfabetizacion, educacion especial; DE EDUCACION SUPERIOR: Normal o universidad
print("Calculo del Percentil 90 y 95 de proximo nivel de educacion:", percentil('Prox Nivel ed',90), percentil('Prox Nivel ed', 95))

#Obtenemos que hasta el 90% de personas tiene las siguiente ocupaciones: No corresponde por la edad, Obrero/Empleado, Empleador/a socio que si recibe salario, Trabajador/a por cuenta propia
#Obtenemos que hasta el 95% de personas tiene las siguiente ocupaciones: No corresponde por la edad, Obrero/Empleado, Empleador/a socio que si recibe salario, Trabajador/a por cuenta propia, Empleador/a o socio/a que no recibe salario, 
#Cooperativista de produccion, Trabajador/a familiar sin remuneracion
print("Calculo del Percentil 90 y 95 de ocupacion actual:", percentil('Ocupacion',90), percentil('Ocupacion', 95))