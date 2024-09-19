# Ordenar una tupla de tuplas por el segundo elemento
# Dado:
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))​
# Salida esperada:
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple2 = sorted(tuple1, key=lambda x: x[1])

print(tuple2)