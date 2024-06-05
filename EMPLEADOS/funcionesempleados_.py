from funcioneslistas import *
from random import randint, choice
from data_empleados import *
def calcular_promedio (a:int, b:int):
    promedio = (a + b) / 2
    return promedio

def mostrar_empleado(un_empleado:dict):
    print(f'  {un_empleado["legajo"]^1}     {un_empleado["nombre"]:^12}{un_empleado["apellido"]}{un_empleado["genero"]:^16}{un_empleado["calle"]:^16}{un_empleado["localidad"]:^16}   {un_empleado["provincia"]:^5} {un_empleado["email"]}') 

def mostrar_empleados(empleados):
    print("                             ***Lista de alumnos***")
    print("  Legajo       Nombre  apellido    Genero    Edad   Calle   Localidad     Provincia    Email")
    print("------------------------------------------------------------------------------------")
    cant = len(empleados)
    for i in range(cant):
        mostrar_empleado(empleados[i])
    print()

def cargar_datos_en_lista(lista_destino:list, lista_origen): #NOMBRE Y GENERO
        lista_destino.append(lista_origen)


def cargar_notas_lista (lista:list): #NOTAS 
    cargar_lista_random(lista,1,1,10) #al reutilizar una funcion dentro de otra funcion, cuando hay parametros que no coinciden solo poner valores en vez de poner parametros.
    


def promediar_lista(lista_promedios:list): #PROMEDIO
        lista_promedios.append(calcular_promedio(lista_promedios[-1], lista_promedios[-2]))

def cargar_legajos_en_lista(lista:list): #LEGAJOS
    cargar_lista_random(lista,1,20000,30000)

def cargar_empleados(lista:list, cantidad:int):
        legajo_inicial = 20000
        next_legajo = legajo_inicial
        for i in range(cantidad):
            legajo = next_legajo
            next_legajo += 1

            genero = choice(['f','m'])
            if genero == "m":
                nombre = choice(nombres_m)
            else:
                nombre = choice(nombres_f)
            
            apellido = choice(apellidos)
            edad = randint(18,70)
            calle = f"calle: {randint(100,500)} nro: {randint(1000,3000)}"
            localidad = choice(localidades)
            provincia = choice(provincias)
            sector = choice(sectores)
            email = f"{nombre.lower()}{apellido.lower()} + {choice(dominios)}"
            lista.append(new_empleado(legajo,nombre,apellido,genero,edad,calle,localidad,provincia,email,sector))

    

def ordenamiento_alumnos_doble_criterio(alumnos:list):
    tam = len(alumnos)
    for i in range(tam - 1): 
        for j in range(i + 1, tam):
            if alumnos[i] [GENERO] == alumnos[j][GENERO]:
                if alumnos[i] [LEGAJO] > alumnos[j][LEGAJO]:
                    swap_lista(alumnos,i,j)


            elif alumnos[i] [GENERO] > alumnos[j][GENERO]:
                swap_lista(alumnos,i,j)

def new_empleado(legajo,nombre,apellido,genero,edad,email,calle,localidad,provincia,sector):
    nuevo_empleado = {}
    nuevo_empleado["legajo"] = legajo
    nuevo_empleado["nombre"] = nombre
    nuevo_empleado["apellido"] = apellido
    nuevo_empleado["genero"] = genero
    nuevo_empleado["edad"] = edad
    nuevo_empleado["email"] = email
    nuevo_empleado["calle"] = calle
    nuevo_empleado["localidad"] = localidad
    nuevo_empleado["provincia"] = provincia
    nuevo_empleado["sector"] = sector
    return nuevo_empleado

def definir_campo(campo):
    match campo:
        case "l":
            retorno = "legajo"
        case "n":
            retorno = "nombre"
        case "g":
            retorno = "genero"
        case "p":
            retorno = "promedio"

def ordenar_empleados(lista,campo,asc:bool = True):
    atributo = definir_campo
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][atributo] > lista[j][atributo] if asc else lista[i][atributo] < lista[j][atributo]:
                swap_lista(lista,i,j)