class Celular:
    #self = constructor;
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        pass

celular1 = Celular("Samsung", "S23", "50mp")
#We can change the object to a dictionary.
celular2 = Celular("Apple", "X", "100MP").__dict__

print(type(celular1.marca)) 
print(celular1.modelo)
print(celular1.camara)

print("\n", celular2)
print(celular2.keys())
print(type(celular2))