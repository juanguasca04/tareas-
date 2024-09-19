# Escriba una función que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 
def elementos_unicos(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos


lista_original = [1, 2, 2, 3, 4, 4, 5, 1]


lista_sin_duplicados = elementos_unicos(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista con elementos únicos: {lista_sin_duplicados}")
