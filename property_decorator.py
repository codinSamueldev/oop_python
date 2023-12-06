class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    # Modify attribute's value.
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


alberto = Persona("Alberto", 21)

#Getter
nombre = alberto.nombre
print(nombre)

""" 
@property already understood that name it is a getter, so if we try to modify its return will output error.

alberto.nombre = "Alpaca"
"""
#Setter
alberto.nombre = "Alpaca"
nombre = alberto.nombre
print(nombre)


#Deleter
#del alberto.nombre
nombre = alberto.nombre
print(nombre)