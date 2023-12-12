""" 
ISP (Interface Segregation Principle)
Clients should not be forced to depend upon methods that they do not use. 
Interfaces belong to clients, not to hierarchies.
In other words, if a class does not use particular methods or attributes, 
then those methods and attributes should be segregated into more specific classes.
"""

from abc import ABC, abstractclassmethod

class Camellar(ABC):

    @abstractclassmethod
    def camellar(self):
        pass


class Almorzar(ABC):
    
    @abstractclassmethod
    def almorzar(self):
        pass


class Momir(ABC):

    @abstractclassmethod
    def mimir(self):
        pass


class Camellador(Camellar, Almorzar, Momir):

    def camellar(self):
        return "Humano camellando mijo."

    def almorzar(self):
        return "Ya camellé un rato, humano va a almorzar."
    
    def mimir(self):
        return "Tengo sueño, hora de mimir."


class Estudiante(Almorzar, Momir):
    def almorzar(self):
        return "Ya estudié, hora de almorzar."
    
    def mimir(self):
        return "Toy cansao, hora de mimir."


class Robot(Camellador):
    
    def camellar(self):
        return "\nRobot camellando al sol y al agua."


roberto = Camellador()
samuel = Estudiante()
chatgpt = Robot()

print(roberto.camellar(), roberto.almorzar(), roberto.mimir())
print(chatgpt.camellar())