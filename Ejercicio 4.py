#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
#iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su
#edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Intruduce la edad del usuario: "))
ingresos = float(input("Introduce los ingresos mensuales: "))

if edad > 16 and ingresos >= 1000.0:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
