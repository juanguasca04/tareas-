# Modificar la tupla
# Dada una tupla anidada. Escribe un programa para modificar el primer elemento (22) de una lista dentro de la siguiente tupla a 222.
# Dado:
# tuple1 = (11, [22, 33], 44, 55)
# Salida esperada:
# tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

lista = list(tuple1)
lista [1][0] = 222

tuple2 = tuple(lista)
print(tuple2)