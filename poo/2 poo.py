#Escriba una clase llamada Rectangle construida por una longitud y anchura y un método que calculará el área de un rectángulo.

class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud  
        self.anchura = anchura    

    def calcular_area(self):
        
        return self.longitud * self.anchura



rectangulo = Rectangle(5, 3)  
area = rectangulo.calcular_area()  

print(f"El área del rectángulo es: {area}")
