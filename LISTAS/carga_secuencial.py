#Carga secuencial







#Carga aleatoria

mi_lista = [-1] * 5

bandera_seguir = True

while bandera_seguir == True:
    posicion = int (input ("Ingrese posición: "))
    while posicion < 1 or posicion > len(mi_lista):
        posicion = int (input ("Error, reingrese posición: "))

    numero = int (input ("Ingrese un número: "))

    mi_lista[posicion + 1] = numero

    seguir = input("Desea continuar? si/no: ")
    if seguir != "si":
        bandera_seguir = False

for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print (f"{i + 1} -> {mi_lista[i]}")