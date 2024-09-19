#Escriba un programa para invertir una cadena. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"

cadena = list("1234abcd")  
cadena.reverse()          
cadena_revertida = ""      


for caracter in cadena:
    cadena_revertida += caracter

print(cadena_revertida)
