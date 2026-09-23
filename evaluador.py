def evaluar(instrucciones) -> int | float | None:
    resultado = None
    if instrucciones is not None:
        for instruccion in instrucciones:
            resultado = instruccion.evaluar()
    return resultado