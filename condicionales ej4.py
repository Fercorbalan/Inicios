# construir un programa que simule el funcionamiento de una calculadora que puede realicar las cuatro operaciones aritmeticas basicas
# suma, resta, multiplicacion, division. El usuario debe especificar la operación con el prier carácter del nombre de la operación.

from ast import Mult
from re import M


print("Ingrese sobre las siguientes opciones la operación a realizar")
print("Suma - 's': ")
print("Resta - 'r': ")
print("Multiplicacion - 'm': ")
print("División - 'd': ")
op = input("Seleccione operación a Realizar: ").lower()

num1 = float(input("Ingrese el 1er Numero a calcular: "))
num2 = float(input("Ingrese el 2do Numero a calcular: "))

if op == "s":
    s = num1 + num2
    print(f"Resultado de la suma es: {s}")
elif op == "r":
    r = num1 - num2
    print(f"El resultado de la resta es: {r}")
elif op == "m" or op == "p":
    mult =  num1 * num2
    print(f"El resultado de la multiplicación es: {mult}")
elif op == "d":
    d = num1 / num2
    print(f"El resultado de la división es: {d}")
else:
    print("La letra ingresada no pertenece a ninguna operación")