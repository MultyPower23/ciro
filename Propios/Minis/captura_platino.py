def captura(PSmax: int, # Vida Maxima
      PSactual: int,    # Vida Actual
      Rc: float,        # Ratio de Captura
      Rb: float,        # Ratio del Pokémon
      Be: float = 1     # Efecto de estado
      ):
    
    Numerador = ((3 * PSmax) - (2 * PSactual)) * Rc * Rb
    Denominador = 3 * PSmax
    Total = Numerador / Denominador * Be
    return Total


PSmax: int = int(input("PS Max: "))
Rc: float = float(input("Ratio del Pokémon: "))
while True:
    try:
        PSactual: int = int(input("\nPS Actual: "))
        Rb: float = float(input("Ratio de la pokébola: "))
    except:
        print("Solo numeros")
        continue
    try:
        DicBe = input("Problema de estado: ")
        Estados = {"dormido": 2,
                   "congelado": 2,
                   "paralizado": 1.5,
                   "quemado": 1.5,
                   "envenenado": 1.5}
        Be = Estados.get(DicBe, 1)
    except:
        print("Lo copiaste mal")
        continue
    

    print(str(captura(PSmax, PSactual, Rc, Rb, Be) / 2.55) + "%")