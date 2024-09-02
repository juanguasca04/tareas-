# Solicitar al usuario que ingrese el número de llantas compradas
numero_llantas = int(input("Ingrese el número de llantas compradas: "))


if numero_llantas < 6:
    precio_unitario = 240000
elif 6 <= numero_llantas <= 7:
    precio_unitario = 221000
else:
    precio_unitario = 180000


valor_total = numero_llantas * precio_unitario


print(f"El valor total a pagar es: ${valor_total}")

print("fin del programa")
