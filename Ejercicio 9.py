#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

num_filas = int(input("Introduce el número de lineas de la piramide:\n"))

for fila in range(1, num_filas + 1, 2):
    for j in range(fila, 0, -2):
        print(j, end=" ")
    print("")
