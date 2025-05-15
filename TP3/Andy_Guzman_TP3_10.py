"""
Crea una clase llamada Circulo que tenga un atributo radio.
Implementa métodos para calcular el área y la circunferencia del círculo, y
asegúrate de que el radio no pueda ser negativo.
"""

import math

class Circulo:
    
    def __init__(self, Radio, Área, Circunferencia):
        
        self._Radio = Radio
        self._Área = Área
        self._Circunferencia = Circunferencia

    def MostrarInformacion(self):
        
        return f"Radio: {self._Radio}\nÁrea: {self._Área}\nCircunferencia: {self._Circunferencia}\n"

    def GetRadio(self):

        return self._Radio

    def GetÁrea(self):

        return self._Área

    def GetCircunferencia(self):

        return self._Circunferencia

    def SetÁrea(self):

        self._Área = math.pi * (self._Radio ** 2)
        
        return ""

    def SetCircunferencia(self):

        self._Circunferencia = 2 * math.pi * self._Radio

        return ""

      
if __name__ == "__main__":


    Circulo1 = Circulo(8, 0, 0)

    print(Circulo1.MostrarInformacion())

    Circulo1.SetÁrea()

    Circulo1.SetCircunferencia()

    print(Circulo1.MostrarInformacion())
    
