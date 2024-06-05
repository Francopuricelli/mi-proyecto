from funciones2 import *
un_alumno = {
    "legajo" : 23343,
    "nombre" : "franco",
    "genero" : "masculino",
    "notaP1" : 8,
    "notaP2" : 7,
    "direccion" : {"calle" : "Belgrano 200", "localidad" : "Avellaneda", "provincia" : "BsAs"} 
}

otro_alumno = {
    "legajo" : 32423,
    "nombre" : "maxi",
    "genero" : "masculino",
    "notaP1" : 4,
    "notaP2" : 10,
    "direccion" : {"calle" : "Frias 5000", "localidad" : "San Jose", "provincia" : "BsAs"} 
}
'''
print(otro_alumno.popitem()) #remueve el ultimo item de un diccionario,lista.
print(otro_alumno)



alumnos = []
alumnos.append(un_alumno)
alumnos.append(otro_alumno)

for alumno in alumnos:
    print(alumno.get("direccion"))
'''

'''
persona = {"nombre" : "mario",}
print(persona)

persona["edad"] = 20
print(persona)


persona["nombre"] = "franco"
print(persona)

print(persona.get("localidad"))



for e in persona.keys():
    print(e)

for e in persona.values():
    print(e)


for e in persona.items():
    print(e)
'''
TAM = 3
lista_alumnos = []

#otra manera de lista paralela

for _ in range(TAM):
    nuevo_alumno = []
    legajo = int(input("ingrese legajo "))
    nuevo_alumno.append(legajo)

    nombre = input("ingrese nombre ")
    nuevo_alumno.append(nombre)

    genero= input("ingrese genero ")
    nuevo_alumno.append(genero)

    notap1= int(input("ingrese nota del primer parcial "))
    nuevo_alumno.append(notap1)

    notap2= int(input("ingrese nota del segundo parcial "))
    nuevo_alumno.append(notap2)

    nuevo_alumno.append(calcular_promedio(notap1, notap2)) #el -1 representa el ultimo elemento de la lista


    lista_alumnos.append(nuevo_alumno)

#cargar_alumnos(listaa, 5)





mostrar_alumnos(lista_alumnos)
ordenamiento_alumnos_doble_criterio(lista_alumnos)
mostrar_alumnos(lista_alumnos)
