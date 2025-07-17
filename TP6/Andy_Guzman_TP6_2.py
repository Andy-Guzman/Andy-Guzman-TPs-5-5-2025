"""
Define una clase base llamada Animal con un método virtual hacerSonido().
Crea dos clases derivadas: Perro y Gato, que implementen el método hacerSonido()
para devolver "Guau" y "Miau", respectivamente.

"""

class Animal:

    def HacerSonido(self):

        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):

    def __init__(self, Ruido):

        self.Ruido = Ruido
    
    def HacerSonido(self):

        return f"{self.Ruido}"

class Gato(Animal):

    def __init__(self, Ruido):

        self.Ruido = Ruido
    
    def HacerSonido(self):

        return f"{self.Ruido}"

def main():

    Animals = [Perro("Guau"), Gato("Miau")]
    
    for Animal in Animals:

        print(f"Ruido de {Animal.__class__.__name__}: {Animal.HacerSonido():}")

if __name__ == "__main__":

    main()

