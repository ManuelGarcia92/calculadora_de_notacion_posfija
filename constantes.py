OPERACIONES = {
    "**": lambda x, y: x ** y,
    "$" : lambda x, y: y ** (1 / x),
    "%" : lambda x, y: x % y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y,
    "//": lambda x, y: x // y,
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y
}

OPERADORES_SIMPLES = {"+", "-", "*", "/", "$", "%", "(", ")"}

OPERADORES_DOBLES = {"**", "//"}

PRIORIDAD = {
    "+"  : 1,
    "-"  : 1,
    "*"  : 2,
    "/"  : 2,
    "//" : 2,
    "%"  : 2,
    "$"  : 3,
    "**" : 3
}

ASOCIATIVIDAD = {
    "+"  : "L",
    "-"  : "L",
    "%"  : "L",
    "*"  : "L",
    "/"  : "L",
    "//" : "L",
    "%"  : "L",
    "$"  : "R",
    "**" : "R"
}
