print("Hoy te dire mi querid@ amig@ si tu tienes chance de conseguir pareja o no (pensado para Colombia)")
print("Te pedire ciertos datos para hallar tu porcentaje de romance")
print("Partiremos desde toda la población general y mediante filtros buscaremos a tu alma gemela")

pobla = float(input("Dime, cual es el N° de personas en tu área geografica: "))


#=== FILTRO DE GENERO ===
def _genero():
    print("=== FILTRO DE GENERO ===")
    Ogen = int(input("Genero de interes, ¿te interesa solo uno, los dos o ninguno?: " ))
    while (Ogen != 1) and (Ogen !=2):
        if Ogen == 0:
            print("Que haces aca con esta formula si no te gusta ningun genero?")
        elif Ogen != 1 and Ogen != 2:
            print("No hay tal cantidad de generos")
        
        Ogen = int(input("Cuantos generos BIOLOGICOS te gustan?"))

    gen = Ogen * 0.5
    return gen



#=== FILTRO DE EDAD ===
def _edad(minEdad, maxEdad):

    datos_edad = {
        (0, 14): 0.22,
        (15, 24): 0.17,
        (25, 34): 0.16,
        (35, 44): 0.14,
        (45, 54): 0.12,
        (55, 64): 0.10,
        (65, 120): 0.09
    }

    #rango_usuario = maxEdad - minEdad + 1
    total = 0

    for (min_e, max_e), porcentaje in datos_edad.items():
        if maxEdad >= min_e and minEdad <= max_e:
            tramo = min(maxEdad, max_e) - max(minEdad, min_e) + 1
            proporcion_tramo = tramo / (max_e - min_e + 1)
            total += porcentaje * proporcion_tramo

    return total

print("=== FILTRO DE EDAD ===")

print("Cuantas personas entran en el rango que buscas? (di tu edad minima y maxima que quieras)")

print("Si es solo una edad coloca la misma en ambos apartados")
minEdad = float(input("Minimo de edad: "))
maxEdad = float(input("Maximo de edad: "))

if minEdad > maxEdad:
    print("Creo que trucaste o algo los valores")

while minEdad > maxEdad:
    print("Si es solo una edad coloca la misma en ambos apartados")
    minEdad = float(input("Minimo de edad: "))
    maxEdad = float(input("Maximo de edad: "))

    if minEdad > maxEdad:
        print("Creo que trucaste o algo los valores")

if minEdad >= 90 or maxEdad >= 90:
    print("Entre mas arrugada la pasa mas sabrosa es, o me equivoco?")

edad = _edad(minEdad, maxEdad)



#=== FILTRO EDUCATIVO ===
def _educacion():
    print("=== FILTRO EDUCATIVO ===")

    # Nivel educativo base
    print("\nNivel mínimo que buscas:")
    print("1. Bachiller")
    print("2. Técnica / tecnológica")
    print("3. Universidad")
    print("4. Posgrado")
    print("5. Doctorado")

    nivel = int(input("Elige una opción (1-5): "))

    while nivel < 1 or nivel > 5:
        print("Opción no válida")
        nivel = int(input("Elige una opción (1-5): "))

    # Valores base
    if nivel == 1:
        edu = 0.78
    elif nivel == 2:
        edu = 0.35
    elif nivel == 3:
        edu = 0.25
    elif nivel == 4:
        edu = 0.08
    elif nivel == 5:
        edu = 0.01


    # Si eligió universidad o superior, puede filtrar por área
    if nivel >= 3:
        print("\n¿Quieres filtrar por área?")
        print("0. No")
        print("1. Ingeniería")
        print("2. Ciencias sociales")
        print("3. Salud")
        print("4. Educación")
        print("5. Artes / Humanidades")

        area = int(input("Elige opción: "))

        while area < 0 or area > 5:
            print("Opción no válida")
            area = int(input("Elige opción: "))

        if area == 1:
            edu *= 0.20
        elif area == 2:
            edu *= 0.25
        elif area == 3:
            edu *= 0.15
        elif area == 4:
            edu *= 0.15
        elif area == 5:
            edu *= 0.10


    # Filtro de perfil académico alto
    print("\n¿Quieres perfil académico alto?")
    print("1. Sí")
    print("2. No")

    perfil = int(input("Elige 1 o 2: "))

    while perfil < 1 or perfil > 2:
        print("Opción no válida")
        perfil = int(input("Elige 1 o 2: "))

    if perfil == 1:
        edu *= 0.15

    return edu



#=== FILTRO DE SOLTER@S ===
def _solteros(minEdad, maxEdad):
    datos_solteros = {
        (10, 11): 1,
        (12, 14): 0.989,
        (15, 19): 0.908,
        (20, 24): 0.687,
        (25, 29): 0.451,
        (30, 34): 0.273,
        (35, 39): 0.196,
        (40, 44): 0.169,
        (45, 49): 0.159,
        (50, 54): 0.142,
        (55, 59): 0.13,
        (60, 64): 0.121,
        (65, 69): 0.12,
        (70, 74): 0.117,
        (75, 79): 0.113,
        (80, 84): 0.104,
        (85, 500): 0.104,
    }

    prom = (minEdad + maxEdad) / 2

    for (min_e, max_e), porcentaje in datos_solteros.items():
        if min_e <= prom <= max_e:
            return porcentaje

    return 0



#=== FILTRO DE GENERO ===
def _gustas():
    print("=== ¿QUÉ TANTO TE GUSTAN? ===")
    gustas = int(input("Del 1-10 que tanto te parecen atractivos?: "))
    return max(0, min(gustas / 10, 1))



# === FILTRO ATRAES ===
def _atraes():
    print("=== ¿QUÉ TANTO ATRAES? ===")

    # --- Apariencia general ---
    print("\n¿Cómo consideras tu apariencia facial?")
    print("1. Bajo promedio")
    print("2. Promedio")
    print("3. Encima del promedio")
    print("4. Muy atractivo")

    cara = int(input("Elige opción (1-4): "))
    while cara < 1 or cara > 4:
        print("Opción no válida")
        cara = int(input("Elige opción (1-4): "))

    if cara == 1:
        atraes = 0.25
    elif cara == 2:
        atraes = 0.50
    elif cara == 3:
        atraes = 0.70
    elif cara == 4:
        atraes = 0.85


    # --- Estado físico ---
    print("\nEstado físico:")
    print("1. Sedentario")
    print("2. Normal")
    print("3. En forma")
    print("4. Atlético")

    fisico = int(input("Elige opción (1-4): "))
    while fisico < 1 or fisico > 4:
        print("Opción no válida")
        fisico = int(input("Elige opción (1-4): "))

    if fisico == 1:
        atraes *= 0.85
    elif fisico == 2:
        atraes *= 1
    elif fisico == 3:
        atraes *= 1.1
    elif fisico == 4:
        atraes *= 1.2


    # --- Estatus / proyección ---
    print("\nTu situación actual:")
    print("1. Estudiante sin ingresos")
    print("2. Estudiante con ingresos")
    print("3. Trabajo estable")
    print("4. Alto ingreso / emprendimiento fuerte")

    estatus = int(input("Elige opción (1-4): "))
    while estatus < 1 or estatus > 4:
        print("Opción no válida")
        estatus = int(input("Elige opción (1-4): "))

    if estatus == 1:
        atraes *= 0.90
    elif estatus == 2:
        atraes *= 1
    elif estatus == 3:
        atraes *= 1.1
    elif estatus == 4:
        atraes *= 1.2


    # Limitar máximo lógico
    if atraes > 0.95:
        atraes = 0.95

    return atraes



#===PORCENTAJE DE ROMANCE===
gen = _genero()
edad = edad
edu = _educacion()
sol = _solteros(minEdad, maxEdad)
gust = _gustas()
atr = _atraes()

print("Desglose:")
print("Genero:", gen)
print("Edad:", edad)
print("Educación:", edu)
print("Solteros:", sol)
print("Te gustan:", gust)
print("Atraes:", atr)

romance = (gen * edad * edu * sol * gust * atr)

if romance > 1:
    romance = 1

print("Tu porcentaje de encontrar pareja es ",(romance ** (1/6)) * 100,"%")
print("Tu estimado de personas es de ",pobla * romance)