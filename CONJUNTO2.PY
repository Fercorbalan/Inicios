a = {1,2,3}
b = {3,1,2}
d = {5,6,7}

c = a | b | d # Une conjuntos

c = a & b # muestra valores duplicados en el conjunto

c = a - b # Elementos en "a" y que no estan en el conjunto "b" y viceversa

c = a ^ b # Muestra elementos que no estan repetidos

print(c)

#SUBCONJUNTOS

e = {1,2,3,4,5,6}
f = {2,3,5,6}
print(e.issubset(f))
print(f.issubset(e))

# "f" es un subconjunto de "e"

#conjunto inmutable

e = frozenset ({1,2,3,4,5,6})
f = {2,3,5,6}

print (e)