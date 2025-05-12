"""
Crea una clase llamada Persona con atributos nombre, edad y sexo.
Implementa un método que permita cambiar la edad de la persona y otro que muestre la información de la persona.
"""


class Persona:
    def __init__(self, Nombre, Sexo, Edad):
        self._Nombre = Nombre
        self._Sexo = Sexo
        self._Edad = Edad

    def MostrarInformacion(self):
        
        return f"Persona: {self._Nombre}\nSexo: {self._Sexo}\nEdad: {self._Edad}\n"

    def GetNombre(self):

        return self._Nombre

    def GetSexo(self):

        return self._Sexo

    def SetSexo(self, Sexo):

        self._Sexo = Sexo

    def GetEdad(self):

        return self._Edad

    def SetEdad(self, Edad):

        if Edad > 0:

            self._Edad = Edad

        else:

            print("Edad no válido. La Edad debe ser mayor que 0.\n")

if __name__ == "__main__":

    Persona1 = Persona("Steve", "Masculino", 25)

    print(Persona1.MostrarInformacion())
    
    # Cambiar la Edad

    Persona1.SetEdad(26)

    print("Después de cambiar la Edad:\n")

    print(Persona1.MostrarInformacion())
