#Escriba una clase para implementar pow(x, n).

class Pow:
    def __init__(self, base, exponente):
        self.base=base
        self.exponente = exponente  

    def calcular_potencia(self):
        
        return self.base ** self.exponente



potencia = Pow(2, 3)  

resultado = potencia.calcular_potencia()  

print(f"El resultado de {potencia.base} elevado a {potencia.exponente} es: {resultado}")
