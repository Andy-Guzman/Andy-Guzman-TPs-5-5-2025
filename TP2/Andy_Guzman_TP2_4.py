"""Crea una clase "Rectángulo" con propiedades para la longitud y la anchura,
y métodos para calcular el área y el perímetro del rectángulo.
"""

class Rectangulo:

    def __init__(Self, Longitud, Anchura, Area, Perimetro):

        Self.Longitud = Longitud
        Self.Anchura = Anchura
        Self.Area = Area
        Self.Perimetro = Perimetro

    def ObtenerLongitud(Self):

        return Self.Longitud 

    def ObtenerAnchura(Self):
        
        return Self.Anchura

    def ObtenerArea(Self):

        return Self.Area

    def EstablecerArea(Self):

        Area = Self.Longitud * Self.Anchura

        return Area

    def ObtenerPerimetro(Self):

        return Self.Perimetro

    def EstablecerPerimetro(Self):

        Perimetro = (Self.Longitud * 2) + (Self.Anchura * 2)

        return Perimetro

if __name__ == "__main__":
    
    Figura = Rectangulo(4, 7, 0, 0)

    print(f"Longitud: {Figura.ObtenerLongitud()}\n")
    
    print(f"Anchura: {Figura.ObtenerAnchura()}\n")

    print(f"Area: {Figura.EstablecerArea()}\n")

    print(f"Perimetro: {Figura.EstablecerPerimetro()}\n")

