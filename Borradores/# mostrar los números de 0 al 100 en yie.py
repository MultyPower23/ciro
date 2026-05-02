# mostrar los números de 0 al 100 en yield
def mostrar100():
    for x in range(101):
        yield x

# calcular los cuadrados uno a uno de una [1,2,3,4,5]
def cuadrados():
    for x in range(6):
        yield x**2

def saltos_diez():
    numero = 0
    while True:
        yield numero
        numero += 10

def semaforo():
    yield "Verde"
    yield "Amarillo"
    yield "Rojo"
    
cuadra = cuadrados()
while cuadra != 25:
    input()
    print(next(cuadra))

# hacer 2 ejemplos con generador

num100 = mostrar100()
while num100 != 100:
    input()
    print(next(num100))

luces = semaforo()

input()
print(next(luces))
input()
print(next(luces))
input()
print(next(luces))



cuenta = saltos_diez()

input("Presiona para ver el primero: ")
print(next(cuenta))
input("Presiona para el siguiente: ")
print(next(cuenta))
input("Presiona para uno más: ")
print(next(cuenta))