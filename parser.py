from nodos import NodoBinario, NodoNumero

def parser(lista_posfijo: list) -> list:
    pila_nodos = []

    for token in lista_posfijo:
        if token.replace(".","", 1).isdigit():
            nodo_numero = NodoNumero(token)
            pila_nodos.append(nodo_numero)

        else:
            operador = token
            derecha = pila_nodos.pop()
            izquierda = pila_nodos.pop()
            nodo = NodoBinario(operador, izquierda, derecha)
            pila_nodos.append(nodo)

    return pila_nodos