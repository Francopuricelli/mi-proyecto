from LISTAS.Listasfunciones import *

def buscar_par_listas(lista:list)->list:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("La lista esta vacia")
        lista_pares = []
        for x in lista:
            if (x % 2 == 0):
                lista_pares.append(x)
        return lista_pares
    raise ValueError("Eso no es una lista")


numeros =crear_lista_random(20, 1, 100)
pares = buscar_par_listas(numeros)
print(pares)



def listas_mayor_que_diez(lista):
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("La lista esta vacia")
        lista_10 = []
        for x in lista:
            if x > 10:
                lista_10.append(x)
        cant10 = len(lista_10)
        if cant10 == 0:
            return ("ningun numero ingresado es mayor a 10")
        return lista_10
    raise ValueError("Eso no es una lista")



lista = []
while True:
    num_ingresados = int(input("ingrese un numero "))
    if num_ingresados == -1:
        break
    lista.append(num_ingresados)

print(lista)
print(f"numeros mayor que 10: {listas_mayor_que_diez(lista)}")