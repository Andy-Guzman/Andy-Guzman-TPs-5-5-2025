"""Crea una clase abstracta Figura con un método abstracto calcular_area().
Luego, implementa dos clases concretas, Circulo y Rectangulo, que calculen el área según su propia lógica.
"""

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    
    @abstractmethod
    def CalcularArea(self):

        pass

class Circulo(Figura):
    
    def __init__(self, Radio, Área):
        
        self._Radio = Radio
        self._Área = Área

    def CalcularArea(self):

        self._Área = math.pi * (self._Radio ** 2)

        return f"{self._Área}"
    
class Rectangulo(Figura):
    
    def __init__(self, Base, Altura, Área):
        
        self._Base = Base
        self._Altura = Altura
        self._Área = Área

    def CalcularArea(self):

        self._Área = self._Base * self._Altura

        return f"{self._Área}"


Money = 15200

if __name__ == "__main__":

    Circulo1 = Circulo(8, 0)

    Rectangulo1 = Rectangulo(4, 7, 0)

    print(Circulo1.CalcularArea())

    print(Rectangulo1.CalcularArea())
