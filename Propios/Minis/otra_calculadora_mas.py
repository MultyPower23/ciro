import math

# =========================
# ------ OPERACIONES ------
# =========================


def suma(*valor):
    resultado: float = 0
    for x in valor:
        try:
            num: float = float(x)
            resultado += num
        except (ValueError, TypeError):
            print("[ERROR]: Todos deben ser valores númericos")
            return None
    return resultado


def resta(base: int | float, *valor):
    resultado: float = float(base)
    try:
        numeros = [float(x) for x in valor]
        for x in numeros[0:]:
            resultado -= x
        return resultado
    except (ValueError, TypeError, IndexError):
        print("[ERROR]: Entrada inválida o faltan argumentos")
        return None


def multi(*valor):
    if not valor:
        return 0  # evitamos que la operacion vacia regrese 1
    resultado: float = 1
    for x in valor:
        try:
            num: float = float(x)
            resultado *= num
        except ValueError:
            print("[ERROR]: Todos deben ser valores númericos")
            return None
    return resultado


def dividir(num1: int | float, num2: int | float, entero: bool = False):
    try:
        num1, num2 = float(num1), float(num2)  # forzamos la comprobacion del TypeError
        if entero:
            return num1 // num2
        return num1 / num2
    except (ValueError, TypeError):
        print("[ERROR]: Todos deben ser valores numéricos")
    except ZeroDivisionError:
        print("[ERROR]: El denominador debe ser diferente a cero (0)")
    return None


def potencia(base: int | float, indice: int | float = 2):
    try:
        return base**indice
    except TypeError:
        print("[ERROR]: Todos deben ser valores númericos")
    except ZeroDivisionError:
        print("[ERROR]: No es posible elevar cero aun exponente negativo")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")
        return None


def raiz(base: int | float, indice: int | float = 2):
    try:
        base, indice = float(base), float(
            indice
        )  # forzamos la comprobacion del TypeError
        if base < 0 and indice % 2 == 0:  # lanza el error y lo atrapamos abajo
            raise ValueError(
                "[ERROR]: El resultado es un número inmaginario, no es posible base negativa y indice par"
            )
        else:
            return base ** (1 / indice)
    except TypeError:
        print("[ERROR]: Todos deben ser valores númericos")
    except ZeroDivisionError:
        print("[ERROR]: El indice de la raiz no puede ser cero")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")
        return None


def factorial(tope: int):
    resultado: int = 1
    try:
        if tope < 0:
            raise ValueError("[ERROR]: La base debe ser igual o mayor a cero")
        tope = int(tope)
        if tope == 0:
            return resultado
        for x in range(2, tope + 1):
            resultado *= x
        return resultado
    except (ValueError, TypeError):
        print("[ERROR]: Debe ser un número entero")
    except OverflowError:
        print("[ERROR]: El proceso es demasiado grande para realizarlo")


def tangente(x):
    return math.tan(x)


# ========================
# --------- MAIN ---------
# ========================


def main():
    print("BIENVENIDO A LA CALCULADORA")
    while True:
        print(
            "\nPROCESOS DISPONIBLES"
            "\n1. Sumar"
            "\n2. Restar"
            "\n3. Multiplicación"
            "\n4. Divisón"
            "\n4. Potencia"
            "\n4. Raiz"
            "\n4. Factorial"
        )

        print(
            "\nPROCESOS DISPONIBLES"
            "\n1. Sumar"
            "\n2. Restar"
            "\n3. Multiplicación"
            "\n4. Divisón"
            "\n4. Potencia"
            "\n4. Raiz"
            "\n4. Factorial"
        )


main()
