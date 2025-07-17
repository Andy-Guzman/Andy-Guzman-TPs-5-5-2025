"""
Crea una clase base Transporte con propiedades de capacidad y velocidad máxima.
Deriva clases como Avión y Barco, e implementa métodos para calcular el tiempo
de viaje basado en la distancia y la velocidad.
"""

class Transporte:

    def __init__(self, Capacidad, VelocidadMáxima):
        
        self.Capacidad = Capacidad
        self.VelocidadMáxima = VelocidadMáxima

class Avión(Transporte):
    
    def __init__(self, Capacidad, VelocidadMáxima):

        super().__init__(Capacidad, VelocidadMáxima)

    def MostrarInformacion(self):

        return f"\nCapacidad: {self.Capacidad}"

    def CalcularVelocidad(self, Nudos):

        Nudos = Nudos * 1852
        self.VelocidadMáxima = Nudos

        return f"Velocidad Máxima: {self.VelocidadMáxima}km/h\n"

    def Viaje(self, KM):

        T = KM/self.VelocidadMáxima
        T = T*60
        T = round(T)
        
        return f"En un viaje de {KM}km en una velocidad de {self.VelocidadMáxima} el tiempo de viaje va a ser de {T} Minutos"


class Barco(Transporte):

    def __init__(self, Capacidad, VelocidadMáxima):

        super().__init__(Capacidad, VelocidadMáxima)

    def MostrarInformacion(self):

        return f"\nCapacidad: {self.Capacidad}"

    def CalcularVelocidad(self, Nudos):

        Nudos = Nudos * 1852
        self.VelocidadMáxima = Nudos

        return f"Velocidad Máxima: {self.VelocidadMáxima}km/h\n"

    def Viaje(self, M):

        T = M/self.VelocidadMáxima
        T = T*60
        T = round(T)
        
        return f"En un viaje de {M}m en una velocidad de {self.VelocidadMáxima} el tiempo de viaje va a ser de {T} Minutos"


if __name__ == "__main__":


    Avión1 = Avión(500, 0)
    Barco1 = Barco(2300, 0) 
    
    print(Avión1.MostrarInformacion())
    print(Avión1.CalcularVelocidad(1))
    print(Avión1.Viaje(1000))
    
    print(Barco1.MostrarInformacion())
    print(Barco1.CalcularVelocidad(1))
    print(Barco1.Viaje(100))
