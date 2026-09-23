def shuting_yard(lista_tokens: list, prioridad: dict, asociatividad: dict) -> list:
    cola_salida = []
    pila_operadores = []

    for token in lista_tokens:
        if token.replace(".","", 1).isdigit():
            cola_salida.append(token)

        elif token == "(":
            pila_operadores.append(token)

        elif token == ")":
            while pila_operadores and pila_operadores[-1] != "(":
                cola_salida.append(pila_operadores.pop())  
            if pila_operadores:
                pila_operadores.pop() 

        elif token in prioridad:
            while (pila_operadores and pila_operadores[-1] != "(" and
                    (prioridad[pila_operadores[-1]] > prioridad[token] or 
                      (prioridad[pila_operadores[-1]] == prioridad[token] and asociatividad[token] == "L"))):
                cola_salida.append(pila_operadores.pop())
            pila_operadores.append(token)

    while pila_operadores:
        cola_salida.append(pila_operadores.pop())
        
    return cola_salida