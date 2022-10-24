#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.

numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))

if numero2 == 0:
    print("¡ERROR! No se puede dividir por 0")

else:
    print(numero1 / numero2)