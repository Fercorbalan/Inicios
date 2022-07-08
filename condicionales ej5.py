# Hacer un programa que simule un cajero automatico con un saldo inicial de $ 1000 y tendra el siguiente manú de opciones:
# 1.- Ingresar dinero de la cuenta
# 2.- Retirar dinero de la cuenta
# 3.- Mostrar dinero disponible
# 4.- Salir

print("Ingrese su clave: ")
clave = int(input())
nuevaAccion = "Y"

saldoInicial = 1000

if clave == 1836:
    print (f'\n "Ingresar alguna de las opciones"', "\n 1.- Ingresar dinero de la cuenta: ", "\n 2.- Retirar dinero de la cuenta: ", "\n 3.- Mostrar dinero dispunoble: " "\n 4.- Salir")
    print()
    opcion = int(input())
    if opcion == 1:
        deposito = float(input("Ingrese la cantidad de dinero a depositar: "))
        saldoInicial += deposito
        print()
        print (f"Su nuevo saldo es: {saldoInicial}")
    elif opcion == 2:
        extraccion = float(input("indique el dinero que desea retirar: "))
        if extraccion <= saldoInicial:
            saldoInicial -= extraccion
            print()
            print(f"Su nuevo saldo es {saldoInicial}")
        else:
            saldoInicial <= extraccion
            print()
            print("No tiene los fondos para retirar esa cantidad")
    elif opcion == 3:
        print()
        print(f"Su saldo es {saldoInicial}")
    elif opcion == 4:
        print("Gracias por su visita")
    else:
        print("Error se equivoco en su opcion de Menu")
else:
    print("Error - Clave Incorecta")



