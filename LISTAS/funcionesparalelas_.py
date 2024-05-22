from Listasfunciones import *
from datos import *

def calcular_promedio (a:int, b:int):
    promedio = (a + b) / 2
    return promedio

def mostrar_alumnos(legajos:list, nombres:list, generos:list, notasp1:list, notasp2:list, promedios:list):
    print("                   ***Lista de alumnos***                  ")
    print("LEGAJO       NOMBRE      GENERO      NOTA1       NOTA2       PROMEDIO")
    print("------------------------------------------------------------------------------")
    for i in range(len(legajos)):
        print( f"{legajos[i]}        {nombres[i]:10}     {generos[i]}         {notasp1[i]:2}         {notasp2[i]:2}             {promedios[i]}")

def cargar_datos_en_lista(lista_destino:list, lista_origen, cant): #NOMBRE Y GENERO
    for i in range (cant):
        lista_destino.append(lista_origen[i])
        if cant > len(lista_origen):
            raise ValueError("la cantidad solicitada sobre pasa la cantidad de nombres en la lista.")


def cargar_notas_lista (lista:list,cant:int): #NOTAS 
    cargar_lista_random(lista,cant,1,10) #al reutilizar una funcion dentro de otra funcion, cuando hay parametros que no coinciden solo poner valores en vez de poner parametros.
    
def promediar_lista(lista_a:list,lista_b:list,lista_promedios:list): #PROMEDIO
    for i in range(len(lista_a)):
        promedio = (lista_a[i] + lista_b[i]) / 2
        lista_promedios.append(promedio)

def cargar_legajos_en_lista(lista:list,cant): #LEGAJOS
    cargar_lista_random(lista,cant,20000,30000)

def cargar_alumnos(legajos, nombres ,generos , notasp1 , notasp2 , promedios , cant)-> None: 
    cargar_datos_en_lista(nombres,nombres1,cant)
    cargar_legajos_en_lista(legajos,cant)
    cargar_datos_en_lista(generos,generos1,cant)
    cargar_notas_lista(notasp1,cant)
    cargar_notas_lista(notasp2,cant)
    promediar_lista(notasp1,notasp2,promedios)
    

def ordenamiento_nombre(legajos, nombres ,generos , notasp1 , notasp2 , promedios):
    tam = len(legajos)
    for i in range(tam - 1): 
        for j in range(i + 1, tam):
            if nombres[i] > nombres[j]:
                swap_lista(legajos,i,j)
                swap_lista(nombres,i,j)
                swap_lista(generos,i,j)
                swap_lista(notasp1,i,j)
                swap_lista(notasp2,i,j)
                swap_lista(promedios,i,j)
