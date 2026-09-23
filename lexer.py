from constantes import OPERADORES_SIMPLES, OPERADORES_DOBLES

def leer_numero(texto: str, pos: int) -> int | str:
    contador_punto_decimal = 0
    buffer = ""

    while pos < len(texto) and (texto[pos].isdigit() or texto[pos] == "."):
        if texto[pos] == ".":
            contador_punto_decimal += 1

        buffer += texto[pos]
        pos += 1

    if contador_punto_decimal > 1:
        raise Exception("Error: Número con varios puntos decimales")
    
    if contador_punto_decimal:
        if buffer == ".":
            return pos, "0.0"
        
        elif buffer[0] == ".":
            buffer = "0" + buffer

        elif buffer[-1] == ".":
            buffer += "0"

    return pos, buffer

def leer_simbolo(texto: str, pos: int) -> int | str:
    if pos < len(texto):
        if pos < len(texto) - 1 and texto[pos] + texto[pos + 1] in OPERADORES_DOBLES:
            simbolo = texto[pos] + texto[pos + 1]
            pos += 2
            
        else:
            simbolo = texto[pos]
            pos += 1  

        return pos, simbolo
    
def lexer(texto: str) -> list:
    lista_tokens = []
    pos = 0

    while pos < len(texto):
        char_actual = texto[pos]

        if char_actual.isspace():
            pos += 1

        elif char_actual.isdigit() or char_actual == ".":
            pos, numero = leer_numero(texto, pos)
            lista_tokens.append(numero)

        elif char_actual in OPERADORES_SIMPLES:
            pos, simbolo = leer_simbolo(texto, pos)
            lista_tokens.append(simbolo)
            
    return lista_tokens
  
