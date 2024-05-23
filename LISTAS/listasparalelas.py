from funcionesparalelas_ import *
from datos import *
from Listasfunciones import *
from random import *
TAM = 3
lista_alumnos = []

#otra manera de lista paralela

for _ in range(TAM):
    nuevo_alumno = []
    legajo = int(input("ingrese legajo "))
    nuevo_alumno.append(legajo)

    nombre = input("ingrese nombre ")
    nuevo_alumno.append(nombre)

    genero= input("ingrese genero ")
    nuevo_alumno.append(genero)

    notap1= int(input("ingrese nota del primer parcial "))
    nuevo_alumno.append(notap1)

    notap2= int(input("ingrese nota del segundo parcial "))
    nuevo_alumno.append(notap2)

    nuevo_alumno.append(calcular_promedio(notap1, notap2)) #el -1 representa el ultimo elemento de la lista


    lista_alumnos.append(nuevo_alumno)

#cargar_alumnos(listaa, 5)




ordenamiento_nombre(lista_alumnos)
mostrar_alumnos(lista_alumnos)
