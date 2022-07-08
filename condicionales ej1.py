# hacer un programa que pida 2 numeros y se de ceunta cual de ellos es par, o si amos lo son

import math

num1 =int(input("Ingrese el 1er Numero: "))
num2 =int(input("Ingrese el 2do Numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos son pares")
elif num1 % 2 == 0 and num2 % 2 !=0:
    print(f"EL 1er numero ({num1}) es par")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"EL 2do numero ({num2}) es par")
else:
    print("Ninguno de los numeros es par")
