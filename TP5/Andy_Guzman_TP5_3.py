"""
Diseña una jerarquía de clases de animales, con clases base como Animal y derivadas como Perro y Gato.
Cada clase debe tener un método para emitir su sonido característico.
Agrega un método en la clase base para mostrar detalles generales.
"""

class Animal:

    def __init__(self, Nombre, Sonido):
        
        self.Nombre = Nombre
        self.Sonido = Sonido

class Perro(Animal):
    
    def __init__(self, Nombre, Sonido, Edad, Raza):

        super().__init__(Nombre, Sonido)
        self.Edad = Edad
        self.Raza = Raza

    def MostrarInformacion(self):
        
        return f"\nNombre: {self.Nombre}\nEdad: {self.Edad}\nRaza: {self.Raza}\n"

    def SonidoPerro(self):

        return f"{self.Sonido}\n"

class Gato(Animal):

    def __init__(self, Nombre, Sonido, Edad, Raza):

        super().__init__(Nombre, Sonido)
        self.Edad = Edad
        self.Raza = Raza

    def MostrarInformacion(self):
        
        return f"Nombre: {self.Nombre}\nEdad: {self.Edad}\nRaza: {self.Raza}\n"

    def SonidoGato(self):

        return f"{self.Sonido}\n"

    
if __name__ == "__main__":


    Perro1 = Perro("Perro", "Woof", 5, "Chihuahua")
    Gato1 = Gato("Gato", "Meow", 9, "Birman") 
    
    print(Perro1.MostrarInformacion())

    print(Perro1.SonidoPerro())

    print(Gato1.MostrarInformacion())

    print(Gato1.SonidoGato())
