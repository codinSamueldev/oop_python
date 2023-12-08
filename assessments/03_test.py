# Power level goes from 0 to 101

from abc import ABC, abstractclassmethod

# create fighters
class Fighter(ABC):
    def __init__(self, name: str, power: float, technique: str):
        self.name = name
        self.power = power
        self.technique = technique

    @abstractclassmethod
    def character_data(self):
        pass
    
    def __add__(self, fighter):
        fighters_fusioned = self.power + fighter.power
        technique_fusioned = self.technique + fighter.technique
        return self.__class__(self.name + fighter.name, fighters_fusioned, technique_fusioned)


class YujiroHanma(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""


class Freezer(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    

class Genos(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    

class Batman(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    
    
class Invincible(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""


class Flash(Fighter):
    def __init__(self, name, power, technique):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""


# instance fighters

yujiro = YujiroHanma("Yujiro Hanma", 84.7, "Strength")
freezer = Freezer("Freezer", 80.2, "Manipulation")
genos = Genos("Genos-San", 78.9, "Spirit")
batman = Batman("Bruce Wayne", 60.5, "Audacious")
invincible = Invincible("Mark Grayson", 79.8, "Strength")
flash = Flash("Dick Grayson", 75.6, "Velocity")

yujiman = round(((yujiro.power + batman.power)/2)**2)
flasher = round(((freezer.power + flash.power)/2)**2)
vigenos = invincible + genos

print(f"""
      Yujiro Hanma and Batman had fusioned
      Now their power has increased to {yujiman}!!\n
      
      Freezer and Flash had fusioned
      Now their power has increased to {flasher}!!\n
      {vigenos.character_data()}""")

