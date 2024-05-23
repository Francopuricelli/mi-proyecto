from os import system

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def operadores():
    operador = print("1-sumar")
    operador = print("2-restar")
    operador = print("3-dividir")
    operador = print("4-multiplicar")
    operador = print("5-factorial")
    return operador

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