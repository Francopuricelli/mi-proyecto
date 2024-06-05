from random import *

def menu():
    
    print("    ORDENAMIENTO LISTA")
    print("1- Ordenar lista de forma ascendente")
    print("2- Ordenar lista de forma descendente")
    return input("ingrese numero ")

def mostrar_lista(lista:list)->None:
    if isinstance(lista, list):
        for el in lista:
            print(el, end=" ")
        print()
    else:
        raise ValueError("Eso no es una lista")

def cargar_lista_random(lista:int, cant:int, desde:int, hasta:int):
    from random import randint
    for _ in range(cant):
        lista.append(randint(desde, hasta))  #para agregarle un valor a la lista (append).

def mostrar_lista(lista):
    print()

def crear_lista_random(cant:int, desde:int, hasta:int):
    from random import randint
    lista = []
    for _ in range(cant):
        lista.append(randint(desde, hasta))
    return lista

def totalizar_lista(lista):
    total = 0
    for i in lista:
        total += i
    
    return total

def promediar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total / i

def calcular_mayor(lista):
    if len(lista) == 0:
        raise ValueError("no esta definido el mayor de una lista vacia")
    flag_mayor = True
    for el in lista:
        if flag_mayor == True or el > num_mayor:
            num_mayor = el
            flag_mayor = False
    return num_mayor

def calcular_menor(lista):
    if len(lista) == 0:
        raise ValueError("no esta definido el mayor de una lista vacia")
    flag_menor = True
    for el in lista:
        if flag_menor == True or el < num_menor:
            num_menor = el
            flag_menor = False
    return num_menor

def entero(lista,target):
    for el in lista:
        if el == target:
            return True
        else:
            return False

def buscar_lista(lista:list,target:int):
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("es una lista vacia")
        indice = -1
        for i in range (len(lista)):
            if lista[i]== target:
                indice = i
                break
        return indice
    raise ValueError("no es una lista")

def contar_en_lista(lista:list,target:int): 

    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("es una lista vacia")
        contador = 0
        for el in lista:
            if el == target:
                contador += 1
        return contador
    raise ValueError("no es una lista")

def sorteador(lista:list):
    import time
    if not isinstance(lista,list):
        raise ValueError("no es una lista")
    time.sleep(1)
    i = randint(0,len(lista) - 1)
    print (f"the winner is ------- {lista[i]}")

def ordenar_lista_ascendente(lista:list):
    if isinstance(lista, list):
        tam = len(lista)
        if tam == 0:
            raise ValueError("la lista esta vacia")
        for i in range(tam - 1): 
            for j in range(i + 1, tam):
                if lista [i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista [j] = aux
        return lista
    raise ValueError("no es una lista")

def ordenar_lista_descendente(lista:list):
    if isinstance(lista, list):
        tam = len(lista)
        if tam == 0:
            raise ValueError("la lista esta vacia")
        for i in range(tam - 1): 
            for j in range(i + 1, tam):
                if lista [i] < lista[j]:
                    #lista[i], lista[j] = lista[j] , lista[i] manera de swapear mas facil.
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista [j] = aux
        return lista
    raise ValueError("no es una lista")

def swap_lista(lista:list,i:int,j:int):
    aux = lista[i]
    lista[i] = lista[j]
    lista [j] = aux


