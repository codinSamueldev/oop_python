""" 
Poly = Multiple/Many
Morphism = Forms
In a nutshell, with polymorphism we can tell every object what action should do,
but, the output will be different based on each object I give the action.
Example: I say talk to cats, dogs and camels; even though I gave the same action to each animal, the result will be different.
"""

class Animal:
    pass

class Gato(Animal):
    def sonido(self):
        return "Meow"
    
class Perro(Animal):
    def sonido(self):
        return "Wof"

def hacer_sonido(animal):
    return f"{animal.sonido()}"

gato = Gato()
perro = Perro()

print(gato.sonido())
print(hacer_sonido(gato))
print(perro.sonido())
print(hacer_sonido(perro))

# Homework: Duck typing, Enlaces dinámicos, Enlaces estáticos, Tipo Real, Tipo declarado.