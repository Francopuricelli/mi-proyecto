from Calculadora.operaciones import *
from os import system
flag_1 = True
flag_2 = True




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

while True:
    match menu():
        case "1":
                if flag_1 == True:
                    num1 = int(input("ingrese primer numero"))
                    flag_1 = False
                else:
                    print("ya ingresaste el primer numero") 
        case "2":
                num2 = int(input("ingrese segundo numero:"))
                flag_2 = False
                if flag_1 == True:
                    print("ingrese primer numero porfavor")
        case "3":
            if flag_1 == True or flag_2 == True:
                print("debes ingresar un numero previamente")
                menu()
            else:
                operadores()
                operacion_a_realizar = input("ingrese un numero")
                if operacion_a_realizar == "1":
                    resultado = suma(num1,num2)
                elif operacion_a_realizar == "2":
                    resultado = resta(num1,num2)
                elif operacion_a_realizar == "3":
                    if num1 == 0 or num2 == 0:
                        raise ValueError("no se puede dividir por 0 intentelo nuevamente")
                    resultado = division(num1,num2)
                elif operacion_a_realizar == "4":
                    resultado = multiplicacion(num1,num2)
                elif operacion_a_realizar == "5":
                    resultado = factorial(num1)
                    resultado1 = factorial(num2)
                    print(f"el resultado del factorial 1 es {resultado} y el resultado del factorial 2 es {resultado1}")
                if operacion_a_realizar != "5":
                    print(f"el resultado de la operacion es {resultado} ")
        case "4":
            if salir() == "no":
                menu()
            else:
                break

    pausar()
        
print("fin del programa")
    



