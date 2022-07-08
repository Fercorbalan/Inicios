#Bucles For

for i in [1,5,3,4,5]:
    print(f"Elemento: {i}")
print()

for i in [1,5,3,4,5]:
    print("Hola Mundo")

print()

coleccion = [2,3,10,5,"fernando"]
for i in coleccion:
    print(f"Elemento: {i}")
print()

coleccion = {"Fernando" : 40 , "Cintia" : 38 , "Lucas" : 8}
for i in coleccion:
    print(f"Elemento: {i}")
print()

coleccion = {"Fernando" : 40 , "Cintia" : 38 , "Lucas" : 8}
for i in coleccion:
    print(f"Elemento: {coleccion[i]}")
print()

coleccion = {"Fernando" : 40 , "Cintia" : 38 , "Lucas" : 8}
for i in coleccion:
    print(f"Elemento: {i} -> {coleccion [i]}")

print()
coleccion = {"Fernando" : 40 , "Cintia" : 38 , "Lucas" : 8}
for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")
    
print()
coleccion = "Fernando"
for i in coleccion:
    print(f"{i}")

print()
coleccion = "Fernando"
for i in coleccion:
    print(f"{i}",end=".")

