

# COndicionales combinados

edad = int(input("Digite su edad: "))

if edad>0 and edad<100: # tambien funciona "if 0<edad<100:"
    print("Edad Correcta")
    if edad>=18:
        print("es mayor de edad")
    elif edad<18:
        print("es menor de edad")
else:
    print("edad incorrecta")
