from enum import Enum


# ======================
# === PINTAR STRINGS ===
# ======================
class Color(Enum):

    # === NEGROS / GRISES ===
    NEGRO = "\033[30m"
    GRIS_OSCURO = "\033[38;5;238m"
    GRIS_MEDIO = "\033[38;5;244m"
    GRIS = "\033[90m"
    GRIS_CLARO = "\033[38;5;250m"
    BLANCO = "\033[37m"
    BLANCO_BRILLANTE = "\033[97m"

    # === ROJOS ===
    ROJO = "\033[31m"
    ROJO_CLARO = "\033[91m"
    ROJO_OSCURO = "\033[38;5;124m"
    ROJO_SANGRE = "\033[38;5;88m"
    ROJO_CORAL = "\033[38;5;203m"

    # === ROSAS / MAGENTAS ===
    ROSA = "\033[38;5;205m"
    ROSA_CLARO = "\033[38;5;218m"
    ROSA_CHICLE = "\033[38;5;212m"
    FUCSIA = "\033[38;5;201m"
    MAGENTA_CLARO = "\033[95m"

    # === MORADOS / VIOLETAS ===
    MORADO = "\033[35m"
    VIOLETA = "\033[38;5;177m"
    LAVANDA = "\033[38;5;183m"
    PURPURA = "\033[38;5;129m"

    # === AZULES ===
    AZUL = "\033[34m"
    AZUL_CLARO = "\033[94m"
    AZUL_CIELO = "\033[38;5;117m"
    AZUL_ACERO = "\033[38;5;67m"
    AZUL_MARINO = "\033[38;5;18m"
    AZUL_PROFUNDO = "\033[38;5;19m"

    # === CYAN / TURQUESAS ===
    CYAN = "\033[36m"
    CYAN_CLARO = "\033[96m"
    TURQUESA = "\033[38;5;80m"
    AGUAMARINA = "\033[38;5;86m"
    MENTA = "\033[38;5;121m"

    # === VERDES ===
    VERDE = "\033[32m"
    VERDE_CLARO = "\033[92m"
    VERDE_LIMA = "\033[38;5;118m"
    VERDE_BOSQUE = "\033[38;5;28m"
    VERDE_OLIVA = "\033[38;5;64m"
    VERDE_OSCURO = "\033[38;5;22m"

    # === AMARILLOS ===
    AMARILLO = "\033[33m"
    AMARILLO_CLARO = "\033[93m"
    AMARILLO_DORADO = "\033[38;5;220m"
    AMARILLO_MOSTAZA = "\033[38;5;178m"
    ARENA = "\033[38;5;223m"

    # === NARANJAS ===
    NARANJA = "\033[38;5;208m"
    NARANJA_CLARO = "\033[38;5;215m"
    NARANJA_QUEMADO = "\033[38;5;166m"
    MELOCOTON = "\033[38;5;216m"

    # === TIERRA / MARRONES ===
    MARRON = "\033[38;5;94m"
    MARRON_CLARO = "\033[38;5;137m"
    CAFE = "\033[38;5;130m"
    BEIGE = "\033[38;5;230m"


class Estilo(Enum):

    RESET = "\033[0m"
    NEGRILLA = "\033[1m"
    TENUE = "\033[2m"
    ITALICA = "\033[3m"
    SUBRAYADO = "\033[4m"
    PARPADEO = "\033[5m"
    INVERTIDO = "\033[7m"
    OCULTO = "\033[8m"
    TACHADO = "\033[9m"


# def pintar(texto:str, color:str = None, negrilla = False):
#     codigo = ""
#     if color:
#         codigo += colores[color.lower()]

#     if negrilla:
#         codigo += colores["negrilla"]

#     return codigo + texto + colores["reset"]

# def estilizar(texto:str, *estilos_usar:str):
#     codigo = ""
#     for estilo in estilos_usar:
#         codigo += estilos[estilo.lower()]
#     return codigo + texto + estilos["reset"]


def estilizar(texto: str, *opciones) -> str:
    codigo = ""

    for opcion in opciones:
        codigo += opcion.value

    return codigo + texto + Estilo.RESET.value


def pintar(texto: str, *opciones) -> None:
    print(estilizar(texto, *opciones))


def error(mensaje: str = "Hiciste algo ilegal") -> None:
    pintar(f"[ERROR]: {mensaje}", Color.ROJO_SANGRE, Estilo.NEGRILLA, Estilo.SUBRAYADO)


def ok(mensaje: str) -> None:
    pintar(mensaje, Color.VERDE_LIMA, Estilo.ITALICA)


def alerta(mensaje: str) -> None:
    pintar(
        f"[INFO]: {mensaje}",
        Color.NARANJA_CLARO,
        Estilo.NEGRILLA,
        Estilo.SUBRAYADO,
        Estilo.ITALICA,
    )


def info(mensaje: str) -> None:
    pintar(f"[INFO]: {mensaje}", Color.AZUL_ACERO, Estilo.ITALICA, Estilo.NEGRILLA)


def ver_variable(nombre: str, valor) -> None:
    pintar(f"[DEBUG] {nombre} = {valor}", Color.VERDE_OLIVA, Estilo.TENUE)
