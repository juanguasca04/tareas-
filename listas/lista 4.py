#Escriba un programa para eliminar duplicados de una lista.


duplicados = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]


lista_original = duplicados[:]


for numero in lista_original:
    while duplicados.count(numero) > 1:
        duplicados.remove(numero)

print("Lista sin duplicados:", duplicados)

