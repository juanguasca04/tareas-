## Solicitar al usuario que ingrese el valor de la cuenta
monto_cuenta = float(input("Ingrese el valor de la cuenta: "))


if monto_cuenta < 150000:
    metodo_pago = "Pago en efectivo"
elif 150000 <= monto_cuenta <= 300000:
    metodo_pago = "Pago con el celular (dinero electrónico)"
elif 300000 < monto_cuenta <= 600000:
    metodo_pago = "Pago con la tarjeta de débito"
else:
    metodo_pago = "Pago con la tarjeta de crédito"

print("Método de pago sugerido:", metodo_pago)

print("fin del programa")
