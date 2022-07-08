# Hacer un programa que pida números y determine cuál es el mayor.

num1 = float(input("Ingrese el 1er Numero: "))
num2 = float(input("Ingrese el 2do Numero: "))
num3 = float(input("Ingrese el 3er Numero: "))

if num1 > num2 and num2 > num3:
    print(f"{num1} 1er es el numero mayor")
elif num1 < num2 and num2 > num3:
    print(f"{num2} 2do es numero mayor")
elif num1 < num2 and num2 < num3:
    print(f"{num3} 3er es el numero mayor")
else:
    print ("los 3 numeros son iguales")