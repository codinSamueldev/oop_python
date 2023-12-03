"""  
Other programming languages we can have public, private and protected attributes.
Each type of attribute declared will have a deeper security, meaning...
For public attributes anyone can access it.
For private attributes, we need to declared methods in order to access the value.
And for protected attributes, neither user and programmer can access the value.

In Python, we can give an attribute the protected security, using two under-scores (self.__nameOfTheVariable).
Nevertheless, since we cannot give those kind of security to attributes natively, we can still access them using ._NameOfClass__AttributeOrMethodName
"""

class Clase:
    def __init__(self):
        self._priv = "12345678"
        self.__priv = "contraseña"

    def __methodSecured(self):
        return "Hoy te dedico\nMis mejores pregones..."


test = Clase()

""" The following prints will output attribute's values. """
print(test._priv)
print(test._Clase__priv)
print(test._Clase__methodSecured())

""" The following prints will output error. """
#print(test.__priv)
#print(test.__methodSecured())