"""
Crea una clase Producto con propiedades nombre, precio y fecha de vencimiento.
Deriva clases como ProductoAlimenticio y ProductoElectrónico, y añade métodos
para aplicar descuentos basados en la fecha actual y en ciertas condiciones.
"""

class Producto:

    def __init__(self, Nombre, Precio, FechaDeVencimiento):
        
        self.Nombre = Nombre
        self.Precio = Precio
        self.FechaDeVencimiento = FechaDeVencimiento

class ProductoAlimenticio(Producto):
    
    def __init__(self, Nombre, Precio, FechaDeVencimiento, Descuento):

        super().__init__(Nombre, Precio, FechaDeVencimiento)

        self.Descuento = Descuento

    def MostrarInformacion(self):
        
        return f"\nNombre: {self.Nombre}\nPrecio: {self.Precio}\nFechaDeVencimiento: {self.FechaDeVencimiento}\n"

    def AñadirDescuento (self, Fecha, Desc):

        if(self.FechaDeVencimiento == Fecha):

            self.Descuento = Desc

            self.Precio = self.Precio * ((100 - self.Descuento) / 100)
        
        return f"En el dia de vencimiento la carne se puso en un descuento del {self.Descuento}%\nPrecio: {self.Precio}\nDescuento: {self.Descuento}%"

class ProductoElectrónico(Producto):

    def __init__(self, Nombre, Precio, FechaDeVencimiento, Descuento):

        super().__init__(Nombre, Precio, FechaDeVencimiento)

        self.Descuento = Descuento

    def MostrarInformacion(self):
        
        return f"\nNombre: {self.Nombre}\nPrecio: {self.Precio}\nFechaDeVencimiento: {self.FechaDeVencimiento}\n"

    def AñadirDescuento (self, Fecha, Desc):

        if(Fecha[1] == 5):

            if(Fecha[0] >= 12 and Fecha[0] <= 14):

                self.Descuento = Desc

                self.Precio = self.Precio * ((100 - self.Descuento) / 100)

            else:
            
                return "No hubo ningun descuento para añadir."

        
        return f"En la fecha el producto se puso en un descuento de {self.Descuento}%\nPrecio: {self.Precio}\nDescuento: {self.Descuento}%"


PA = [29, 5, 2025]
PE = [29, 8, 2025]

if __name__ == "__main__":


    ProductoAlimenticio1 = ProductoAlimenticio("Carne", 6000, PA, 0)
    ProductoElectrónico1 = ProductoElectrónico("Computadora", 25000, PE, 0) 
    
    print(ProductoAlimenticio1.MostrarInformacion())
    print(ProductoAlimenticio1.AñadirDescuento([29, 5, 2025], 85))

    print(ProductoElectrónico1.MostrarInformacion())
    print(ProductoElectrónico1.AñadirDescuento([12, 5, 2025], 15))


