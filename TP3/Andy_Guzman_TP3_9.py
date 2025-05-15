"""
Crea una clase llamada Juego que tenga atributos nombre, genero y precio.
Implementa un método que muestre la información del juego y otro que
verifique si el juego está en oferta (si el Genero es menor a un valor dado).
"""


class Juego:
    
    def __init__(self, Nombre, Genero, Precio):
        
        self._Nombre = Nombre
        self._Genero = Genero
        self._Precio = Precio
        self._PrecioOriginal = Precio

    def MostrarInformacion(self):
        
        return print(f"Nombre: {self._Nombre}\nGenero: {self._Genero}\nPrecio: {self._Precio}\n")

    def GetNombre(self):

        return self._Nombre

    def GetGenero(self):

        return self._Genero

    def GetPrecio(self):

        return self._Precio

    def DisminuirPrecio(self, Cantidad):

        Cantidad = Cantidad * -1

        self._Precio = self._Precio + Cantidad
        
        return ""

    def VerificarOferta(self):

        if (self._PrecioOriginal == self._Precio):

            return print("\nEl juego no esta en oferta.\n")

        elif (self._PrecioOriginal >= self._Precio):

            return print("\nEl juego esta en oferta.\n")

        else:

            return print("\nEl juego es más caro que antes.\n")
            
        return ""

      
if __name__ == "__main__":


    Juego1 = Juego("Megaman", "Platformer", 1500)

    print(">Precio Inicial: ")

    Juego1.MostrarInformacion()

    print(">Verifica si esta en oferta o no: ")

    Juego1.VerificarOferta()

    print("--------\n\n\n>Disminuye el precio por 500: ")

    Juego1.DisminuirPrecio(500)
    Juego1.MostrarInformacion()

    print(">Verifica si esta en oferta o no: ")

    Juego1.VerificarOferta()


    
    
    
