"""Crea una clase "Coche" con propiFechaFabricaciones para la marca, el modelo y el año de fabricación,
y un método para obtener el número de años que ha pasado desde que se fabricó el coche.
"""

class Coche:

    def __init__(Self, Marca, FechaFabricacion, Modelo):

        Self.Marca = Marca
        Self.FechaFabricacion = FechaFabricacion
        Self.Modelo = Modelo

    def ObtenerMarca(Self):

        return Self.Marca 

    def ObtenerFechaFabricacion(Self):

        Años = 2025 - int(Self.FechaFabricacion)
        
        return Años

    def ObtenerModelo(Self):

        return Self.Modelo

if __name__ == "__main__":
    
    Vehiculo = Coche("Chevrolet", 2020, "Deportivo")

    print(f"Marca: {Vehiculo.ObtenerMarca()}")
    
    print(f"Años desde que se fabricó: {Vehiculo.ObtenerFechaFabricacion()}")

    print(f"Modelo: {Vehiculo.ObtenerModelo()}")
