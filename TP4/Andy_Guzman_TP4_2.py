"""Define una clase abstracta Pago con un método abstracto procesar_pago().
Luego, crea dos clases concretas, TarjetaCredito y PayPal, que implementen el
método procesar_pago() de manera diferente."
"""
from abc import ABC, abstractmethod

class Pago(ABC):
    
    @abstractmethod
    def Procesar_Pago(self):

        pass

class TarjetaCredito(Pago):

    def Procesar_Pago(self, Money):

        return f"\nTransfiriendo {Money} a PayPal.\n\n\n"
    
class PayPal(Pago):

    def Procesar_Pago(self, Money):

        return f"Se a recibido un total de {Money} en su cuenta."


Money = 15200
print(TarjetaCredito().Procesar_Pago(Money))

print(PayPal().Procesar_Pago(Money))
