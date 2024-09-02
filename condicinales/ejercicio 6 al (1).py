#Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas que se muestran a continuación.

print("\nCálculo de Áreas de Figuras Geométricas")
print("1. Rectángulo")
print("2. Cuadrado")
print("3. Paralelogramo")
print("4. Rombo")
print("5. Trapecio")
print("6. Triángulo")
print("7. Triángulo Equilátero")
print("8. Triángulo Rectángulo")
print("9. Polígono Regular")

opcion = input("Seleccione una opción: ")

if opcion == '1':
    a = int(input("Ingrese la base (a): "))
    b = int(input("Ingrese la altura (b): "))
    area = a * b
    print("El área del rectángulo es:", area)

elif opcion == '2':
    a = int(input("Ingrese el lado (a): "))
    area = a * a
    print("El área del cuadrado es:", area)

elif opcion == '3':
    b = int(input("Ingrese la base (b): "))
    h = int(input("Ingrese la altura (h): "))
    area = b * h
    print("El área del paralelogramo es:", area)

elif opcion == '4':
    d1 = int(input("Ingrese la diagonal mayor (AC): "))
    d2 = int(input("Ingrese la diagonal menor (BD): "))
    area = (d1 * d2) / 2
    print("El área del rombo es:", area)

elif opcion == '5':
    a = int(input("Ingrese la base menor (a): "))
    b = int(input("Ingrese la base mayor (b): "))
    h = int(input("Ingrese la altura (h): "))
    area = ((a + b) / 2) * h
    print("El área del trapecio es:", area)

elif opcion == '6':
    b = int(input("Ingrese la base (b): "))
    h = int(input("Ingrese la altura (h): "))
    area = (b * h) / 2
    print("El área del triángulo es:", area)

elif opcion == '7':
    a = int(input("Ingrese el lado (a): "))
    area = (a * a * (3 ** 0.5)) / 4
    print("El área del triángulo equilátero es:", area)

elif opcion == '8':
    a = int(input("Ingrese el cateto a: "))
    c = int(input("Ingrese el cateto c: "))
    area = (a * c) / 2
    print("El área del triángulo rectángulo es:", area)

elif opcion == '9':
    P = int(input("Ingrese el perímetro (P): "))
    ap = int(input("Ingrese el apotema (ap): "))
    area = (P * ap) / 2
    print("El área del polígono regular es:", area)

else:
    print("Opción no válida.")

    print("fin del programa")
