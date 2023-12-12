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
    

### 2nd example. ###

class KitchenAppliance:
    def turn_on():
        pass


    def turn_off():
        pass


"""  
Some Kitchen appliances does not require a temperature feature, 
so in order to have every single appliance inherit the correct methods,
we need to create a subclass for appliances that requires set up temperature.
This is aplicable for everything, some objects may have common attributes but not always has every single attribute.
"""

class KitchenApplianceWithTemperature(KitchenAppliance):
    def set_temperature():
        pass


class Toaster(KitchenApplianceWithTemperature):
    def turn_on():
        pass


    def turn_off():
        pass

    def set_temperature():
        pass


class Juicer(KitchenAppliance):
    def turn_on():
        pass

    def turn_off():
        pass


### 3rd Example. ###

class Animal:
    def walk():
        pass

    def run():
        pass

    def procreate():
        pass


class AnimalsWithTwoLegs(Animal):
    def fly():
        pass

class AnimalsWithFourLegs(Animal):
    def crawl():
        pass


class Bird(AnimalsWithTwoLegs):
    def walk():
        pass

    def run():
        pass

    def procreate():
        pass

    def fly():
        pass


class Dog(AnimalsWithFourLegs):
    def walk():
        pass

    def run():
        pass

    def procreate():
        pass

    def crawl():
        pass
