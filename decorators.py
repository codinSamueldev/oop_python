""" 
Decorators allows programmers to modify the behaviour of a function or class. 
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
without permanently modifying it.

"""

""" This is not most useful way to create a decorator, but works
    def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar la función *")
        Execute a function we set up previously as a parameter
        funcion()
        print("Despues de llamar la función +")
    return funcion_modificada

def saludo():
    print("Holii y chaii") """

#The follow code it is the most optimal way to create decorators.
def decorador(funcion):
    funcion()
    def funcion_modificada():
        print("Antes de llamar la función *")
        funcion()
        print("Despues de llamar la función +")
    return funcion_modificada

@decorador
def saludo():
    print("Salute mamuacel!")


if __name__ == "__main__":
    """ 
    salute_modified = decorador(saludo)
    salute_modified() 
    """
    saludo()