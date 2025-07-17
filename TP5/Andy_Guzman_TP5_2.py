"""Crea una clase Empleado con propiedades nombre, salario y cargo.
Deriva clases como Gerente y EmpleadoTemporal, añadiendo un método en
cada una que calcule el aumento de salario basado en ciertos criterios.
"""

class Empleado:

    def __init__(self, Nombre, Salario, Cargo):
        
        self.Nombre = Nombre
        self.Salario = Salario
        self.Cargo = Cargo

class Gerente(Empleado):
    
    def __init__(self, Nombre, Salario, Cargo):

        super().__init__(Nombre, Salario, Cargo)

    def MostrarInformacion(self):
        
        return f"Nombre: {self.Nombre}\nSalario: {self.Salario}\nCargo: {self.Cargo}\n"

    def CalcularSalario(self, Cantidad):

        Pago = self.Salario * Cantidad

        return f"\nEl salario del Gerente en {Cantidad} meses es de: {Pago}\n"

class EmpleadoTemporal(Empleado):

    def __init__(self, Nombre, Salario, Cargo):

        super().__init__(Nombre, Salario, Cargo)

    def MostrarInformacion(self):
        
        return f"Nombre: {self.Nombre}\nSalario: {self.Salario}\nCargo: {self.Cargo}\n"

    def CalcularSalario(self,Cantidad):

        Pago = self.Salario * Cantidad

        return f"\nEl salario del Empleado Termporal en {Cantidad} de horas es de: {Pago}\n"

    
if __name__ == "__main__":


    Gerente1 = Gerente("Jack", 10000, "Gerente")
    EmpleadoTemporal1 = EmpleadoTemporal("Steve", 5000, "Empleado") 
    
    print(Gerente1.MostrarInformacion())

    print(Gerente1.CalcularSalario(3))

    print(EmpleadoTemporal1.MostrarInformacion())

    print(EmpleadoTemporal1.CalcularSalario(24))
