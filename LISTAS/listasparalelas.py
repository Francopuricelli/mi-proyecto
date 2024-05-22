from funcionesparalelas_ import *
from datos import *
from Listasfunciones import *
from random import *

legajos = []
nombres = []
generos = []
notasp1 = []
notasp2 = []
promedios = []

#otra manera de lista paralela
'''  
for _ in range(TAM):
    aux = int(input("ingrese legajo "))
    legajos.append(aux)

    aux = input("ingrese nombre ")
    nombres.append(aux)

    aux = input("ingrese genero ")
    generos.append(aux)

    aux = int(input("ingrese nota del primer parcial "))
    notasp1.append(aux)

    aux = int(input("ingrese nota del segundo parcial "))
    notasp2.append(aux)

    promedios.append(calcular_promedio(notasp1[-1], notasp2[-1])) #el -1 representa el ultimo elemento de la lista
'''


cargar_alumnos(legajos, nombres ,generos , notasp1 , notasp2 , promedios , 15)
mostrar_alumnos(legajos, nombres ,generos , notasp1 , notasp2 , promedios)



ordenamiento_nombre(legajos, nombres ,generos , notasp1 , notasp2 , promedios,)
mostrar_alumnos(legajos, nombres ,generos , notasp1 , notasp2 , promedios)
