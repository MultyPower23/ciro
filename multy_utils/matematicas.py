from multy_utils.colores import error

def porcentaje(parte:float, total:float) -> float:
    return (parte / total) * 100

def es_par(num:int) -> bool:
    return num % 2 == 0

def es_inpar(num:int) -> bool:
    return num % 2 != 0

def promedio(lista) -> float:
    return sum(lista) / len(lista)