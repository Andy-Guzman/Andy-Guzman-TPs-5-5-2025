"""
Crea una clase llamada Producto que tenga atributos nombre, precio y stock.
Implementa métodos para aumentar y disminuir el stock, asegurándote de que no se pueda tener un stock negativo.
"""


class Producto:
    
    def __init__(self, Nombre, Precio, Stock):
        
        self._Nombre = Nombre
        self._Precio = Precio
        self._Stock = Stock

    def MostrarInformacion(self):
        
        return f"Nombre: {self._Nombre}\nPrecio: {self._Precio}\nStock: {self._Stock}\n"

    def GetNombre(self):

        return self._Nombre

    def GetPrecio(self):

        return self._Precio

    def GetStock(self):

        return self._Stock

    def AumentarStock(self, Más):

        self._Stock = self._Stock + Más
        
        return ""

    def DisminuirStock(self, Menos):

        Menos = Menos * -1

        if (self._Stock + Menos <= -1):

            print(">No hay suficiente stock para restar.")

        else:

            self._Stock = self._Stock + Menos
            
        return ""

      
if __name__ == "__main__":


    Producto1 = Producto("Manzana", 250, 25)

    print(">Stock Inicial: ")

    print(Producto1.MostrarInformacion())

    print(">Stock despues de subir por 25 unidades: ")

    Producto1.AumentarStock(25)

    print(Producto1.MostrarInformacion())

    print(">Stock despues de disminuir por 45 unidades: ")

    Producto1.DisminuirStock(45)

    print(Producto1.MostrarInformacion())

    print(">Stock despues de intentar disminuir por 6 unidades: ")

    Producto1.DisminuirStock(6)

    print(Producto1.MostrarInformacion())
    
    


    
