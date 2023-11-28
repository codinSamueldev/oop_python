""" 
With inheritance we can re-utilize the father class code and also we can add new attributes.

Cookies example: When baking cookies we need to have the ingredients and recipe,
then, let's say I want to bake chocolate cookies, well that is simple just use same ingredients and recipe then add the chocolate.
Or if I want to bake vainilla cookies, use same ingredients and recipe and the vainilla flavour.

In previous example we can grasp the inheritance concept, we use the father class code to create a new class + that extra thing you want to add
"""

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        return "Hola estoy hablando..."

#Inheritance of Persona class.
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #Specify which elements we want to inherit.
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


roberto = Empleado("Roberto", "33", "Peruano", "Ladron", 100000)

#We can inherite methods as well.
print(roberto.hablar())
print(roberto.trabajo)