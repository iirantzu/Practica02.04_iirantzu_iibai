#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

numero_filas = int(input("Introduce el número de lineas de la piramide:\n"))

for fila in range(1, numero_filas+1):
    for i in range(fila):
        print("*", end=" ")
    print("")
