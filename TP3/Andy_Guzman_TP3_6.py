"""
Crea una clase llamada Rectangulo que tenga atributos base y altura.
Implementa métodos para calcular el área y el perímetro del rectángulo.
"""


class Rectangulo:
    
    def __init__(self, Base, Altura, Área, Perímetro):
        
        self._Base = Base
        self._Altura = Altura
        self._Área = Área
        self._Perímetro = Perímetro

    def MostrarInformacion(self):
        
        return f"Base: {self._Base}\nAltura: {self._Altura}\nÁrea: {self._Área}\nPerímetro: {self._Perímetro}\n"

    def GetBase(self):

        return self._Base

    def GetAltura(self):

        return self._Altura

    def GetÁrea(self):

        return self._Área

    def GetÁrea(self):

        return self._Área

    def GetPerímetro(self):

        return self._Perímetro

    def NewArea(self):

        self._Área = self._Base * self._Altura

        return ""

    def NewPerimetro(self):

        self._Perímetro = (self._Base * 2) + (self._Altura * 2)

        return ""

        
if __name__ == "__main__":


    Rectangulo1 = Rectangulo(4, 7, 0, 0)

    Rectangulo1.NewArea()

    Rectangulo1.NewPerimetro()

    print(Rectangulo1.MostrarInformacion())

