#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
#que ha cumplido (desde 1 hasta su edad).

anos = int(input("Introduce tu edad:\n"))

for i in range(anos):
    print("Has cumplido " + str(i + 1) + " años")