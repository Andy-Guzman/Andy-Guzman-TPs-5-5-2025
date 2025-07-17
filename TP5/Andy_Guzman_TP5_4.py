"""
Define una clase Vehiculo con propiedades marca, modelo y año.
Crea clases derivadas como Automovil y Motocicleta, incorporando un método para calcular la eficiencia
de combustible y otro para proyectar la cantidad de combustible necesaria para un viaje.
"""

class Vehiculo:

    def __init__(self, Marca, Modelo, Año):
        
        self.Marca = Marca
        self.Modelo = Modelo
        self.Año = Año

class Automovil(Vehiculo):
    
    def __init__(self, Marca, Modelo, Año):

        super().__init__(Marca, Modelo, Año)
        

    def MostrarInformacion(self):
        
        return f"\nMarca: {self.Marca}\nModelo: {self.Modelo}\nAño: {self.Año}\n"

    def EficienciaAutomovil(self, Km, Litros):

        Eficiencia = Km / Litros

        return f"\nLa eficiencia del Automovil es de: {Eficiencia}\n"

    def ViajeAutomovil(self, ViajeRecorrido, Litros):

        NewLitros = Litros * ViajeRecorrido
        
        return f"En un viaje de {ViajeRecorrido} kilometros, la motocicleta utiliza: {NewLitros} litros de combustible"

class Motocicleta(Vehiculo):

    def __init__(self, Marca, Modelo, Año):

        super().__init__(Marca, Modelo, Año)

    def MostrarInformacion(self):
        
        return f"\nMarca: {self.Marca}\nModelo: {self.Modelo}\nAño: {self.Año}\n"

    def EficienciaMotocicleta(self, Km, Litros):

        Eficiencia = Km / Litros

        return f"\nLa eficiencia de la Motocicleta es de:{Eficiencia}\n"

    def ViajeMotocicleta(self, ViajeRecorrido, Litros):

        NewLitros = Litros * ViajeRecorrido

        return f"En un viaje de {ViajeRecorrido} kilometros, la motocicleta utiliza: {NewLitros} litros de combustible"

    
if __name__ == "__main__":


    Automovil1 = Automovil("Chevrolet", "Onix", 2012 )
    Motocicleta1 = Motocicleta("BMW", "R 1300 GS", 2024) 
    
    print(Automovil1.MostrarInformacion())

    print(Automovil1.EficienciaAutomovil(26900, 30))

    print(Automovil1.ViajeAutomovil(2690, 3))

    print(Motocicleta1.MostrarInformacion())

    print(Motocicleta1.EficienciaMotocicleta(26900, 15))

    print(Motocicleta1.ViajeMotocicleta(2690, 15))


