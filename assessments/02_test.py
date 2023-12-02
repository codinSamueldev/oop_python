class Animal:
    def comer(self):
        return "\nComer"

class Mamifero(Animal):
    def amamantar(self):
        return "\nAmamantar"

class Ave:
    def volar(self):
        return "\nVolar"
    
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

print(murcielago.amamantar(), murcielago.volar(), Murcielago.comer(murcielago))
#print(Murcielago.mro())