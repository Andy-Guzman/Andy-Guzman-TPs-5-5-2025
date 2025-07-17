"""
Diseña una jerarquía de clases que incluya Persona y clases derivadas como Estudiante y Profesor.
Implementa métodos para asignar roles y mostrar información específica de cada rol, junto con un
método en la clase base para mostrar información personal.
"""

class Persona:

    def __init__(self, Nombre, Edad, Genero):
        
        self.Nombre = Nombre
        self.Edad = Edad
        self.Genero = Genero

class Estudiante(Persona):
    
    def __init__(self, Nombre, Edad, Genero, AñoEscolar, Rol):

        super().__init__(Nombre, Edad, Genero)

        self.Rol = Rol
        self.AñoEscolar = AñoEscolar



    def MostrarInformacion(self):
        
        return f"\nNombre: {self.Nombre}\nEdad: {self.Edad}\nGenero: {self.Genero}"
    
    def AsignarRol(self, info1, info2):

        self.Rol = info2
        self.AñoEscolar = info1

        return ""
    
    def MostrarRol(self):
        
        return f"Rol: {self.Rol}\nAño Escolar: {self.AñoEscolar}\n"

class Profesor(Persona):

    def __init__(self, Nombre, Edad, Genero, Materia, Rol):

        super().__init__(Nombre, Edad, Genero)

        self.Rol = Rol
        self.Materia = Materia


    def MostrarInformacion(self):
        
        return f"\nNombre: {self.Nombre}\nEdad: {self.Edad}\nGenero: {self.Genero}"

    def AsignarRol(self, info1, info2):

        self.Rol = info2
        self.Materia = info1

        return ""
    
    def MostrarRol(self):
        
        return f"Rol: {self.Rol}\nMateria: {self.Materia}\n"


if __name__ == "__main__":


    Estudiante1 = Estudiante("Pepita", 16, "Femenino", 0, ".")
    Profesor1 = Profesor("Kuan", 25, "Masculino", "", "") 
    
    print(Estudiante1.MostrarInformacion())
    Estudiante1.AsignarRol(4, "Estudiante")
    print(Estudiante1.MostrarRol())

    print(Profesor1.MostrarInformacion())
    Profesor1.AsignarRol("Matematica", "Profesor")
    print(Profesor1.MostrarRol())


