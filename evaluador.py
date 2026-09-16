def evaluar_posfijo(lista_posfijo: list, operaciones: dict) -> float | int:
    pila_numeros = []
    for token in lista_posfijo:
        if token in operaciones:
            b = float(pila_numeros.pop())
            a = float(pila_numeros.pop())
            resultado = operaciones[token](a, b)
            pila_numeros.append(resultado)
        else:
            pila_numeros.append(token)
    return pila_numeros[0] if pila_numeros else 0