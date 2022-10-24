#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

altura = int(input("Por favor ingrese una altura para el triangulo: "))

for pisos in range(1, altura + 1):
    for escalones in range(pisos):
        print("*", end="")
    print("")
