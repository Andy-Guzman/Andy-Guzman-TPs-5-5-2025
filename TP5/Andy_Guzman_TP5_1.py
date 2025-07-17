"""Define una clase base llamada Figura con propiedades nombre y color.
Crea las clases derivadas Círculo y Rectángulo que hereden de Figura.
Para cada figura, implementa métodos que calculen su área y perímetro, y un método para imprimir sus detalles.
"""

import math

class Figura:

    def __init__(self, Nombre, Color):
        
        self.Nombre = Nombre
        self.Color = Color

class Círculo(Figura):
    
    def __init__(self, Nombre, Color, Radio, Área, Perímetro):

        Figura.__init__(self, Nombre, Color)
        self.Radio = Radio
        self.Área = Área
        self.Perímetro = Perímetro

    def MostrarInformacion(self):
        
        return f"Nombre: {self.Nombre}\nColor: {self.Color}\nRadio: {self.Radio}\nÁrea: {self.Área}\nPerímetro: {self.Perímetro}\n"


    def SetÁrea(self):

        self.Área = math.pi * (self.Radio ** 2)
        
        return ""

    def SetPerímetro(self):

        self.Perímetro = (2 * math.pi) * self.Radio
        
        return ""

class Rectángulo(Figura):

    def __init__(self, Nombre, Color, Base, Altura, Área, Perímetro):

        super().__init__(Nombre, Color)
        self.Base = Base
        self.Altura = Altura
        self.Área = Área
        self.Perímetro = Perímetro

    def MostrarInformacion(self):
        
        return f"Nombre: {self.Nombre}\nColor: {self.Color}\nBase: {self.Base}\nAltura: {self.Altura}\nÁrea: {self.Área}\nPerímetro: {self.Perímetro}\n"

    def SetÁrea(self):

        self.Área = self.Base * self.Altura

        return ""

    def SetPerímetro(self):

        self.Perímetro = (self.Base * 2) + (self.Altura * 2)

        return ""

if __name__ == "__main__":


    Circulo1 = Círculo("Círculo", "Azul", 8, 0, 0)
    Rectangulo1 = Rectángulo("Rectángulo", "Rojo", 4, 7, 0, 0)

    Circulo1.SetÁrea()
    Circulo1.SetPerímetro()
    
    print(Circulo1.MostrarInformacion())

    Rectangulo1.SetÁrea()
    Rectangulo1.SetPerímetro()
    
    print(Rectangulo1.MostrarInformacion())
