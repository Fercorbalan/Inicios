# Determinar la solución lógica de la siguiente operación

print ("De la siguiente expresión logica, ingrese los valores de las variables A y B")

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print(f"el valor de la expresión da como resultado {resultado}")