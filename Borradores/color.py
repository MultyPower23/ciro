from multy_utils.colores import error, alerta
from multy_utils.entradas import *

texto = input("Ingresa un texto para el error: ")

error(texto)

yes = pedir_opcion_texto("Elige: ", ["yes", "not yes", "not"])

print(yes)
error("ciro")

alerta("ciro")
alerta(["ciro", 25])