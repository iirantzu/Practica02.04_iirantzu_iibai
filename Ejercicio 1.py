#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
#minúsculas.

contraseña = "contraseña"

contraseña_usuario = input("Introduce contraseña:\n")

while contraseña_usuario.lower() != contraseña:
   contraseña_usuario = input("La contraseña es ERRONEA, introduce contraseña:\n")
   print("La contraseña es CORRECTA")
