""" 
Python Magic/Dunder methods are the methods starting and ending with double underscores (__). 
They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means “Double Under (Underscores)”. 
"""
class Persona:
    # Constructor method with __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Return code given in a string type.
    def __str__(self):
        return f"Persona(nombre={self.name}, edad={self.age})"
    
    # Seems that __repr__ dunder, can turn a string into a class.
    def __repr__(self):
        return f'Persona("{self.name}", {self.age})'
    
    def __add__(self, otro):
        new_value = self.age + otro.age
        return Persona(self.name + otro.name, new_value)

    
# __str__
alpaca = Persona(" Alpaca Gonzales", 56)
print(alpaca)

# __repr__ 
representation = repr(alpaca)
evaluation = eval(representation)
print(evaluation.age)

#__add__
roberto = Persona(" Roberto Zipaquirá", 36)
andrea = Persona(" Andrea Wacha", 26)
resultado = alpaca + roberto + andrea
print(resultado)
