"""
Crea una clase base llamada Vehiculo con un método virtual mover().
Luego, crea dos clases derivadas: Coche y Bicicleta, que implementen
el método mover() de manera diferente.
"""

class Vehiculo:

    def Mover(self):

        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Coche(Vehiculo):

    def __init__(self, Recorrido):

        self.Recorrido = Recorrido
    
    def Mover(self, Min):

        self.Recorrido = Min * self.Recorrido 

        return f"{self.Recorrido}"

class Bicicleta(Vehiculo):

    def __init__(self, Recorrido):
        

        self.Recorrido = Recorrido
    
    def Mover(self, Min):

        self.Recorrido = Min * self.Recorrido
        
        return f"{self.Recorrido}"

def main():

    Min = 2

    Vehiculos = [Coche(50), Bicicleta(15)]
    
    for Vehiculo in Vehiculos:

        print(f"Km recorrido {Min} minutos por {Vehiculo.__class__.__name__}: {Vehiculo.Mover(Min)}km")

if __name__ == "__main__":

    main()

