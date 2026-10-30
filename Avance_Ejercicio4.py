print ("\n★★★ Dayana Regina Cruz López.    Matrícula: AL07282883")

print ("★★★★ Ejercicio 4 MIS ESTADÍSTICAS ★★★")
print ("★★★★ Ejercicio 4 MIS ESTADÍSTICAS ★★★\n")

usuario = input("¿Cuál es tu usuario?")
seguidores = int(input("¿Cuántos seguidores tienes?"))
likes = int(input("¿Cuántos likes tuvo tu último video? "))

if seguidores >= 1000:
    print ("Pueder hacer lives")
else:
    print ("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes > seguidores:
    print ("¡Tu último video se hizo viral!\n")
else:
    print ("Sigue publicando, vas bien\n")