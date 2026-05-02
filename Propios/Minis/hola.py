import msvcrt
import math

print("Dijita tu numero de telefono")
print("1=*3, 2=+7, 3=/5, 4=-2, 5=FLOOR, 6=RAIZ CUADRADA, 7=CUADRADO, 8=LOGARITMO BASE 10")
telefono = 1

while True:
    key = msvcrt.getch().lower()
    if key == b'1':
        telefono *= 3
        #print("*3")
        print(telefono)

    elif key == b'2':
        telefono += 7
        #print("+7")
        print(telefono)

    elif key == b'3':
        telefono /= 5
        #print("/5")
        print(telefono)

    elif key == b'4':
        telefono -= 2
        #print("-2")
        print(telefono)

    elif key == b'5':
        telefono = math.floor(telefono)
        #print("FLOOR")
        print(telefono)

    elif key == b'6':
        telefono = telefono ** (1/2)
        #print("RAIZ CUADRADA")
        print(telefono)

    elif key == b'7':
        telefono = telefono ** 2
        #print("CUADRADO")
        print(telefono)
    
    elif key == b'8':
        telefono = math.log10(telefono)
        #print("LOGARITMO BASE 10")
        print(telefono)

    elif telefono == 3218878347:
        print("Numero de telefono correcto!")
        break