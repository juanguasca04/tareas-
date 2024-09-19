#Escriba una función para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336

def multiplicar_lista(numeros):
    multiplicar= 1
    for numero in numeros:
        multiplicar *= numero
    return multiplicar


lista_muestra = [8, 2, 3, -1, 7]


resultado = multiplicar_lista(lista_muestra)
print(f"Resultado esperado: {resultado}")