from extras import limpiar_terminal, pausa
from constantes import PRIORIDAD, ASOCIATIVIDAD
from lexer import lexer
from shuting_yard import shuting_yard
from parser import parser

def main() -> None:
    while True:
        limpiar_terminal()
        print("[Ingrese break para salir]")
        texto = input(">>> : ")
        if texto == "break":
            break 
        try:
            expresion = lexer(texto)
            operacion = shuting_yard(expresion, PRIORIDAD, ASOCIATIVIDAD)
            arbol = parser(operacion)
            resultado = arbol.evaluar()
            print(resultado)
        except Exception as error:
            print(error)
        pausa()

if __name__ == "__main__":
    main()