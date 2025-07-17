"""
Define una clase Pago con propiedades de  monto y fecha. Crea clases
derivadas como PagoTarjeta y PagoPayPal,implementando métodos para
procesar pagos, generar recibos y mostrar detalles de pago en la clase base.
"""

class Pago:
    
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha

    def MostrarDetalles(self):

        return f"Monto: ${self.monto:.2f}\nFecha: {self.fecha}\n"

    def ProcesarPago(self):

        return
    
    def GenerarRecibo(self):

        return
    
class PagoTarjeta(Pago):
    
    def __init__(self, monto, fecha):

        super().__init__(monto, fecha)

    def ProcesarPago(self):
        
        return "Pago con tarjeta procesado correctamente.\n"

    def GenerarRecibo(self):
        
        return f"Recibo generado para pago con tarjeta por ${self.monto:} en fecha {self.fecha}.\n"

class PagoPayPal(Pago):
    
    def __init__(self, monto, fecha):
        
        super().__init__(monto, fecha)

    def ProcesarPago(self):
        
        return "Pago con PayPal procesado correctamente.\n"

    def GenerarRecibo(self):
        
        return f"Recibo generado para pago con PayPal por ${self.monto:} en fecha {self.fecha}.\n"

# Prueba del funcionamiento
if __name__ == "__main__":
    PagoTarjeta1 = PagoTarjeta(1500.00, "2025-07-17")
    PagoPaypal1 = PagoPayPal(2200.50, "2025-07-17")

    print("--Pago con Tarjeta\n")
    print(PagoTarjeta1.ProcesarPago())
    print(PagoTarjeta1.GenerarRecibo())
    print(PagoTarjeta1.MostrarDetalles())

    print("--Pago con PayPal\n")
    print(PagoPaypal1.ProcesarPago())
    print(PagoPaypal1.GenerarRecibo())
    print(PagoPaypal1.MostrarDetalles())
