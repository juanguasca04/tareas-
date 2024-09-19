# 12. **Escriba** una función que compruebe si una cadena frase o palabra pasada es palíndromo o no. 
# Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. 
# Por ejemplo: Ana, Anita lava la tina.
def es_palindromo(cadena):
    
    cadena_limpia = ""
    for caracter in cadena:
        if caracter.isalnum():  
            
            if 'A' <= caracter <= 'Z':
                caracter = chr(ord(caracter) + 32)  
            cadena_limpia += caracter


    return cadena_limpia == cadena_limpia[::-1]


cadena = input("Introduce una cadena o frase: ")


if es_palindromo(cadena):
    print(f"'{cadena}' es un palíndromo.")
else:
    print(f"'{cadena}' no es un palíndromo.")
