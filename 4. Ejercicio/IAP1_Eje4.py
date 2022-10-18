# -*- coding: utf-8 -*-
from kanren import Relation, facts, run, var

padre = Relation()
facts(padre,
      ("Sebastian","Vicky"),
      ("Sebastian","Aurora"),
      ("Sebastian","Lucia"),
      ("Sebastian","Leonor"),
      ("Sebastian","Francisco"),
      ("Rene","Estefani"),
      ("Rene","Rodrigo"),
      ("Abel","Noemi"),
      ("Abel","Nestor"),
      ("Abel","Natali"),
      ("Gregorio","Saul"),
      ("Gonzalo","Alison"),
      ("Gonzalo","Kevin"),
      ("Francisco","Gustavo"))
madre = Relation()
facts(madre,
      ("Felipa","Vicky"),
      ("Felipa","Aurora"),
      ("Felipa","Lucia"),
      ("Felipa","Leonor"),
      ("Felipa","Francisco"),
      ("Vicky","Estefani"),
      ("Vicky","Rodrigo"),
      ("Aurora","Noemi"),
      ("Aurora","Nestor"),
      ("Aurora","Natali"),
      ("Lucia","Saul"),
      ("Leonor","Alison"),
      ("Leonor","Kevin"),
      ("Nela","Gustavo"))

#Abuelos, tios, padres, primos e hijos de su familia.

#RELACION DE ABUELOS
x = var()
y = var()
z = var()
w = var()
print("El abuelo paterno de Gustavo:", run(1,x,padre(x,y),padre(y,'Gustavo')))
print("El abuelo materno de Noemi:", run(1,x,padre(x,y),madre(y,'Noemi')))
print("La abuela paterna de Gustavo:", run(1,x,madre(x,y),padre(y,'Gustavo')))
print("La abuela materna de Noemi:", run(1,x,madre(x,y),madre(y,'Noemi')))

#RELACION DE TIOS
#Tios paternos
i = ""
tiosP = run(5,y,padre(x,y),madre(w,y),padre(x,z),madre(w,z),padre(z,"Gustavo"))
print("Los tios paternos de Gustavo: ")
for i in tiosP:
    if i != run(1,x,padre(x,"Gustavo"))[0]:
        esposo = run(1,x,padre(x,y),madre(i,y))
        esposa = run(1,x,madre(x,y),padre(i,y))
        if(len(esposo) != 0):
            print(i, esposo[0])
        else:
            print(i, esposa[0])

        
#Tios maternos
tiosP = run(5,y,padre(x,y),madre(w,y),padre(x,z),madre(w,z),madre(z,"Noemi"))
print("Los tios maternos de Noemi: ")
for i in tiosP:
    if i != run(1,x,madre(x,"Noemi"))[0]:
        esposo = run(1,x,padre(x,y),madre(i,y))
        esposa = run(1,x,madre(x,y),padre(i,y))
        if(len(esposo) != 0):
            print(i, esposo[0])
        else:
            print(i, esposa[0])
            

#Padres
print("Madre de Noemi: ",run(1,x,madre(x,"Noemi")))
print("Padre de Noemi: ",run(1,x,padre(x,"Noemi")))


#Primos
tiosP = run(5,y,padre(x,y),madre(w,y),padre(x,z),madre(w,z),madre(z,"Noemi"))
print("Los Primos maternos de Noemi: ")
for i in tiosP:
    if i != run(1,x,madre(x,"Noemi"))[0]:
        esposo = run(1,x,padre(x,y),madre(i,y))
        esposa = run(1,x,madre(x,y),padre(i,y))
        if(len(esposo) != 0):
            primos = run(10,x,madre(i,x),padre(esposo[0],x))
        else:
            primos = run(10,x,padre(i,x),madre(esposa[0],x))
        print(primos)
      
tiosP = run(5,y,padre(x,y),madre(w,y),padre(x,z),madre(w,z),padre(z,"Gustavo"))
print("Los Primos paternos de Gustavo")
for i in tiosP:
    if i != run(1,x,padre(x,"Gustavo"))[0]:
        esposo = run(1,x,padre(x,y),madre(i,y))
        esposa = run(1,x,madre(x,y),padre(i,y))
        if(len(esposo) != 0):
            primos = run(10,x,madre(i,x),padre(esposo[0],x))
        else:
            primos = run(10,x,padre(i,x),madre(esposa[0],x))
        print(primos)
        

#Hijos
print("Los hijos de Abel: ",run(5,x,padre("Abel",x)))
print("Los hijos de Aurora: ",run(5,x,madre("Aurora",x)))