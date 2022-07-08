# Hacer un programa que pida un carácter e indique si es una vocal o no.

vocal = str(input("Ingrese la letra a comprobar: ")).lower() #.uper es para llevarlo a mayuscula

if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print ("la letra ingresada es una vocal") 
else:
    print("La letra ingresada no es una vocal")