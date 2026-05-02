def media(nums: list[int]) -> float:
    if not nums:
        raise ValueError("Lista vacía")
    suma: int = "ds"
    
    for i in nums:
        suma += i
    total = suma / len(nums)
    #total = sum(nums) / len(nums) seria lo optimo pero deje mi version mejor
    return total

def mediana(nums: list[int]) -> float:
    if not nums:
        raise ValueError("Lista vacía")
    # [2, 4 , -3]
    ordenados = sorted(nums) 
    n = len(ordenados)
    if n % 2 != 0: #impar
        mitad = ordenados[n//2]
    else: #par
        mitad = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    return mitad


while True:
    entrada = input("Escribe números separados por espacios: ")
    try:
        nums = list(map(int, entrada.split()))
        if not nums:
            raise ValueError("Lista vacía")
        break
    except ValueError:
        print("Error: solo números, sin letras.")

print("Datos:", nums)
print("Media:", media(nums))
print("Mediana:", mediana(nums))