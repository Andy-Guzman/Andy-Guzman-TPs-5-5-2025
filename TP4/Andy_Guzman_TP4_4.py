"""
Define una clase abstracta Notificacion con un método abstracto enviar().
Crea dos clases concretas, Email y SMS, que implementen el método enviar() de manera diferente.
"""

from abc import ABC, abstractmethod
import math

class Notificacion(ABC):
    
    @abstractmethod
    def Enviar(self):

        pass

class Email(Notificacion):
    
    def __init__(self, Nombre):
        
        self._Nombre = Nombre

    def Enviar(self):

        Mensaje = input("\nEnvia un mensaje al Email:\n")

        return f"Mensaje enviado desde {self._Nombre}:\n\n{Mensaje}"
    
class SMS(Notificacion):
    
    def __init__(self, Nombre):
        
        self._Nombre = Nombre

    def Enviar(self):

        Mensaje = input("\nEnvia un mensaje al SMS:\n")

        return f"Mensaje enviado desde {self._Nombre}:\n\n{Mensaje}"


Money = 15200

if __name__ == "__main__":

    Email1 = Email("NombreBasico@gmail.com")

    SMS1 = SMS("NombreBasico")

    print(Email1.Enviar())

    print(SMS1.Enviar())
