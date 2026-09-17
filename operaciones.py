def division(x, y):
    if y == 0:
        raise Exception("Error matemático: No se puede dividir por 0")
    return x / y
    
def division_entera(x, y):
    if y == 0:
        raise Exception("Error matemático: No se puede dividir por 0")
    return x // y
    
def modulo(x, y):
    if y == 0:
        raise Exception("Error matemático: Módulo no se puede dividir por 0")
    return x % y

def raiz_enesima(x, y):
    if y < 0 and x % 2 != 0:
        return -(-y ** x)
    return y ** (1 / x)