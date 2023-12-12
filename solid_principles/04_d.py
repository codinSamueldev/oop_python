""" 
DIP (Dependency Inversion Principle)
Abstractions should not depend upon details. Details should depend upon abstractions.

The general idea of this principle is as simple as it is important: 
High-level modules which provide complex logic, 
should be easily reusable and unaffected by changes in low-level modules, 
which provide utility features.
"""

# Bad implementation...

""" 
class Diccionario:
    def verificar_palabra(self):
        # Código para verificar palabras
        pass


class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self):
        # Usar diccionario para corregir texto.
        pass 
"""

# Good implementation...

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):

    @abstractmethod
    def verificar_palabra(self, palabra):
        # Codigo para verificar palabra
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Codigo para verificar que palabra se encuentre en el diccionario.
        pass


class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Codigo para corregir texto.
        pass
