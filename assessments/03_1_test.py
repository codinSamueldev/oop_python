from abc import ABC, abstractclassmethod

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
    

class Strength(Fighter):
    def __init__(self, name: str, power: float, technique: str):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    

class Audacious(Fighter):
    def __init__(self, name: str, power: float, technique: str):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    

class Velocity(Fighter):
    def __init__(self, name: str, power: float, technique: str):
        super().__init__(name, power, technique)

    def character_data(self):
        return f"""
            FIGHTER DATA:
            Name -> {self.name}
            Power level -> {self.power}
            Technique -> {self.technique}"""
    

# instance classes

yujiro = Strength("Yujiro Hanma", 84.7, "Strength")
freezer = Velocity("Freezer", 80.2, "Velocity")
genos = Velocity("Genos-San", 78.9, "Velocity")
batman = Strength("Bruce Wayne", 60.5, "Strength")
invincible = Audacious("Mark Grayson", 79.8, "Audacious")
flash = Audacious("Dick Grayson", 75.6, "Audacious")

yujiman = round(((yujiro.power + batman.power)/2)**2)

print(yujiman)