"""
SRP (Single Responsability Principle)
A class should have one and only one reason to change, 
meaning that a class should have only one job.
"""

class Auto:
    def __init__(self, fuel):
        self.position = 0
        self.fuel = fuel

    
    def move(self, distancia):
        if self.fuel.get_gas() >= distancia / 2:
            self.position += distancia
            self.fuel.use_gas(distancia / 2)
            return f"El carro se ha movido {self.position} km"
        else:
            return "Mani se acabo la gasolina"

    
    def get_car_position(self):
        return self.position


class FuelTank:
    def __init__(self):
        self.gas = 100

    
    def use_gas(self, cantidad):
        self.gas -= cantidad


    def fill_up(self, cantidad):
        self.gas += cantidad


    def get_gas(self):
        return self.gas 
    

fuel_tank = FuelTank()
tesla = Auto(fuel_tank)

print(tesla.fuel.get_gas())
print(tesla.move(10))
print(tesla.fuel.get_gas())
print(tesla.move(20))
print(tesla.fuel.get_gas())
print(tesla.move(30))
print(tesla.fuel.get_gas())
print(tesla.move(60))
print(tesla.fuel.get_gas())
print(tesla.move(90))
print(tesla.fuel.get_gas())