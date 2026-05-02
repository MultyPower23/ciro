import tkinter as tk
from tkinter import ttk
import json
from preguntas import preguntas
import random

respuesta_correcta = None

archivo_ranking = "ranking.json"

def guardar_ranking(nombre, area, puntaje):

    try:
        with open(archivo_ranking,"r") as f:
            data=json.load(f)
    except:
        data=[]

    data.append({
        "nombre":nombre,
        "area":area,
        "puntaje":puntaje
    })

    with open(archivo_ranking,"w") as f:
        json.dump(data,f,indent=4)

def mostrar_ranking():

    with open(archivo_ranking,"r") as f:
        data=json.load(f)

    texto="RANKING\n\n"

    for area in preguntas.keys():

        texto+=area+"\n"

        lista=[x for x in data if x["area"]==area]

        lista=sorted(lista,key=lambda x:x["puntaje"],reverse=True)

        for i,r in enumerate(lista[:5]):
            texto+=f"{i+1}. {r['nombre']} - {r['puntaje']}\n"

        texto+="\n"

    ranking_label.config(text=texto)

def iniciar_test():

    global area_actual,pregunta_actual,puntaje,preguntas_area

    area_actual=area_var.get()
    nombre=nombre_entry.get()

    if nombre=="":
        return

    pregunta_actual=0
    puntaje=0

    # copiar preguntas del área
    preguntas_area = preguntas[area_actual].copy()

    # mezclar preguntas
    random.shuffle(preguntas_area)

    mostrar_pregunta()

def mostrar_pregunta():

    global respuesta_correcta

    q = preguntas_area[pregunta_actual]

    pregunta_label.config(text=q["pregunta"])

    # Mezclar opciones
    opciones_mezcladas = list(enumerate(q["opciones"]))
    random.shuffle(opciones_mezcladas)

    for i in range(4):

        indice_original, texto = opciones_mezcladas[i]

        opciones[i].config(text=texto)

        if indice_original == q["respuesta"]:
            respuesta_correcta = i

    progreso["value"] = pregunta_actual

def responder(i):

    global pregunta_actual, puntaje

    if i == respuesta_correcta:
        puntaje += 1

    pregunta_actual += 1

    if pregunta_actual >= len(preguntas_area):

        guardar_ranking(nombre_entry.get(), area_actual, puntaje)

        pregunta_label.config(text=f"Puntaje final: {puntaje}/10")

        for b in opciones:
            b.config(state="disabled")

    else:
        mostrar_pregunta()

root=tk.Tk()
root.title("Evaluación STEM")

nombre_entry=tk.Entry(root)
nombre_entry.pack()

area_var=tk.StringVar()
area_var.set("Ciencia")

menu=ttk.Combobox(root,textvariable=area_var)
menu["values"]=list(preguntas.keys())
menu.pack()

tk.Button(root,text="Comenzar",command=iniciar_test).pack()

pregunta_label=tk.Label(root,text="")
pregunta_label.pack()

opciones = []

for i in range(4):

    b = tk.Button(root, text="", command=lambda i=i: responder(i))
    b.pack()

    opciones.append(b)

progreso = ttk.Progressbar(root, length=200, maximum=10)
progreso.pack()

tk.Button(root,text="Ver Ranking",command=mostrar_ranking).pack()

ranking_label=tk.Label(root,text="")
ranking_label.pack()

root.mainloop()