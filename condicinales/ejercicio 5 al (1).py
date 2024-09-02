# Solicitar cinco (5) notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 
notas = []

print("Ingrese cinco notas (de 0.0 a 5.0):")
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
nota4 = int(input("Ingrese la cuarta nota: "))
nota5 = int(input("Ingrese la quinta nota: "))

# Verificar si las notas están en el rango válido (de 0.0 a 5.0)
if 0.0 <= nota1 <= 5.0 and 0.0 <= nota2 <= 5.0 and 0.0 <= nota3 <= 5.0 and 0.0 <= nota4 <= 5.0 and 0.0 <= nota5 <= 5.0:
    # Calcular el promedio
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

    # Determinar si aprobó o no
    if promedio >= 3.0:
        print(f"Promedio: {promedio:}. Aprobó.")
    else:
        print(f"Promedio: {promedio:}. No aprobó.")
else:
    print("Una o más notas ingresadas no son válidas. Asegúrese de que estén entre 0.0 y 5.0.")

    print("fin del programa")
