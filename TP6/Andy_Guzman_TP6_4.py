"""
Define una clase Pago con propiedades de  monto y fecha. Crea clases
derivadas como PagoTarjeta y PagoPayPal,implementando métodos para
procesar pagos, generar recibos y mostrar detalles de pago en la clase base.
"""

class Empleado:
    def CalcularSalario(self):
        # Método base que será sobrescrito
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class EmpleadoPorHora(Empleado):
    def __init__(self, HorasTrabajadas, PagoPorHora):
        self.HorasTrabajadas = HorasTrabajadas
        self.PagoPorHora = PagoPorHora
    
    def CalcularSalario(self):
        return self.HorasTrabajadas * self.PagoPorHora

class EmpleadoFijo(Empleado):
    def __init__(self, SalarioMensual):
        self.SalarioMensual = SalarioMensual
    
    def CalcularSalario(self):
        return self.SalarioMensual

def main():
    empleados = [
        EmpleadoPorHora(40, 250),
        EmpleadoFijo(50000)
    ]
    
    for empleado in empleados:
        print(f"Salario de {empleado.__class__.__name__}: {empleado.CalcularSalario()}")

if __name__ == "__main__":
    
    main()
