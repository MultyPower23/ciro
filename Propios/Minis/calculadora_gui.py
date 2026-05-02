import tkinter as tk
import math

# ---------- Funciones ----------
def sumar():
    resultado.set(float(entrada1.get()) + float(entrada2.get()))

def restar():
    resultado.set(float(entrada1.get()) - float(entrada2.get()))

def multiplicar():
    resultado.set(float(entrada1.get()) * float(entrada2.get()))

def dividir():
    if float(entrada2.get()) == 0:
        resultado.set("Error")
    else:
        resultado.set(float(entrada1.get()) / float(entrada2.get()))

def potencia():
    resultado.set(float(entrada1.get()) ** float(entrada2.get()))

def raiz_cuadrada():
    if float(entrada1.get()) < 0:
        resultado.set("Error")
    else:
        resultado.set(float(entrada1.get()) ** 0.5)

def logaritmo():
    if float(entrada1.get()) <= 0:
        resultado.set("Error")
    else:
        resultado.set(math.log10(float(entrada1.get())))

def factorial(): 
    num = float(entrada1.get())
    if num < 0 or not num.is_integer():
        resultado.set("Error")
    else:
        resultado.set(math.factorial(int(num)))
def modulo():
    resultado.set(float(entrada1.get()) % float(entrada2.get()))

def raiz_n_esima():
    n = float(entrada2.get())
    if float(entrada1.get()) < 0 and n % 2 == 0:
        resultado.set("Error")
    else:
        resultado.set(float(entrada1.get()) ** (1/n))

def logaritmo_base_n():
    base = float(entrada2.get())
    if float(entrada1.get()) <= 0 or base <= 0 or base == 1:
        resultado.set("Error")
    else:
        resultado.set(math.log(float(entrada1.get())) / math.log(base))

def factorial_n():
    num = float(entrada1.get())
    if num < 0 or not num.is_integer():
        resultado.set("Error")
    else:
        resultado.set(math.factorial(int(num)))

def seno():
    resultado.set(math.sin(float(entrada1.get())))

def coseno():
    resultado.set(math.cos(float(entrada1.get())))

def tangente():
    resultado.set(math.tan(float(entrada1.get())))

# ---------- Ventana ----------
ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("300x600")

# ---------- Variables ----------
resultado = tk.StringVar()

# ---------- Entradas ----------
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

# ---------- Botones ----------
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=2)
tk.Button(ventana, text="Restar", command=restar).pack(pady=2)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=2)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=2)
tk.Button(ventana, text="Potencia", command=potencia).pack(pady=2)
tk.Button(ventana, text="Raíz Cuadrada", command=raiz_cuadrada).pack(pady=2)
tk.Button(ventana, text="Raíz n-ésima", command=raiz_n_esima).pack(pady=2)
tk.Button(ventana, text="Logaritmo Base 10", command=logaritmo).pack(pady=2)
tk.Button(ventana, text="Logaritmo Base n", command=logaritmo_base_n).pack(pady=2)
tk.Button(ventana, text="Módulo", command=modulo).pack(pady=2)
tk.Button(ventana, text="Factorial", command=factorial).pack(pady=2)
tk.Button(ventana, text="Seno", command=seno).pack(pady=2)
tk.Button(ventana, text="Coseno", command=coseno).pack(pady=2)
tk.Button(ventana, text="Tangente", command=tangente).pack(pady=2)
tk.Button(ventana, text="Factorial (n)", command=factorial_n).pack(pady=2)

# ---------- Resultado ----------
tk.Label(ventana, text="Resultado:").pack(pady=5)
tk.Label(ventana, textvariable=resultado).pack()

# ---------- Loop ----------
ventana.mainloop()
