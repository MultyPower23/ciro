def pedir_int(mensaje:str = "Ingrese un número: ", minimo:int = None, maximo:int = None) -> int:        
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue

            if maximo is not None and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue   

            return valor

        except ValueError:
            print("Ingrese un número válido")

def pedir_float(mensaje:str = "Ingrese un número: ", minimo:float = None, maximo: float = None) -> float:
    while True:
        try:
            valor = float(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue

            if maximo is not None and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue

            return valor

        except ValueError:
            print("Ingrese un número válido")

def pedir_str(mensaje:str = "Ingrese texto: ", minimo:int = None, maximo:int = None) -> str:
    while True:
        texto = input(mensaje).strip()

        if minimo is not None and len(texto) < minimo:
            print(f"Debe tener al menos {minimo} caracteres")
            continue

        if maximo is not None and len(texto) > maximo:
            print(f"Debe tener máximo {maximo} caracteres")
            continue

        return texto

def confirmar(mensaje:str = "¿Confirmar? (s/n): ") -> bool:
    while True:
        valor = input(mensaje).lower()

        if valor in ["s", "si", "sí"]:
            return True

        if valor in ["n", "no"]:
            return False

        print("Ingrese 's' o 'n'")

def pedir_opcion_num(mensaje:str, opciones: list[str]) -> int:
    while True:

        print(mensaje)

        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        valor = input("Seleccione una opción: ").strip()

        if valor.isdigit():

            indice = int(valor)

            if 1 <= indice <= len(opciones):
                return indice

        print("Opción inválida\n")

def pedir_opcion_texto(mensaje:str, opciones: list[str]) -> str:
    opciones_norm = [op.lower() for op in opciones]

    while True:

        valor = input(mensaje, "Opciones: ", ", ".join(opciones)).strip().lower()

        if valor in opciones_norm:
            return valor

        print("Opción inválida. Opciones:", ", ".join(opciones))