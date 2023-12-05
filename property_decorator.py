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