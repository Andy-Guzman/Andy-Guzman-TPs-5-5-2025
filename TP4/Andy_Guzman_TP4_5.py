"""
Crea una clase abstracta Empleado con un método abstracto calcular_sueldo().
Luego, implementa dos clases concretas, EmpleadoPorHora y EmpleadoFijo, que
calculen el sueldo de manera diferente.
"""

from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    
    @abstractmethod
    def CalcularSueldo(self):

        pass

class EmpleadoPorHora(Empleado):
    
    def __init__(self, Nombre, PagoHora):
        
        self._Nombre = Nombre
        self._PagoHora = PagoHora
        

    def CalcularSueldo(self):

        return f"\nEl sueldo del Empleado Por Hora es de: {self._PagoHora}\n"
    
class EmpleadoFijo(Empleado):
    
    def __init__(self, Nombre, PagoMensual):
        
        self._Nombre = Nombre
        self._PagoMensual = PagoMensual

    def CalcularSueldo(self):

        return f"\nEl sueldo del Empleado Fijo es de: {self._PagoMensual} \n"


Money = 15200

if __name__ == "__main__":

    EmpleadoPorHora1 = EmpleadoPorHora("Carlos", 250)

    EmpleadoFijo1 = EmpleadoFijo("Marco", 250000)

    print(EmpleadoPorHora1.CalcularSueldo())

    print(EmpleadoFijo1.CalcularSueldo())
