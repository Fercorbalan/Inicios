# diccionarios 2

equipo = {10: "Paulo Dybala" , 11: "Duglas Costa", 7 : "Cristiano Ronaldo", 13 : "Fideo Dimaria", 17 : "Sami Kedira"}

print(equipo.get(20,"No existe un jugador con ese dorsal"))

print(equipo.keys())
print(equipo.values())
print(equipo.items())
print(len(equipo))

equipo.clear()

print(equipo)