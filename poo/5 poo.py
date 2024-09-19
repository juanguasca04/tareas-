#Escriba un clase padre llamada Ave que herede a clases hijas con tipos de aves
# clase padre
class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        return f"{self.nombre} está volando."

    def hacer_sonido(self):
        return f"{self.nombre} está haciendo un sonido."



class Aguila(Ave):
    def volar(self):
        return f"{self.nombre} vuela a grandes alturas."

    def hacer_sonido(self):
        return f"{self.nombre} emite un chillido fuerte."


class Pato(Ave):
    def volar(self):
        return f"{self.nombre} vuela bajo y nada."

    def hacer_sonido(self):
        return f"{self.nombre} hace cuac cuac."


class Paloma(Ave):
    def hacer_sonido(self):
        return f"{self.nombre} arrulla suavemente."



aguila = Aguila("Águila Real")
pato = Pato("Pato Salvaje")
paloma = Paloma("Paloma Blanca")

print(aguila.volar())
print(aguila.hacer_sonido())

print(pato.volar())
print(pato.hacer_sonido())

print(paloma.volar())
print(paloma.hacer_sonido())
