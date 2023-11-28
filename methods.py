#With methods we can define object's actions.

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #Creating methods.
    def llamar(self, name):
        #Since it has function syntaxis, we can set parameters.
        self.name = name
        #We can call attributes within a method.
        return "Llamando a " + self.name + f" desde un {self.marca} {self.modelo}"
    
    def colgar(self):
        return "Colgando"

celular1 = Celular("Samsung", "S23", "50mp")
celular2 = Celular("Iphone", "X", "100MP")

print(celular2.llamar("Dalto"))