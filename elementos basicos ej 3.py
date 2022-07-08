# Ejercicio 3:

from calendar import c
from re import A


print("Hacer un programa para intercambiar el valor de 2 variables.")

a = (input("ingrese el valor de a: "))
b = (input("ingrese el valor de b: "))

print(f"variables ingresadas a = {a}  y b = {b}")

a , b = b , a

print(f"El resultado intercambiado es a = {a} b = {b}")