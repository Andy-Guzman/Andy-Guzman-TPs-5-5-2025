"""Crea una clase "Tienda" con propiedades para el nombre de la tienda
y una lista de productos disponibles, y métodos para añadir o eliminar productos
de la lista y para obtener la lista completa de productos."""

class Tienda:

    def __init__(self, Nombre, Productos=None):

        self.Nombre = Nombre

        self.Productos = Productos if Productos is not None else []

    def ObtenerNombre(self):

        return self.Nombre

    def AgregarProducto(self, producto):

        self.Productos.append(producto)

        print(f"Producto '{producto}' agregado.\n")

    def EliminarProducto(self, producto):
        
        if producto in self.Productos:

            self.Productos.remove(producto)

            print(f"Producto '{producto}' eliminado.\n")

        else:

            print(f"El producto '{producto}' no está en la tienda.\n")

    def ObtenerProductos(self):

        return self.Productos

if __name__ == "__main__":
    
    tienda = Tienda("Super Kiosco", ["Galletas", "Jugo", "Caramelos"])

    print(f"Tienda: {tienda.ObtenerNombre()}\n")
    print("Productos actuales:", tienda.ObtenerProductos(),"\n")

    tienda.AgregarProducto("Chicles")
    tienda.EliminarProducto("Jugo")
    tienda.EliminarProducto("Helado")  # No existe

    print("Productos finales:", tienda.ObtenerProductos(),"\n")


