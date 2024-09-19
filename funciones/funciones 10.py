#Escriba una función que tome un número como parámetro 
# y verifique que el número sea primo o no. Un número primo (o primo) 
# es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.
def es_primo(numero):
    if numero <= 1:
        return False  
    if numero == 2:
        return True   
    if numero % 2 == 0:
        return False  

    
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True


numero = int(input("Introduce un número entero: "))


if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
