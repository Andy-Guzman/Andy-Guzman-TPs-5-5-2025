"""Crea una clase "Banco" con propiedades para el nombre del banco y la tasa de interés,
y métodos para calcular el interés que se obtendría en una cantidad determinada de dinero
y el tiempo que se tardaría en duplicar esa cantidad."""

class Banco:

    def __init__(self, Nombre, TasaInteres):

        self.Nombre = Nombre

        self.TasaInteres = TasaInteres  # En porcentaje

    def ObtenerNombre(self):

        return self.Nombre

    def ObtenerTasa(self):

        return self.TasaInteres

    def CalcularInteres(self, Monto, Años):

        Interes = Monto * (self.TasaInteres / 100) * Años

        return Interes

    def TiempoParaDuplicar(self):

        if self.TasaInteres <= 0:

            return None  # No se puede duplicar si no hay interés

        Tiempo = 72 / self.TasaInteres

        return Tiempo

if __name__ == "__main__":
    
    banco = Banco("Banco Central", 5)

    print(f"Nombre del banco: {banco.ObtenerNombre()}\n")
    print(f"Tasa de interés: {banco.ObtenerTasa()}%\n")

    Interes = banco.CalcularInteres(10000, 3)
    
    print(f"Interés ganado en 3 años con $10000: ${Interes}\n")

    Tiempo = banco.TiempoParaDuplicar()
    
    print(f"Años para duplicar el dinero: {Tiempo}\n")

