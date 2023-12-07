""" 
An abstract class can be considered a blueprint for other classes. 
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
We use an abstract class while we are designing large functional units or when we want to provide a common interface for different implementations of a component. 
"""

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, trabajo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.trabajo = trabajo

    #After abstract method is created, we must always implement them in future classes if not will output error.
    @abstractclassmethod
    def trabajar(self):
        pass


    def presentarse(self):
        return f"Holi soy {self.nombre} y tengo {self.edad} años."
    

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)

    def trabajar(self):
        pass

    #Implementation of the abstract method.
    def presentarse(self):
        return f"\nHoli soy {self.nombre} y tengo {self.edad} años. Actualmente estoy trabajando como {self.trabajo}\n"
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, trabajo):
        super().__init__(nombre, edad, sexo, trabajo)

    def trabajar(self):
        pass

    #Implementation of the abstract method.
    def presentarse(self):
        return f"Holi soy {self.nombre} y tengo {self.edad} años. Me encuentro, estudiando para convertirme en {self.trabajo}\n"


alpaca = Estudiante("Alpaca", 14, "M", "Back-end developer")
print(alpaca.presentarse())

alberto = Trabajador("Alberto", 41, "F", "Back-end developer")
print(alberto.presentarse())

