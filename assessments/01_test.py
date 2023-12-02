class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def informacion_basica(self):
        return f"""
            INFORMACION BASICA DEL ESTUDIANTE
            Nombre: {self.nombre}
            Edad: {self.edad}"""

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_estudiante(self):
        return f"""
            Grado: {self.grado}\n"""
    

alberto = Estudiante("Alberto Ramiro", 27, "Quinto")

print(alberto.informacion_basica(), alberto.grado_estudiante())