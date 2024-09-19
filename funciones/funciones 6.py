#Escriba una función para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


numero = int(input("Introduce un número entero no negativo: "))


if numero < 0:
    print("El número debe ser no negativo.")
else:
    print(f"El factorial de {numero} es: {factorial(numero)}")
