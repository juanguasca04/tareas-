#Dada una lista de números. Escribe un programa para convertir cada elemento de una lista en su cuadrado.
#  Ejemplo dado: numbers = [1, 2, 3, 4, 5, 6, 7]Resultado esperado: numbers = [1, 4, 9, 16, 25, 36, 49]

numeros= [4,6,8,10,12,14]
cuadrados= []

for numero in numeros:
 cuadrados.append (numero**2)
 
 print("lista en su cuadrado",cuadrados)