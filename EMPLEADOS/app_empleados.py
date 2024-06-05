from funcionesempleados_ import *
from data_empleados import *
from funcioneslistas import *
from random import *
TAM = 10
lista_empleados = []

#otra manera de lista paralela
'''
for _ in range(TAM):
    nuevo_empleado = []
    legajo = int(input("ingrese legajo "))

    nombre = input("ingrese nombre ")

    apellido = input("ingrese apellido")

    genero= input("ingrese genero ")

    edad= int(input("ingrese edad"))

    calle = input("ingrese calle")

    localidad = input("ingrese localidad")

    provincia = input("ingrese provincia")

    email = input("ingrese email")

    sector= input("ingrese sector")


    lista_empleados.append(new_empleado(legajo,nombre,apellido,genero,edad,calle,localidad,provincia,email,sector))
'''
#cargar_alumnos(listaa, 5)



cargar_empleados(lista_empleados,TAM)

mostrar_empleados(lista_empleados)
