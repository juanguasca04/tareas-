
#Escriba una función para comprobar si un número cae en un rango determinado. Defina como parámetros rango de inicio, número y rango final.  
def en_rango(inicio, numero, fin):
    if inicio <= numero <= fin:
        return True
    else:
        return False


inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el final del rango: "))
numero = int(input("Introduce el número a comprobar: "))


if en_rango(inicio, numero, fin):
    print(f"El número {numero} está en el rango de {inicio} a {fin}.")
else:
    print(f"El número {numero} NO está en el rango de {inicio} a {fin}.")
