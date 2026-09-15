prioridad = {
    "+"  : 1,
    "-"  : 1,
    "*"  : 2,
    "/"  : 2,
    "**" : 3
}

asociatividad = {
    "+"  : "L",
    "-"  : "L",
    "*"  : "L",
    "/"  : "L",
    "**" : "R"
}

expresion = "2+3*4-5/2"
cola_salida = []
pila_operadores = []

for token in expresion:
    if token.replace(".","", 1).isdigit():
        cola_salida.append(token)

    elif token in prioridad:
        while (pila_operadores and 
               (prioridad[pila_operadores[-1]] > prioridad[token] or 
                (prioridad[pila_operadores[-1]] == prioridad[token] and asociatividad[token] == "L"))):
            cola_salida.append(pila_operadores.pop())
        pila_operadores.append(token)

while pila_operadores:
    cola_salida.append(pila_operadores.pop())
