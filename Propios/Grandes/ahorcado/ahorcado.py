from multy_utils.colores import Color, Estilo, pintar
from random import choice

palabras = ["estetica", "queso", "elevador", "zapato", "toro", "abajo", "perro"]
with open(r"E:\Codigos USB\Propios\Grandes\ahorcado\glosario.txt", mode="x", encoding="utf-8") as glosario:
    glosario.write("GLOSARIO:")

PALABRA_CORRECTA: str = choice(palabras)
largo: int = len(PALABRA_CORRECTA)

MUNECO_FINAL = "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|   /|\\  \n" \
               "|   / \\  \n" \
               "|         \n" \
               "___________" \
               
intentos: int = 0

abc: str = "ABCDEFGHIJKLMNOPQSTUVWXYZ"

while True:


    # ================
    # GRAFICA AHORCADO
    # ================

    match intentos:
        case 0:
            print(
            "|----|    \n" \
            "|    |    \n" \
            "|         \n" \
            "|         \n" \
            "|         \n" \
            "|         \n" \
            "___________" \
            )
        case 1:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|         \n" \
               "|         \n" \
               "|         \n" \
               "___________" \
            )
        case 2:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|    |    \n" \
               "|         \n" \
               "|         \n" \
               "___________" \
            )
        case 3:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|   /|    \n" \
               "|         \n" \
               "|         \n" \
               "___________" \
            )
        case 4:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|   /|\\  \n" \
               "|         \n" \
               "|         \n" \
               "___________" \
            )
        case 5:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|   /|\\  \n" \
               "|   /     \n" \
               "|         \n" \
               "___________" \
            )
        case 6:
            print(
               "|----|    \n" \
               "|    |    \n" \
               "|    0    \n" \
               "|   /|\\  \n" \
               "|   / \\  \n" \
               "|         \n" \
               "___________" \
            )
            pintar("PERDISTE: Te has ahorcado", Color.ROJO_SANGRE, Estilo.NEGRILLA)
            print(f"La palabra correcta era {PALABRA_CORRECTA}")
            break
        case _:
            pass
    

    # ===============
    # PALABRA
    # ===============

    palabra: str = input("Ingresa la palabra: ")
    intentos += 1

    if palabra == PALABRA_CORRECTA:
        pintar("¡FELICIDADES GANASTE!", Color.VERDE_LIMA, Estilo.NEGRILLA)
        break
    

    for letra in palabra:
        pass

    # ===============
    # ABECEDARIO
    # ===============

   # for letra in palabra:
     
    # ==================
    # LIMPIAR PANTALLA
    # ==================

    print("\033[H\033[J", end="")