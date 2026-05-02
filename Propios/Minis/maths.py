# ====== CABECERA ======

from math import pi, isqrt, sqrt
from typing import TypeVar
#from hypothesis import given
#from hypothesis import strategies as s

A = TypeVar('A')

def error():
    print(pintar("ERROR: Hiciste algo ilegal", "rojo", True))

estilos = {
    "rojo": "\033[31m",
    "verde": "\033[32m",
    "amarillo": "\033[33m",
    "azul": "\033[34m",
    "morado": "\033[35m",
    "cyan": "\033[36m",
    "negrilla": "\033[1m",
    "reset": "\033[0m"
}

def pintar(texto:str, color:str, negrilla=False):
    codigo = estilos[color]

    if negrilla:
        codigo += estilos["negrilla"]

    return codigo + texto + estilos["reset"]

# ====== PROCEDIMIENTOS ======

def volumenEsfera():
    r = float(input("Radio: "))
    if r > 0:
        volumen = (4 / 3) * pi * r ** 3
        return volumen
    else:
        error()
        return

def media():
    valores = input("Dime 3 numeros: ").split()

    numeros = []
    for x in valores:
        numeros.append(float(x))

    valor = 0
    for i in numeros:
        valor += i

    media = valor / len(numeros)
    return media

    ##numeros = list(map(float, input("Dime numeros: ").split())) --------------- la forma correcta
    ##return sum(numeros) / len(numeros)

def areaDeCoronaCircular():
    r1 = float(input("Radio Interno: "))
    r2 = float(input("Radio Externo: "))
    if (r1 > 0) and (r2 > r1):
        area = pi * (r2 ** 2 - r1 ** 2)
        return area
    else:
        error()
        return 
    
def ultimoDigito():
    numero = int(input("Numero: "))
    resultado = numero % 10
    return resultado


def raizCuadrada(n = None, entera = False):
    if n is None:
        n = int(input("El numero es: "))
    
    if n > -1:
        if entera is False:
            raiz = sqrt(n)
        elif entera:
            raiz = isqrt(n)
        return raiz
    else:
        error()
        return 
    

def esPrimo():
    n = int(input("Posible primo: "))
    if n > 1:
        for i in range(2, raizCuadrada(n, True)+1):
            if n % i == 0:
                return "No es primo"
        return "Si es primo"
    else:
        return "No es posible"
    

def areaTriangulo():
    lados = input("Tamaño de los lados: ").split()
    a = float(lados[0])
    b = float(lados[1])
    c = float(lados[2])

    ## a, b, c = map(float, input("Tamaño de los lados: ").split()) ---------------- la forma correcta

    if a + b <= c or a + c <= b or b + c <= a:
        return pintar("ERROR: Eso no es un triangulo", "rojo", True)

    s = (a + b + c) / 2
    
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

class Vector2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def magnitud(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"<{self.x}, {self.y}>"

class Vector3D:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def magnitud(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

def distancia2D():
    p1 = input("Punto Origen (x y): ").split()
    p2 = input("Punto Llegada (x y): ").split()

    if len(p1) > 2 or len(p2) > 2:
        print (pintar("ERROR: Demasiados ejes", "rojo", True))
        return 
    elif len(p1) < 2 or len(p2) < 2:
        print (pintar("ERROR: Insufisientes ejes", "rojo", True))
        return 

    x1, y1 = map(float, p1)
    x2, y2 = map(float, p2)

    v = Vector2D(x2 - x1, y2 - y1)
    return v, v.magnitud()

def distancia3D():
    p1 = input("Punto Origen (x y z): ").split()
    p2 = input("Punto Llegada (x y z): ").split()

    if len(p1) > 3 or len(p2) > 3:
        print (pintar("ERROR: Demasiados ejes", "rojo", True))
        return 
    elif len(p1) < 3 or len(p2) < 3:
        print (pintar("ERROR: Insufisientes ejes", "rojo", True))
        return 

    x1, y1, z1 = map(float, p1)
    x2, y2, z2 = map(float, p2)

    v = Vector3D(x2 - x1, y2 - y1, z2 - z1)
    return v, v.magnitud()






# ====== LISTA DE PROCEDIMENTOS ======

procesos = {
    "Volumen de una Esfera": volumenEsfera,
    "La Media de unos Datos": media,
    "Area de una Corona Circular": areaDeCoronaCircular,
    "La Ultima Cifra de un Numero": ultimoDigito,
    "¿Es un numero primo?": esPrimo,
    "Raiz cuadrada": raizCuadrada,
    "Area de un Triangulo": areaTriangulo,
    "Distancia entre dos Puntos 2D": distancia2D,
    "Distancia entre dos Puntos 3D": distancia3D
}

# ====== MENÚ ======

while True:

    nombres = list(procesos.keys())

    print(pintar("\nProcesos disponibles:", "verde", True))
    for i, nombre in enumerate(nombres, start=1):
        print(i, "-", nombre)
    print(pintar("0 - Salir", "negrilla"))

    opcion = int(input(pintar("\nDime el número del procedimiento: ", "azul", True)))

    if opcion == 0:
        print(pintar("Adios", "rojo", True))
        break

    if 1 <= opcion <= len(nombres):
        nombre_elegido = nombres[opcion - 1]
        funcion = procesos[nombre_elegido]

        resultado = funcion()

    if resultado is not None:
        if isinstance(resultado, tuple):
            v, d = resultado
            print(pintar("Vector:", "amarillo", True), v)
            print(pintar("Distancia:", "amarillo", True), d)
        else:
            print(pintar("Resultado =", "amarillo", True), resultado)

    else:
        print("Proceso no reconocido.")