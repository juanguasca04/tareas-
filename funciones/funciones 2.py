# Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 
def area_circulo(radio):
    return 3.1416 * radio**2


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_rectangulo(base, altura):
    return base * altura


def area_cuadrado(lado):
    return lado**2


def menu():
    print("Seleccione una figura para calcular su area:")
    print("1. Circulo")
    print("2. Tringulo")
    print("3. Rectangulo")
    print("4. Cuadrado")


menu()
opcion = int(input("Introduce el numero de la opcion: "))

if opcion == 1:
    radio = float(input("Introduce el radio del circulo: "))
    print(f"El area del circulo es: {area_circulo(radio)}")

elif opcion == 2:
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    print(f"El area del triangulo es: {area_triangulo(base, altura)}")

elif opcion == 3:
    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce la altura del rectangulo: "))
    print(f"El area del rectangulo es: {area_rectangulo(base, altura)}")

elif opcion == 4:
    lado = float(input("Introduce el lado del cuadrado: "))
    print(f"El area del cuadrado es: {area_cuadrado(lado):.2f}")

else:
    print("Opcion no valida")