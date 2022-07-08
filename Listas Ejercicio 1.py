# Listas Ejercicio 1

# Ejercicio 1: Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos, por ultimo mostrar la lista.

lista = [1,2,3,4,3,6,7,7,9,9,1]

#opcion 1
conjunto = set(lista)

lista = list(conjunto)

#opcion 2
lista = list(set(lista)) 

print(lista)

