"""
Crea una clase llamada Estudiante que tenga atributos como nombre, edad y notas (una lista de números).
Implementa métodos para agregar una nota y calcular el promedio de las notas.
"""


class Estudiante:
    
    def __init__(self, Nombre, Edad, Notas):
        self._Nombre = Nombre
        self._Edad = Edad
        self._Notas = Notas

    def MostrarInformacion(self):
        
        return f"Nombre: {self._Nombre}\nEdad: {self._Edad}\nNotas: {self._Notas}\n"

    def GetNombre(self):

        return self._Nombre

    def GetEdad(self):

        return self._Edad

    def GetNotas(self):

        return self._Notas

    def GetNotas(self):

        return self._Notas

    def NewNotas(self, Lista):

        return self._Notas == Lista

    def Promedio(self):

        Total = sum(self._Notas)

        Total = Total/4

        print(f"Promedio de las notas: ", Total)
        
        return ""
        
if __name__ == "__main__":

    L = [0]*4

    Estudiante1 = Estudiante("Harry Potter", 45, L)

    print(Estudiante1.MostrarInformacion())
    print("Añada 4 notas al estudiante, vaya de una en una, en un rango de 1 hasta el 10.")

    X = -1
    
    while (X != 3):

        X = X + 1
        
        A = int(input("\n>"))

        if (A >= 11 or A <= 0):

            print("La nota debe estar en un rango de 1 hasta 10.")

            X = X - 1

        else:

            L[X] = A

    print(Estudiante1.MostrarInformacion())

    print(Estudiante1.Promedio())
