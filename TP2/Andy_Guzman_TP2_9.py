"""Crea una clase "Empleado" con propiedades para el nombre, la edad, el salario y el cargo,
y métodos para obtener y establecer estas propiedades,
así como un método para calcular el salario anual."""

class Empleado:

    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def ObtenerNombre(self):
        return self.nombre

    def ObtenerEdad(self):
        return self.edad

    def ObtenerSalario(self):
        return self.salario

    def ObtenerCargo(self):
        return self.cargo

    def EstablecerNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def EstablecerEdad(self, nueva_edad):
        self.edad = nueva_edad

    def EstablecerSalario(self, nuevo_salario):
        self.salario = nuevo_salario

    def EstablecerCargo(self, nuevo_cargo):
        self.cargo = nuevo_cargo
        
    def CalcularSalarioAnual(self):
        return self.salario * 12

if __name__ == "__main__":
    
    empleado = Empleado("Carlos Pérez", 30, 50000, "Analista de Datos")

    print(f"Nombre: {empleado.ObtenerNombre()}\n")
    print(f"Edad: {empleado.ObtenerEdad()}\n")
    print(f"Cargo: {empleado.ObtenerCargo()}\n")
    print(f"Salario mensual: ${empleado.ObtenerSalario()}\n")
    print(f"Salario anual: ${empleado.CalcularSalarioAnual()}\n")



