"""
LSP (Liskov's Substitution Principle)
every subclass or derived class should be substitutable for their base or parent class.
"""

""" 
class Bird:
    def fly(self):
        return "Flying"
    
class Penguin(Bird):
    def fly(self):
        return "Penguin flying"


def fly_specie(bird = Bird):
    return bird.fly()

print(fly_specie(Penguin())) 
"""

class Bird:
    pass


class BirdWhoCanFly(Bird):
    def fly(self):
        return "Flying"
    

# Objects of subclasses requires to behave in the same way as the objects of the superclass.

class BirdWhoCannotFly(Bird):
    def fly(self):
        return "I cannot fly"
