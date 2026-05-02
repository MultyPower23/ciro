dis_pedida: float = float(input("Que distancia quieres llegar (en km): "))

distancia: float = 1 / 1000000

pliegues: int = 0

while distancia < dis_pedida:
    pliegues += 1
    distancia *= 2 

print("Pliegues totales:", pliegues, distancia)


