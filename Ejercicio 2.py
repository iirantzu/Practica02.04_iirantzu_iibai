#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.

numero1 = float(input("Introduce un número:\n"))
numero2 = float(input("Introduce otro número:\n"))

if numero2 == 0:
    print("No se puede dividir por 0 ¡Error!")

else:
    print(numero1 / numero2)