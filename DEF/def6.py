def calcularresto(dividendo:int,divisor:int):
    resto = dividendo % divisor
    
    return resto


#print(calcularresto(10,3)) 

def esmultiplo(a:int, b:int):
    """verifica si un numero es multiplo de otro

    Args:
        a (int): numero a verificar
        b (int): posible numro

    Returns:
        _type_: booleano
    """
    if a % b == 0: #si el resto (%) de dividir a por b es 0...
        return True
    else:
        return False


#print(esmultiplo(12,6))

def es_par(valor: int):
    return calcularresto(valor,2)


