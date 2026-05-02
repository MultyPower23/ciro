from math import tan, radians


def angulo() -> float:
    while True:
        try:
            a: float = float(input("Ingresa el ángulo: "))
            if (a < 90) and (a > 0):
                return radians(a)
        except ValueError:
            print("Debe ser un valor númerico")


def base(retroceso: float, I_angulo: float, II_angulo: float) -> float:
    a: float = retroceso * tan(II_angulo)
    b: float = tan(I_angulo) - tan(II_angulo)
    return a / b


def altura(base: float, angulo: float) -> float:
    return base * tan(angulo)


alpha: float = angulo()
beta: float = angulo()
r: float = float(input("¿Cuanta distancia retrocediste? (en metros): "))
p: float = float(input("¿Cuanto mides de los ojos para abajo? (en metros): "))

x: float = base(r, alpha, beta)
h_1: float = altura(x, alpha)
h_2: float = altura(x + r, beta)
h_media: float = (h_1 + h_2) / 2

print(
    f"X: {x:.2f} \nh_1: {h_1:.2f} \nh_2: {h_2:.2f} \nLa altura media es {h_media:.2f} y mas la medida tuya es {h_media+p:.2f}"
)
