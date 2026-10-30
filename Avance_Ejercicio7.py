print ("\n★★★ Dayana Regina Cruz López.    Matrícula: AL07282883")

print ("★★★ Ejercicio 7: TIEMPO DE PANTALLA ★★★")

nombre = input("¿Cuál es tu nombre? ")
limite = float(input("¿Cuál es tu limite de horas? "))
horas_redes = float(input("¿Cuántas horas en rede sociales? "))
horas_juegos = float(input("¿Cuántas horas en videojuegos? "))

total = horas_redes + horas_juegos
print (nombre + ",hoy usaste el celular", total, "horas")

if total > limite:
    print ("Pasate", total - limite, "horas de tu limite, ¡es hora de desconectarte!")
else:
    print ("¡Felicidades! Cumpliste tu meta")

if horas_redes > horas_juegos:
    print ("Lo que más usaste fueron las redes sociales\n")
else:
    print ("Lo que más usaste fueron los videojuegos\n")
    