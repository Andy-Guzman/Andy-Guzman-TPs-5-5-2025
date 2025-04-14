"""Crea una clase "Círculo" con propiedades para el radio y el diámetro,
y métodos para calcular el área y la circunferencia del círculo.
"""

import math

class Circulo:

    def __init__(self, Radio, Diametro, Area, Circunferencia):

        self.Radio = Radio
        self.Diametro = Diametro
        self.Area = Area
        self.Circunferencia = Circunferencia

    def ObtenerRadio(self):
        return self.Radio 

    def ObtenerDiametro(self):
        return self.Diametro

    def ObtenerArea(self):
        return self.Area

    def EstablecerArea(self):
        
        Area = math.pi * (self.Radio ** 2)

        return Area

    def ObtenerCircunferencia(self):

        return self.Circunferencia

    def EstablecerCircunferencia(self):

        Circunferencia = 2 * math.pi * self.Radio

        return Circunferencia

if __name__ == "__main__":
    
    Figura = Circulo(8, 4, 0, 0)

    print(f"Radio: {Figura.ObtenerRadio()}\n")
    
    print(f"Diametro: {Figura.ObtenerDiametro()}\n")

    print(f"Área: {Figura.EstablecerArea():}\n")

    print(f"Circunferencia: {Figura.EstablecerCircunferencia():}\n")
