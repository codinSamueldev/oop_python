"""  
Other programming languages we can have public, private and protected attributes.
Each type of attribute declared will have a deeper security, meaning...
For public attributes anyone can access it.
For private attributes, we need to declared methods in order to access the value.
And for protected attributes, neither user and programmer can access the value.

In Python, we can give an attribute the protected security, using two under-scores (self.__nameOfTheVariable).

"""

class Clase:
    def __init__(self):
        self._priv = "12345678"
        self.__priv = "contraseña"


test = Clase()

print(test._priv)
#This print will output an error.
print(test.__priv)