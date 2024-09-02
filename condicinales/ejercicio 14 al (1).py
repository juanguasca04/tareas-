# Solicitar al usuario el género
genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))


edad = int(input("Ingrese su edad en años: "))

if genero == 1:  # Género femenino
    pulsaciones = (220 - edad) / 10
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones:}")
elif genero == 2:  # Género masculino
    pulsaciones = (210 - edad) / 10
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones:}")
else:
    print("Género no válido. Por favor, ingrese 1 para femenino o 2 para masculino.")

    print("fin del programa")
