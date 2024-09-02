# Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Comparar los dos números e imprimir el resultado
if num1 > num2:
    print(f"El número mayor es {num1} y el número menor es {num2}.")
elif num1 < num2:
    print(f"El número mayor es {num2} y el número menor es {num1}.")
else:
    print("Ambos números son iguales.")

    print("fin del programa")
