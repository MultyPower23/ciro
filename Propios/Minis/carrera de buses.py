import random
import time
import os


# ======================
# COLORES
# ======================

RESET = "\033[0m"
AZUL = "\033[34m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
ROJO = "\033[31m"
MORADO = "\033[35m"
CIAN = "\033[36m"


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def color_velocidad(v, vmax):
    if v < vmax * 0.25:
        return AZUL
    elif v < vmax * 0.55:
        return VERDE
    elif v < vmax * 0.8:
        return AMARILLO
    else:
        return ROJO


# ======================
# INPUT
# ======================

def pedir_nombre(n):
    while True:
        nombre = input(f"Nombre del bus {n}: ").strip()

        if 1 <= len(nombre) <= 16:
            return nombre

        print("Nombre inválido.")


# ======================
# SPRITE
# ======================

def crear_bus(nombre):
    ancho = 20

    nombre = nombre[:ancho-4]
    espacios = (ancho - 2 - len(nombre)) // 2

    centro = (
        " " * espacios +
        nombre +
        " " * (ancho - 2 - len(nombre) - espacios)
    )

    return [
        "   _____________   ",
        " _/|" + centro + "|\\__ ",
        "|__|_____________|__|",
        "  O---O-------O---O  "
    ]


# ======================
# CONFIG
# ======================

TURBO_MAX = 100
TURBO_DUR = 6
TURBO_MULT = 2.5
RECARGA = 2

PISTA = 140

ACEL_MAX = 0.25
VEL_MAX = 2.5
FRICCION = 0.05


# ======================
# CREAR BUSES
# ======================

while True:
    try:
        n = int(input("Cuántos buses (2-5): "))
        mostrar_estrategia = input("¿Mostrar estrategia? (s/n): ").lower().startswith("s")
        usar_estrategia = mostrar_estrategia

        if 2 <= n <= 5:
            break
    except:
        pass

    print("Número inválido.")


buses = []

for i in range(n):

    nombre = pedir_nombre(i+1)

    bus = {
        "nombre": nombre,
        "sprite": crear_bus(nombre),
        "pos": 0.0,
        "vel": 0.0,
        "turbo": 10,
        "activo": 0,
        "fin": None,
        "estilo": (
                    random.choice(["AGRESIVO", "BALANCEADO", "CONSERVADOR"])
                    if usar_estrategia else
                    "NORMAL"
        ),

    }

    buses.append(bus)


# ======================
# START
# ======================

print("\nPreparados...")
time.sleep(1)

print("Listos...")
time.sleep(1)

print("YA!")
time.sleep(1)

inicio = time.perf_counter()


# ======================
# RENDER SETUP
# ======================

alto_bus = len(buses[0]["sprite"])
espacio = 3

alto = n * alto_bus + (n-1)*espacio + 2


# ======================
# LOOP
# ======================

while True:

    linea = "INICIO " + "-" * (PISTA - 13) + " FINAL"
    col_final = len(linea) - 6

    posiciones = [b["pos"] for b in buses]


# ------------------
# TURBO CON ESTRATEGIA
# ------------------
    if usar_estrategia:

        max_pos = max(b["pos"] for b in buses)

        for b in buses:

            if b["activo"] > 0:
                continue

            if b["turbo"] < 25:
                continue


            avance = b["pos"] / col_final


            prob = 0.05


            if b["estilo"] == "AGRESIVO":

                if avance < 0.4:
                    prob = 0.25
                else:
                    prob = 0.15


            elif b["estilo"] == "BALANCEADO":

                if 0.3 < avance < 0.7:
                    prob = 0.22
                else:
                    prob = 0.08


            elif b["estilo"] == "CONSERVADOR":

                if avance > 0.7:
                    prob = 0.30
                else:
                    prob = 0.03



            if random.random() < prob:

                b["activo"] = TURBO_DUR
    else:

    # Turbo simple para todos
        for b in buses:

            if b["activo"] > 0:
                continue

            if b["turbo"] < 30:
                continue

            if random.random() < 0.12:
                b["activo"] = TURBO_DUR

            
    # ------------------
    # FÍSICA
    # ------------------

    for b in buses:

        # Si ya llegó, no corre
        if b["fin"] is not None:
            continue


        if b["activo"] > 0:

            if b["estilo"] == "AGRESIVO":
                mult = 3.0  # explosivo
            elif b["estilo"] == "BALANCEADO":
                mult = 2.0  # normal
            elif b["estilo"] == "CONSERVADOR":
                mult = 2.5  # remontada
            else:  # NORMAL
                mult = 2.0
        else:
            mult = 1


        acel = random.uniform(0, ACEL_MAX) * mult

        b["vel"] += acel


        if b["activo"] > 0:
            b["turbo"] -= 6
            b["activo"] -= 1
        else:
            if b["estilo"] == "AGRESIVO":
                b["turbo"] += RECARGA * 0.8   # gasta más, recupera lento

            elif b["estilo"] == "BALANCEADO":
                b["turbo"] += RECARGA * 1.0   # normal

            elif b["estilo"] == "CONSERVADOR":
                b["turbo"] += RECARGA * 1.4   # ahorra y recarga rápido

            else:  # NORMAL
                b["turbo"] += RECARGA



        dist = max(posiciones) - b["pos"]

        if dist > 10:
            b["turbo"] += 3
        elif dist > 5:
            b["turbo"] += 2
        elif dist > 2:
            b["turbo"] += 1


        res = b["vel"] * 0.08

        b["vel"] -= FRICCION + res


        b["vel"] = max(0, min(b["vel"], VEL_MAX))
        b["turbo"] = max(0, min(b["turbo"], TURBO_MAX))

        b["pos"] += b["vel"]


    # ------------------
    # RENDER
    # ------------------

    limpiar()

    filas = []

    for _ in range(alto):
        f = [" "] * (PISTA + 40)
        f[col_final] = "|"
        filas.append(f)


    llegados = 0


    y_base = 0


    for b in buses:

        # HUD
        cv = color_velocidad(b["vel"], VEL_MAX)
        ct = CIAN if b["turbo"] > 30 else AZUL

        if b["fin"] is None:
            hud = f"{cv}V:{b['vel']:4.2f}{RESET} {ct}T:{int(b['turbo']):3d}{RESET}"

            if mostrar_estrategia:
                hud += f" {b['estilo']}"

        else:
            hud = f"{VERDE}FIN {b['fin']:.2f}s{RESET}"

        for i, c in enumerate(hud):
            filas[y_base][int(b["pos"]) + i] = c


        # Bus
        for i, l in enumerate(b["sprite"]):

            for j, c in enumerate(l):

                x = int(b["pos"]) + j
                y = y_base + i + 1


                # Detectar llegada
                if filas[y][x] == "|" and b["fin"] is None:

                    b["fin"] = time.perf_counter() - inicio
                    llegados += 1



                if b["activo"] > 0 and c != " ":
                    filas[y][x] = MORADO + c + RESET
                else:
                    filas[y][x] = c


        y_base += alto_bus + espacio


    for f in filas:
        print("".join(f))


    time.sleep(0.25)


    # ------------------
    # FIN CONDICIÓN
    # ------------------

    terminados = sum(1 for b in buses if b["fin"] is not None)

    if terminados == n:
        break



# ======================
# RANKING CON EMPATES
# ======================

print("\n🏁 CLASIFICACIÓN FINAL\n")


# Solo los que terminaron
finalistas = [b for b in buses if b["fin"] is not None]


# Ordenar por tiempo
finalistas.sort(key=lambda b: b["fin"])


puestos = []
i = 0
pos = 1


while i < len(finalistas):

    actual = finalistas[i]
    tiempo = round(actual["fin"], 2)

    empatados = [actual]

    j = i + 1

    # Buscar empates
    while j < len(finalistas):

        if round(finalistas[j]["fin"], 2) == tiempo:
            empatados.append(finalistas[j])
            j += 1
        else:
            break


    puestos.append((pos, tiempo, empatados))


    pos += len(empatados)
    i = j


# Mostrar
for puesto, tiempo, grupo in puestos:

    if puesto == 1:
        medalla = "🥇"
    elif puesto == 2:
        medalla = "🥈"
    elif puesto == 3:
        medalla = "🥉"
    else:
        medalla = f"{puesto}°"


    for b in grupo:

        print(
            f"{medalla} Puesto {puesto}: {b['nombre']} — {tiempo:.2f} s"
        )