class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre


alberto = Persona("Alberto", 21)

nombre = alberto.nombre
print(nombre)

""" 
@property already understood that name it is a getter, so if we try to modify its return will output error.

alberto.nombre = "Alpaca"
"""

alberto.__nombre = "Alpaca"
nombre = alberto.__nombre
print(nombre)