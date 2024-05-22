def suma(a,b):
    return a + b

def multiplicacion(a,b):
    return a * b


def division(a,b):
    return a / b

def resta(a,b):
    return a - b

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    