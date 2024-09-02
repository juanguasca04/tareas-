# Solicitar al usuario la cantidad de artículos comprados
cantidad_articulos = int(input("Ingrese la cantidad de artículos comprados: "))


precio_unitario_original = float(input("Ingrese el precio unitario original: "))


if cantidad_articulos > 5 and cantidad_articulos < 10:
    descuento = 0.05  
elif cantidad_articulos >= 10:
    descuento = 0.08  
else:
    descuento = 0  


precio_unitario_final = precio_unitario_original * (1 - descuento)


valor_total = precio_unitario_final * cantidad_articulos


print(f"El valor total a pagar es: ${valor_total:}")

print("fin del programa")
