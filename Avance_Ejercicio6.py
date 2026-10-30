print ("\n★★★ Dayana Regina Cruz López.    Matrícula: AL07282883")

print ("★★★ Ejercicio 6 META DE AHORRO ★★★")

producto = input("¿Qué quieres comprar? ")
precio = float(input("¿Cuánto cuesta? "))
ahorrado = float(input("¿Cuánto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuánto ahorras por semana? "))

if ahorrado >= precio:
    print ("¡Ya puedes comprar tu", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal
    print ("Te falta $", faltante, "para", producto, sep="")
    print ("Ahorrando $", ahorro_semanal, "por semana, lo tendrás en", semanas, "semanas", sep="")
    print ("\n")