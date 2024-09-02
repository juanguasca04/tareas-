# Pedir el nombre y la edad al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


if edad < 0 or edad > 100:
    print("Por favor, ingrese una edad válida.")
else:
    
    if edad >= 18:
        print(f"{nombre}, usted es mayor de edad.")
    else:
        print(f"{nombre}, usted es menor de edad.")

        print("fin del programa")
