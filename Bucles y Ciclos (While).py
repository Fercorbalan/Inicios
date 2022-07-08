# Bucles y Ciclos (While)


#Ejemplo matematico
import math

numero = int(input("Digite un numero:  "))

while numero < 0:
    print("Error debe ingresar un numero positivo")
    numero = int(input("Digite un numero:  "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")


#numeros
i = 1
while i < 10:
    print(i)
    i += 1
