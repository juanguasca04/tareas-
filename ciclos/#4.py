import random

numero_secreto = random.randint(1, 100)
adivinado = False

while not adivinado :
    intento = int(input("adivina el bumero (entre 1 y 100)"))


    if intento < numero_secreto:
        print ("demasiado bajo")
    elif intento > numero_secreto:
        print("demasiado alto")
else:
    print("correcto, adivinaste el numero.")
    adivinado = True