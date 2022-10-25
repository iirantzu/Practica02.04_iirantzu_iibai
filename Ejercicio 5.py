#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un
#nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al
#usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Introduce tu nombre:\n")
sexo = input("Introduce tu sexo(M o H):\n")

if sexo == "M":
    if nombre[0].lower() < "m":
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
else:
    if nombre.lower() > "n":
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")