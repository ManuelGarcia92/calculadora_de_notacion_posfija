import operaciones
OPERACIONES = {
    "**": lambda x, y: x ** y,
    "$" : lambda x, y: operaciones.raiz_enesima(x, y),
    "//": lambda x, y: operaciones.division_entera(x, y),
    "%" : lambda x, y: operaciones.modulo(x, y),
    "/" : lambda x, y: operaciones.division(x, y),
    "*" : lambda x, y: x * y,
    "-" : lambda x, y: x - y,
    "+" : lambda x, y: x + y
} 

OPERADORES_SIMPLES = {"+", "-", "*", "/", "%", "$", "(", ")"}

OPERADORES_DOBLES = {"//", "**"}

PRIORIDAD = {
    "**" : 3,
    "$"  : 3,
    "//" : 2,
    "%"  : 2,
    "/"  : 2,
    "*"  : 2,
    "-"  : 1,
    "+"  : 1,
}  

ASOCIATIVIDAD = {
    "**" : "R",
    "$"  : "R",
    "//" : "L",
    "%"  : "L",
    "/"  : "L",
    "*"  : "L",
    "-"  : "L",
    "+"  : "L",
}  
  
