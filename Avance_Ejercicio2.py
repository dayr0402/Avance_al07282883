print ("\n★★★ Dayana Regina Cruz López.    Matrícula: AL07282883")

print ("★★★ Ejercicio 2 CREA TU CUENTA ★★★\n")

nombre = input("¿Cuál es tu nombre?")
anio = int(input("¿En qué año naciste?"))
red_social = input("¿Cuál es tu red social favorita?")

edad = 2026 - anio
print (nombre + ",tienes", edad, "años")

if edad >= 13:
    print ("Tu cuenta en", red_social, "fue creada")
else: 
    print ("Todavía no puedes crear tu ceunta, te faltan", 13 - edad, "años")

if edad >= 18:
    print ("Compras dentro de la app activadas\n")
else:
    print ("Compras de la app desactivadas\n")
    