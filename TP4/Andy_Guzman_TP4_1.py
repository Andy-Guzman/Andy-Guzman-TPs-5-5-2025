from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def mover(self):

        pass

    @abstractmethod
    def detener(self):

        pass

class Coche(Vehiculo):

    def mover(self):

        return "\nEl coche está en movimiento."

    def detener(self):

        return "El coche se ha detenido.\n"

class Bicicleta(Vehiculo):

    def mover(self):

        return "La bicicleta está en movimiento."
 
    def detener(self):

        return "La bicicleta se ha detenido."

print(Coche().mover())
print(Coche().detener())

print(Bicicleta().detener())
print(Bicicleta().mover())
