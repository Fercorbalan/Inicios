#Listas 2

lista = [1 , 3 , 4 , 7 , 5]

lista.append(6)
lista.insert(2 , 3)
lista.extend ([ 6, 7 , 8])
lista.append("Alejandro")

print (lista)

lista1 = [1 , 2 , 3 , 4]
lista2 = [5 , 6 , 7]
lista3 = [8 , 9 , 10]

print(lista1 + lista2 + lista3)

print(11 in lista1)

print(lista.index(5))

lista.pop(1)
lista.remove("Alejandro")
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.clear()
print(lista)