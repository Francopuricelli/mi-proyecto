from Listasfunciones import *
from funcionesparalelas_ import *
'''
lista = crear_lista_random(20,1,100)
tam = len(lista)

mostrar_lista(lista)

for i in range(tam - 1):
    for j in range(i + 1, tam):
        if lista [i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista [j] = aux


print("------------------------")
print(lista)
'''
'''
lista = crear_lista_random(20,1,100)

print(lista)


print("-------------------------------------------------------")
print(ordenar_lista_ascendente(lista))
print(ordenar_lista_descendente(lista))
'''
'''
test = []
def ordenar_lista(lista:list):
    
    match menu():
        case "1":
            listaB = ordenar_lista_ascendente(lista) 
        case "2":
            listaB = ordenar_lista_descendente(lista)
    return listaB

lista = crear_lista_random(10,1,100)


cargar_legajos_en_lista(test,4)
print(test)
'''

valores = [
    [23,14,52,29],
    ["a","b","c","d"],
    ["python",[4,3,8,7]],
    [True, 3.14, "hola"]
    ]
    
print(valores[3][1])
print(valores[-1][1])
