# Escriba una función que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 
def contar_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    for caracter in cadena:
        
        if 'A' <= caracter <= 'Z':
            mayusculas += 1
        
        elif 'a' <= caracter <= 'z':
            minusculas += 1

    return mayusculas, minusculas


cadena = input("Introduce una cadena de texto: ")

mayusculas, minusculas = contar_mayusculas_minusculas(cadena)
print(f"Letras mayúsculas: {mayusculas}")
print(f"Letras minúsculas: {minusculas}")
