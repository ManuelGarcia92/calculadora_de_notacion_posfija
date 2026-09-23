from constantes import OPERACIONES

class NodoBinario:
    def __init__(self, operador, izquierda, derecha):
        self.operador = operador
        self.izquierda = izquierda
        self.derecha = derecha

    def evaluar(self) -> int | float:
        valor_izq = self.izquierda.evaluar()
        valor_der = self.derecha.evaluar()
        resultado = OPERACIONES[self.operador](valor_izq, valor_der)
        return resultado


class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self) -> int | float:
        if "." in self.valor:
            valor = float(self.valor)
        else:
            valor = int(self.valor)
        return valor