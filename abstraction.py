""" 
A class that contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation 
By default, Python does not provide abstract classes. 
Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
"""

class Auto:
    def __init__(self):
        self.__estado = "Apagao"

    def encender(self):
        self.__estado = "Encendido"
        return "Ya prendio"
    
    def conducir(self):
        if self.__estado == "Apagao":
            arrancar: str = self.encender()
        return arrancar, "Conduciendo"
    
mazda3 = Auto()

print(mazda3.conducir())