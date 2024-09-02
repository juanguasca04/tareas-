# Definir los precios de las pizzas por tamaño
precios_pizza = {
    1: 15000,
    2: 24000,
    3: 36000
}

costo_ingrediente_adicional = 4000

tamaño_pizza = int(input("Ingrese el tamaño de la pizza (1, 2, o 3): "))

ingredientes_adicionales = int(input("Ingrese la cantidad de ingredientes adicionales: "))

precio_total = precios_pizza[tamaño_pizza] + (costo_ingrediente_adicional * ingredientes_adicionales)

print(f"El precio total a pagar es: ${precio_total}")

print("fin del programa")
