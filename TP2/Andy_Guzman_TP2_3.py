"""Crea una clase "Producto" con propiedades para el nombre, el precio
y el stock disponible, y métodos para aumentar o disminuir el stock.
"""

class Producto:

    def __init__(Self, Nombre, Precio, Stock):

        Self.Nombre = Nombre
        Self.Precio = Precio
        Self.Stock = Stock

    def ObtenerNombre(Self):

        return Self.Nombre 

    def ObtenerPrecio(Self):
        
        return Self.Precio

    def ObtenerStock(Self):

        return Self.Stock

    def EstablecerStock(Self, Stock):

        Self.Stock = Stock

if __name__ == "__main__":
    
    Item = Producto("Chocolate", 1500, 100)

    for _ in (0, 1):

        print(f"Nombre: {Item.ObtenerNombre()}\n")
    
        print(f"Precio: {Item.ObtenerPrecio()}\n")

        print(f"Stock: {Item.ObtenerStock()}\n")

        Cambio = int(input("Haga un cambio en el Stock del producto(Numeros negativos restan el Stock, Numeros positivos lo aumentan):\n"))

        Cambio = int(Item.ObtenerStock()) + Cambio
    
        Item.EstablecerStock(Cambio)

print(f"Nombre: {Item.ObtenerNombre()}\n")
    
print(f"Precio: {Item.ObtenerPrecio()}\n")

print(f"Stock: {Item.ObtenerStock()}\n")

print("Todos los cambios fueron hechos.\n")


    
