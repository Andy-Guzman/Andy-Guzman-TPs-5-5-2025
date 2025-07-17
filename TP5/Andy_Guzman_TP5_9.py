"""
Diseña una jerarquía de clases con Tienda como clase base y TiendaRopa y TiendaElectrónica como clases derivadas.
Agrega métodos para gestionar el Stock (agregar, eliminar) y calcular el total de ventas, y un método en la
clase base para mostrar información general.
"""

class Tienda:

    def __init__(self, Producto, Ventas):
        
        self.Producto = Producto
        self.Ventas = Ventas

    def MostrarInformacion(self):

        return f"\nProducto: {self.Producto}\nVentas: {self.Ventas}\n"

class TiendaRopa(Tienda):
    
    def __init__(self, Producto, Ventas):

        super().__init__(Producto, Ventas) 

    def CambiarInventario(self, S):
        #StockName: 0 = Pantalon, 1 = Camisa, 2 = Campera
        #Stock  : 0 = 75,       1 = 50,     2 = 65
        #Change: '-' = Restar Stock, '+' = Aumentar Stock, '0' = Sin cambios

        Change = False
        X = -1
        Precios = [12000, 30800, 20000]

        print("Elija un producto.")
        for key in self.Producto:

            X = X + 1

            KeyNames = list(self.Producto.keys())
                
            print(f"{X}- {key}(Stock: {self.Producto[key]}) (Precio: {Precios[X]})")

        X = int(input(""))
        S = int(input("Indique cuantos Comprar/Añadir(Numero positivo) o Vender/Eliminar(Numero negativo)\n"))
        
        if (X >= 0 and X <= 2): 

            if (S != 0 and S < self.Producto[KeyNames[X]]):

                self.Producto[KeyNames[X]] = self.Producto[KeyNames[X]] + S

                if(S > 0):

                    Change = True

                    S = S * -1
                
                self.Ventas = self.Ventas + (Precios[X] * S)

            else:

                print("--No hubieron cambios hechos en el stock.")
        else:

            print("--Numero de producto invalido.")

        if(Change == True):
            
            print(f"{Tienda.MostrarInformacion(self)}")

        else:

            self.Ventas = self.Ventas * -1

            print(f"{Tienda.MostrarInformacion(self)}")

        return f""

class TiendaElectrónica(Tienda):

    def __init__(self, Producto, Ventas):

        super().__init__(Producto, Ventas) 

    def CambiarInventario(self, S):
        #StockName: 0 = Laptop, 1 = Celular, 2 = Audiculares
        #Stock  : 0 = 50,       1 = 75,     2 = 25
        #Change: '-' = Restar Stock, '+' = Aumentar Stock, '0' = Sin cambios

        Change = False
        X = -1
        Precios = [272025, 120000, 10000]

        print("Elija un producto.")
        for key in self.Producto:

            X = X + 1

            KeyNames = list(self.Producto.keys())
                
            print(f"{X}- {key}(Stock: {self.Producto[key]}) (Precio: {Precios[X]})")

        X = int(input(""))
        S = int(input("Indique cuantos Comprar/Añadir(Numero positivo) o Vender/Eliminar(Numero negativo)\n"))
        
        if (X >= 0 and X <= 2): 

            if (S != 0 and S < self.Producto[KeyNames[X]]):

                self.Producto[KeyNames[X]] = self.Producto[KeyNames[X]] + S

                if(S > 0):

                    Change = True

                    S = S * -1
                
                self.Ventas = self.Ventas + (Precios[X] * S)

            else:

                print("--No hubieron cambios hechos en el stock.")
        else:

            print("--Numero de producto invalido.")

        if(Change == True):
            
            print(f"{Tienda.MostrarInformacion(self)}")

        else:

            self.Ventas = self.Ventas * -1

            print(f"{Tienda.MostrarInformacion(self)}")

        return f""
    
ProductoR = {"Pantalon": 150, "Camisa": 100, "Campera": 125}
ProductoE = {"Laptop": 50, "Celular": 75, "Audiculares": 25}

if __name__ == "__main__":


    TiendaRopa1 = TiendaRopa(ProductoR, 0)
    TiendaElectrónica1 = TiendaElectrónica(ProductoE, 0) 
    
    print(TiendaRopa1.MostrarInformacion()) 
    print(TiendaRopa1.CambiarInventario(0))
    
    print(TiendaElectrónica1.MostrarInformacion()) 
    print(TiendaElectrónica1.CambiarInventario(0))
