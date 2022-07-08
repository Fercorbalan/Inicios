# DICCIONARIOS

diccionario = {"azul": "blue" , "rojo" : "red" , "verde" : "Green"}

diccionario ["amarillo"] = "yellow"

diccionario ["AMARILLO"] = "YELLOW"
print (diccionario["amarillo"])


del(diccionario["rojo"])
print (diccionario)

diccionario2 = {"Fernando" : {"edad" : 40, "estatura" : 1.70}, "Lucas" : [8,1.36] , "Cintia" : [37, 1.50]}
print(diccionario2["Fernando"])
