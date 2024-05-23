from Listasfunciones import *
from datos import *

LEGAJO = 0
NOMBRE = 1
GENERO = 2
NOTAP1 = 3
NOTAP2 = 4
PROMEDIO = 5

def calcular_promedio (a:int, b:int):
    promedio = (a + b) / 2
    return promedio

def mostrar_alumno(un_alumno:list):
    print(f"  {un_alumno[LEGAJO]^1}     {un_alumno[NOMBRE]:^12}{un_alumno[GENERO]:^16}{un_alumno[NOTAP1]:^16}{un_alumno[NOTAP2]:^16}   {un_alumno[PROMEDIO]:^5} ") 

def mostrar_alumnos(alumnos):
    print("                             ***Lista de alumnos***")
    print("  Legajo       Nombre      Genero          NotaP1          NotaP2          Promedio")
    print("------------------------------------------------------------------------------------")
    cant = len(alumnos)
    for i in range(cant):
        mostrar_alumno(alumnos[i])
    print()

def cargar_datos_en_lista(lista_destino:list, lista_origen): #NOMBRE Y GENERO
        lista_destino.append(lista_origen)


def cargar_notas_lista (lista:list): #NOTAS 
    cargar_lista_random(lista,1,1,10) #al reutilizar una funcion dentro de otra funcion, cuando hay parametros que no coinciden solo poner valores en vez de poner parametros.
    
def promediar_lista(lista_promedios:list): #PROMEDIO
        lista_promedios.append(calcular_promedio(lista_promedios[-1], lista_promedios[-2]))

def cargar_legajos_en_lista(lista:list): #LEGAJOS
    cargar_lista_random(lista,1,20000,30000)

def cargar_alumnos(alumnos:list, cantidad:int):
    if isinstance(alumnos,list):
        for i in range(cantidad):
            j = randint(0, 25)
            alumnos.append([])
            cargar_legajos_en_lista(alumnos[i])
            cargar_datos_en_lista(alumnos[i], nombres1[j])
            cargar_datos_en_lista(alumnos[i], generos1[j])
            cargar_notas_lista(alumnos[i])
            cargar_notas_lista(alumnos[i])
            promediar_lista(alumnos[i])
    
    

def ordenamiento_nombre(alumnos):
    tam = len(alumnos)
    for i in range(tam - 1): 
        for j in range(i + 1, tam):
            if alumnos[i] > alumnos[j]:
                swap_lista(alumnos,i,j)
                swap_lista(alumnos,i,j)
                swap_lista(alumnos,i,j)
                swap_lista(alumnos,i,j)
                swap_lista(alumnos,i,j)
                swap_lista(alumnos,i,j)
