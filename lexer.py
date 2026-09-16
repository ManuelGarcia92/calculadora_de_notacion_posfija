from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES

def leer_numero(texto: str, posicion: int) -> int | str:
    contador_punto_decimal = 0
    buffer = ""

    while posicion < len(texto) and (texto[posicion].isdigit() or texto[posicion] == "."):
        if texto[posicion] == ".":
            contador_punto_decimal += 1

        buffer += texto[posicion]
        posicion += 1

    if contador_punto_decimal > 1:
        raise Exception("Error: Número con varios puntos decimales")
    
    if contador_punto_decimal:
        if buffer == ".":
            return posicion, 0.0
        
        elif buffer[0] == ".":
            buffer = "0" + buffer

        elif buffer[-1] == ".":
            buffer += "0"

    return posicion, buffer

def leer_simbolo(texto: str, posicion: int) -> int | str:
    if posicion < len(texto):
        if posicion < len(texto) - 1 and texto[posicion] + texto[posicion + 1] in OPERADORES_DOBLES:
            simbolo = texto[posicion] + texto[posicion + 1]
            posicion += 2
            
        else:
            simbolo = texto[posicion]
            posicion += 1  

        return posicion, simbolo
    
def lexer(texto: str) -> list:
    lista_tokens = []
    posicion = 0

    while posicion < len(texto):
        char_actual = texto[posicion]

        if char_actual.isspace():
            posicion += 1

        elif char_actual.isdigit() or char_actual == ".":
            posicion, numero = leer_numero(texto, posicion)
            lista_tokens.append(numero)

        elif char_actual in OPERADORES_SIMPLES:
            posicion, simbolo = leer_simbolo(texto, posicion)
            lista_tokens.append(simbolo)

    return lista_tokens

