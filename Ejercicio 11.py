#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última.

palabra = input("Introduce una palabra: ")

for num_letra in range(len(palabra)):
    print(palabra[num_letra])
