#Escriba un programa para obtener el número más pequeño de una lista.

lista = [5, 2, 9, 1, 7, 3]

numero_mas_pequeno = lista[0]


for numero in lista:
    if numero < numero_mas_pequeno:
        numero_mas_pequeno = numero

print("El número más pequeño de la lista es:", numero_mas_pequeno)


