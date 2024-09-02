#Solicitar número al usuario y determinar si es par, impar o es cero. 
n1 = int(input("ingrese un numero:"))

if n1 == 0:
    print("Error: El número no puede ser cero")
else:
    if n1 % 2 != 0:
        print(f"{n1} es impar")
    else:
        print(f"{n1} es par")

print("fin del programa")

