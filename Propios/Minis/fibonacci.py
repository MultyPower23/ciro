def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    lista = []
    for i in range(2, n+1):
        a, b = b, b + a
        lista.append(b)
    return lista
    
while True:
    n = int(input("Cual numero de la succesion quieres?: "))
    print(fibonacci(n))