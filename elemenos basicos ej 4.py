# hacer un programa para ingresa el radio de un circulo y se reporte su area y la longitud de la circunferencia

from multiprocessing.spawn import import_main_path

import math

radio = float(input("ingrese el radio para realizar el calculo de area: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area del radio seleccionado es: {area:.2f} y la longitud resultante es {longitud:.2f}")  