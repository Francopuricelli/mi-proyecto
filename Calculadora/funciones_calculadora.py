from os import system

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def operadores():
    print("1-sumar")
    print("2-restar")
    print("3-dividir")
    print("4-multiplicar")
    print("5-factorial")

def menu():
    print("        Calculadora")
    print("1-Ingresar primer valor ")
    print("2-Ingresar segundo valor ")
    print("3-Elegir operador ")
    print("4-Salir ")
    return  input("Ingrese opcion: ")

def salir():
    salir = input("desea salir? \n (si/no) ")
    return salir