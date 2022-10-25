#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre
#por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase:\n")
letra = input("Introduce una letra:\n")
num_veces = 0
for i in frase:
   if i == letra:
       num_veces += 1
print("La letra " + letra + "aparece %2i veces en la frase '%s'." % (num_veces, frase))
