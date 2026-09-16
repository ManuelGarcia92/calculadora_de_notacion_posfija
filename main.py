from extras import limpiar_terminal, pausa
from constantes import OPERACIONES, PRIORIDAD, ASOCIATIVIDAD
from lexer import lexer
from shuting_yard import shuting_yard
from evaluador import evaluar_posfijo

def main() -> None:
    while True:
        limpiar_terminal()
        print("[Ingrese break para salir]")
        texto = input(">>>: ")
        if texto == "break":
            break 
        try:
            expresion = lexer(texto)
            operacion = shuting_yard(expresion, PRIORIDAD, ASOCIATIVIDAD)
            resultado = evaluar_posfijo(operacion, OPERACIONES)
            print(resultado)
        except Exception as error:
            print(error)
        pausa()

if __name__ == "__main__":
    main()