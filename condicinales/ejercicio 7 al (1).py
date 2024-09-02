

print("\nConversión de Temperaturas")
print("1. Fahrenheit a Celsius")
print("2. Fahrenheit a Kelvin")
print("3. Fahrenheit a Rankine")
print("4. Fahrenheit a Réaumur")
print("5. Celsius a Fahrenheit")
print("6. Celsius a Kelvin")
print("7. Celsius a Rankine")
print("8. Celsius a Réaumur")
print("9. Kelvin a Celsius")
print("10. Kelvin a Fahrenheit")
print("11. Kelvin a Rankine")
print("12. Kelvin a Réaumur")
print("13. Rankine a Celsius")
print("14. Rankine a Fahrenheit")
print("15. Rankine a Kelvin")
print("16. Rankine a Réaumur")
print("17. Réaumur a Celsius")
print("18. Réaumur a Fahrenheit")
print("19. Réaumur a Kelvin")
print("20. Réaumur a Rankine")

opcion = input("Seleccione una opción: ")

if opcion == '1':
    F = float(input("Ingrese la temperatura en Fahrenheit: "))
    C = (F - 32) / 1.8
    print(f"La temperatura en Celsius es: {C}")

elif opcion == '2':
    F = float(input("Ingrese la temperatura en Fahrenheit: "))
    K = (F + 459.67) / 1.8
    print(f"La temperatura en Kelvin es: {K}")

elif opcion == '3':
    F = float(input("Ingrese la temperatura en Fahrenheit: "))
    Ra = F + 459.67
    print(f"La temperatura en Rankine es: {Ra}")

elif opcion == '4':
    F = float(input("Ingrese la temperatura en Fahrenheit: "))
    Re = (F - 32) / 2.25
    print(f"La temperatura en Réaumur es: {Re}")

elif opcion == '5':
    C = float(input("Ingrese la temperatura en Celsius: "))
    F = C * 1.8 + 32
    print(f"La temperatura en Fahrenheit es: {F}")

elif opcion == '6':
    C = float(input("Ingrese la temperatura en Celsius: "))
    K = C + 273.15
    print(f"La temperatura en Kelvin es: {K}")

elif opcion == '7':
    C = float(input("Ingrese la temperatura en Celsius: "))
    Ra = C * 1.8 + 32 + 459.67
    print(f"La temperatura en Rankine es: {Ra}")

elif opcion == '8':
    C = float(input("Ingrese la temperatura en Celsius: "))
    Re = C * 0.8
    print(f"La temperatura en Réaumur es: {Re}")

elif opcion == '9':
    K = float(input("Ingrese la temperatura en Kelvin: "))
    C = K - 273.15
    print(f"La temperatura en Celsius es: {C}")

elif opcion == '10':
    K = float(input("Ingrese la temperatura en Kelvin: "))
    F = K * 1.8 - 459.67
    print(f"La temperatura en Fahrenheit es: {F}")

elif opcion == '11':
    K = float(input("Ingrese la temperatura en Kelvin: "))
    Ra = K * 1.8
    print(f"La temperatura en Rankine es: {Ra}")

elif opcion == '12':
    K = float(input("Ingrese la temperatura en Kelvin: "))
    Re = (K - 273.15) * 0.8
    print(f"La temperatura en Réaumur es: {Re}")

elif opcion == '13':
    Ra = float(input("Ingrese la temperatura en Rankine: "))
    C = (Ra - 32 - 459.67) / 1.8
    print(f"La temperatura en Celsius es: {C}")

elif opcion == '14':
    Ra = float(input("Ingrese la temperatura en Rankine: "))
    F = Ra - 459.67
    print(f"La temperatura en Fahrenheit es: {F}")

elif opcion == '15':
    Ra = float(input("Ingrese la temperatura en Rankine: "))
    K = Ra / 1.8
    print(f"La temperatura en Kelvin es: {K}")

elif opcion == '16':
    Ra = float(input("Ingrese la temperatura en Rankine: "))
    Re = (Ra - 32 - 459.67) / 2.25
    print(f"La temperatura en Réaumur es: {Re}")

elif opcion == '17':
    Re = float(input("Ingrese la temperatura en Réaumur: "))
    C = Re * 1.25
    print(f"La temperatura en Celsius es: {C}")

elif opcion == '18':
    Re = float(input("Ingrese la temperatura en Réaumur: "))
    F = Re * 2.25 + 32
    print(f"La temperatura en Fahrenheit es: {F}")

elif opcion == '19':
    Re = float(input("Ingrese la temperatura en Réaumur: "))
    K = Re * 1.25 + 273.15
    print(f"La temperatura en Kelvin es: {K}")

elif opcion == '20':
    Re = float(input("Ingrese la temperatura en Réaumur: "))
    Ra = Re * 2.25 + 32 + 459.67
    print(f"La temperatura en Rankine es: {Ra}")

else:
    print("Opción no válida.")

    print("fin del programa")
