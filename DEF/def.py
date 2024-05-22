
'''
def saludar():
    print("holas")

def nombreperso(nombre): #retiene informacion para reutilizarla cuantas veces quiera.
    print("hola " + nombre)



nombreperso("pedro")
nombreperso("maximo")
nombreperso("franco")



def calcularporcentaje(cantidad, total):
    return cantidad * 100 / total


print(calcularporcentaje(50, 76))
'''
'''
def cargar_datos():
    cadena1 = ingresar_cadena("nombre")
    cadena2 = ingresar_cadena("apellido")
    cadena3 = ingresar_cadena("edad")
    cadena4 = ingresar_cadena("fecha nacimiento")


def ingresar_cadena(mensaje):
    cadena = input(f"ingrese su {mensaje} ")
    print(cadena)
    return cadena

cargar_datos()
print(ingresar_cadena)
'''

def sumar():
    num1 = int(input("ingrese 1er numero:"))
    num2 = int(input("ingrese 2do numero:"))    
    return num1 + num2


print(sumar())

#pedir dos numeros de consola usando la funcion sumar y mostrar el resultado por pantalla



