#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid_num = num1 + num2 + num3 - min_num - max_num

ascendente = [min_num, mid_num, max_num]
descendente = [max_num, mid_num, min_num]


print("Números en orden ascendente:", ascendente)
print("Números en orden descendente:", descendente)

print("fin del programa")