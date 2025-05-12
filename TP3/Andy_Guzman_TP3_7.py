"""
Crea una clase llamada Empleado con atributos nombre, salario y departamento.
Implementa un método que aumente el salario en un porcentaje dado y otro que muestre la información del empleado.
"""


class Empleado:
    
    def __init__(self, Nombre, Salario, Departamento):
        
        self._Nombre = Nombre
        self._Salario = Salario
        self._Departamento = Departamento

    def MostrarInformacion(self):
        
        return f"Nombre: {self._Nombre}\nSalario: {self._Salario}\nDepartamento: {self._Departamento}\n"

    def GetNombre(self):

        return self._Nombre

    def GetSalario(self):

        return self._Salario

    def GetDepartamento(self):

        return self._Departamento

    def GetDepartamento(self):

        return self._Departamento

    def AumentarSalario(self, Porcentaje):

        Porcentaje = Porcentaje/100

        self._Salario = self._Salario + (self._Salario * Porcentaje)
        
        return ""

    def DisminuirSalario(self, Porcentaje):

        Porcentaje = Porcentaje/100

        self._Salario = self._Salario - (self._Salario * Porcentaje)

        return ""

      
if __name__ == "__main__":


    Empleado1 = Empleado("Bob", 25000, "Gestion")

    print(Empleado1.MostrarInformacion())

    print("Salario despues de subir un 25%: ")

    Empleado1.AumentarSalario(25)

    print(Empleado1.MostrarInformacion())

    print("Salario despues de disminuir un 50%: ")

    Empleado1.DisminuirSalario(50)

    print(Empleado1.MostrarInformacion())
    
    
