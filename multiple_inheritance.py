class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        return "Hola estoy hablando..."

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"
    

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #Instead of super(); we need to specify from which classes we want to inherit attributes. Then, we have created a multiple inheritance.
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"Hola soy {self.nombre}, y {super().mostrar_habilidad()}, trabajo en {self.empresa}"
        #return f"Hola soy {self.nombre}, y {self.mostrar_habilidad()}, trabajo en {self.empresa}"
    

roberto = EmpleadoArtista("Roberto", "33", "Peruano", "Pintar", 100000, "Femsa")

#print(f'{roberto.presentarse()}')

#####################################
"""
    Let's say this a module a we need to import it in the main.py script,
    now we need to verify the inheritances of a class, either instances.
    With issubclass() and isinstance() we can check that info.
    issubclass() will only print False if the class to verify has nothing to do with the class given.
"""

#herencia = issubclass(EmpleadoArtista, Persona)
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

#instancia = isinstance(roberto, EmpleadoArtista)
#instancia = isinstance(roberto, Persona)
instancia = isinstance(roberto, Artista)
print(instancia)