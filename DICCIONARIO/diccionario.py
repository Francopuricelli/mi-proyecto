from funciones import *
from calculadora import *
lista_nombres = []
lista_edad = []

diccionario = {

"nombre" : lista_nombres,
"edad" : lista_edad,

}

while True:
    match menu():
        case "1":
            usuario_ing = input("ingrese su usuario ")
            usuario_edad_ing = input("ingrese edad ")
            lista_nombres.append(usuario_ing)
            lista_edad.append(usuario_edad_ing)
        case "2":
            usuario_mod1 = input("ingrese el nombre a cambiar ")
            usuario_edad_mod1 = int(input("ingrese edad a cambiar "))
            usuario_mod2 = input("ingrese el nuevo nombre ")
            usuario_edad_mod2 = int(input("ingrese nueva edad "))
            lista_nombres.pop(usuario_mod1)
            lista_edad.pop(usuario_mod2)
        case "3":
            pass
        case "4":
    
    
    
    pausar()














