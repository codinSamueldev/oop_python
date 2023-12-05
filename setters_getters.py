""" 
It is the way we can modify the attribute's values of an object.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        #This a getter
        return self.__nombre
    
    def set_nombre(self, name):
        self.__nombre = name


alberto = Persona("Alberto", 21)

# Create getter.
nombre = alberto.get_nombre()
print(nombre)

# Create setter.
alberto.set_nombre("Alpaca")

# After setting up a new name, we call again the getter.
nombre = alberto.get_nombre()
print(nombre)