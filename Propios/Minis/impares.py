max: int = int(input("Ingresa el tope de números: "))

print("Todos los impares son:")
for i in range(0, max+1):
    if i % 2 != 0:
        print(i)