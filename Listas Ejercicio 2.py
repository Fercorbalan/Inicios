# Escriba un programa que tenga dos listas y que a continuación, cree las siguientes listas (en las que no debe haber repeticiones)

from importlib.abc import SourceLoader


lista1 = ("fernando",3,9,"Miguel", "fernando" ,"Corbalan", "Cintia", "Lucas")
lista2 = (1,3,5,"fernando", "Miguel", 7,9)

a = set(lista1)
b  = set(lista2)

union = list(a | b)
soloA = (a - b)
soloB = (b - a)
interseccion = (a & b)

print(f"Elementos de las Listas {union}")
print(f"Elemento de la lista que aparecen en la 1ra pero no en la 2da {soloA}")
print(f"Elemento de la lista que aparecen en la 2da pero no en la 1ra {soloB}")
print(f"Lista de elementos que aparecen en ambas listas {interseccion}")

