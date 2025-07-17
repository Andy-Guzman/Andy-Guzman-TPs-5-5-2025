"""
Crea una clase base llamada Pago con un método virtual procesarPago().
Luego, crea dos clases derivadas: TarjetaCredito y PayPal,
que implementen el método procesarPago() de manera diferente.
"""

class Pago:

    def ProcesarPago(self):

        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class TarjetaCredito(Pago):

    def __init__(self, PagoRecibido):

        self.PagoRecibido = PagoRecibido
    
    def ProcesarPago(self):

        return f"{self.PagoRecibido}"

class PayPal(Pago):

    def __init__(self, PagoRecibido):
        

        self.PagoRecibido = PagoRecibido
    
    def ProcesarPago(self):
        
        return f"{self.PagoRecibido}"

def main():

    Pagos = [TarjetaCredito(1500.00), PayPal(2200.50)]
    
    for Pago in Pagos:

        print(f"Cantidad de pago recibido de {Pago.__class__.__name__}: {Pago.ProcesarPago()}")

if __name__ == "__main__":

    main()

