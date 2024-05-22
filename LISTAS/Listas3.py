from LISTAS.Listasfunciones import *


listaa = []
cargar_lista_random(listaa,10,1,45)




total = totalizar_lista(listaa)
promedio = promediar_lista(listaa)
mayor = calcular_mayor(listaa)
menor = calcular_menor(listaa)
entero = entero(listaa,5)
buscar = buscar_lista(listaa,10)
sorteador(["martinez", "puricelli", "guevara", "pajez","puricelli","gonzalez","Baus","Martinez"])


print(listaa)


print(f"el total es {total}")
print(f"el promedio es {promedio}")
print(f"el mayor de la lista es {mayor}")
print(f"el menor de la lista es: {menor}")
print(entero)
print(buscar)
print(sorteador)




