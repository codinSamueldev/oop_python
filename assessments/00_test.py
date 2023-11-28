""" 
a) Create a class called: "Estudiante"
b) class attribute's: Nombre, Edad, Grado
c) Create a method called: estudiar. And will print "El estudiante (nombre) está estudiando"
d) Users must input attributes
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        return f"Estudiante {self.nombre} está estudiando Python"
    
student0 = Estudiante(input("Ingresa tu nombre: ").capitalize(), int(input("Ingresa tu edad: ")), int(input("Ingresa tu grado: ")))

print(f'''
        DATOS ESTUDIANTE\n\n
        El estudiante se llama {student0.nombre}
        Tiene {student0.edad} años
        Y está cursando el grado {student0.grado}
        {student0.estudiar()}
    ''')
#print(f'\n{student0.nombre}\n{student0.edad}\n{student0.grado}\n{student0.estudiar()}')