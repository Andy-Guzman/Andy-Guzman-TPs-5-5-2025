"""Crea una clase "Persona" con propiedades para el nombre, la edad y la altura,
y métodos para obtener y establecer estas propiedades.
"""

class Persona:

    def __init__(Self, Nombre, Edad, Altura):

        Self.Nombre = Nombre
        Self.Edad = Edad
        Self.Altura = Altura

    def ObtenerNombre(Self):

        return Self.Nombre

    def EstablecerNombre(Self, Nombre):

        Self.Nombre = Nombre

    def ObtenerEdad(Self):
        
        return Self.Edad

    def EstablecerEdad(Self, Edad):
        
        Self.Edad = Edad

    def ObtenerAltura(Self):

        return Self.Altura

    def EstablecerAltura(Self, Altura):

        Self.Altura = Altura

if __name__ == "__main__":
    
    Persona1 = Persona("Juan", 30, 1.75)

    print(f"Nombre: {Persona1.ObtenerNombre()}")

    print(f"Edad: {Persona1.ObtenerEdad()}")

    print(f"Altura: {Persona1.ObtenerAltura()} m")

    Persona1.EstablecerNombre("Carlos")

    Persona1.EstablecerEdad(31)

    Persona1.EstablecerAltura(1.80)

    print("\nDespués de actualizar:")

    print(f"Nombre: {Persona1.ObtenerNombre()}")

    print(f"Edad: {Persona1.ObtenerEdad()}")

    print(f"Altura: {Persona1.ObtenerAltura()} m")
