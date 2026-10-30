print ("\n★★★ Dayana Regina Cruz López.    Matrícula: AL07282883")

print ("★★★ Ejercicio 3 WI-FI DEL CAFÉ ★★★\n")

contrasena_cafe = "Latte2026"

nombre = input("¿Cuál es tu nombre? ")
contrasena = input("Escribe la contraseña: ")
gasto = float(input("¿Cuánto gastaste?"))

if contrasena == contrasena_cafe:
    print ("Conectado a Wi-Fi, bienvenido/a", nombre)
else:
    print ("Contraseña incorrecta")

if gasto >= 100:
    print("Tienes 1 hora de Wi-Fi\n")
else:
    print ("Tienes 30 minutos de Wi-Fi\n")
