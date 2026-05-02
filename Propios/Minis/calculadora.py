import math

numero1 = float(input("Escribe el primer numero: "))
numero2 = float(input("Escribe el segundo numero: "))

print("Elige una operacion:")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
print("5 - Potencia")
print("6 - Raíz cuadrada")
print("7 - Módulo")
print("8 - Logaritmo")
print("9 - Factorial (del primer numero)")

opcion = input("Ingresa el numero de la operacion: ")

if opcion == '1':
    resultado = numero1 + numero2
    print("La suma es: " + str(resultado))
elif opcion == '2':
    resultado = numero1 - numero2
    print("La resta es: " + str(resultado))
elif opcion == '3':
    resultado = numero1 * numero2
    print("La multiplicación es: " + str(resultado))
elif opcion == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print("La división es: " + str(resultado))
    else:
        print("Error: No se puede dividir entre cero.")
elif opcion == '5':
    resultado = numero1 ** numero2
    print("La potencia es: " + str(resultado))
elif opcion == '6':
    if numero1 >= 0:
        resultado = numero1 ** (1/numero2)
        print("La raíz numero" + str(numero2) + " del primer numero es: " + str(resultado))
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
elif opcion == '7':
    resultado = numero1 % numero2
    print("El módulo es: " + str(resultado))
elif opcion == '8':
    if numero1 > 0:        
        resultado = math.log(numero1)/(math.log(numero2))
        print("El logaritmo base " + str(numero2) + " del primer numero es: " + str(resultado))
    else:
        print("Error: No se puede calcular el logaritmo de un número negativo.")
elif opcion == '9':
    if numero1 < 0 or not numero1.is_integer():
        print("Error: El factorial solo está definido para números enteros no negativos.")
    else:
        resultado = math.factorial(int(numero1))
        print("El factorial del primer numero es: " + str(resultado))



else:
    print("Opción no válida.")
