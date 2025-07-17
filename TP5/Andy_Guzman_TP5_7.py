"""
Define una clase Instrumento con propiedades nombre y material.
Crea clases derivadas como Guitarra y Piano, agregando métodos
para tocar notas musicales y un método en la clase base para indicar el tipo de sonido.
"""

class Instrumento:

    def __init__(self, Nombre, Material):
        
        self.Nombre = Nombre
        self.Material = Material

    def DefinirSonido(self, info):

        self.Sonido = info

        return f"Tipo de Sonido: {self.Sonido}\n"

class Guitarra(Instrumento):
    
    def __init__(self, Nombre, Material, Notas, Sonido):

        super().__init__(Nombre, Material)

        self.Notas = Notas
        self.Sonido = Sonido

    def MostrarInformacion(self):

        print(f"\nNombre: {self.Nombre}\nMaterial: {self.Material}")

        return Instrumento.DefinirSonido(self, "Cuerda Pulsada")

    def TocarNota(self, Num):

        return f"{self.Notas[Num]}"

class Piano(Instrumento):

    def __init__(self, Nombre, Material, Notas, Sonido):

        super().__init__(Nombre, Material)

        self.Notas = Notas
        self.Sonido = Sonido

    def MostrarInformacion(self):

        print(f"\nNombre: {self.Nombre}\nMaterial: {self.Material}")

        return Instrumento.DefinirSonido(self, "Cuerda Pulsada")

    def TocarNota(self, Num):

        return f"{self.Notas[Num]}"

Sound1 = ["Clink", "Twang", "Zing"]
Sound2 = ["Plin", "Ploc", "Tic"]

if __name__ == "__main__":


    Guitarra1 = Guitarra("Guitarra", "Madera", Sound1, "???")
    Piano1 = Piano("Piano", "Metal", Sound2, "???") 
    
    print(Guitarra1.MostrarInformacion())
    print(Guitarra1.TocarNota(2), Guitarra1.TocarNota(0), Guitarra1.TocarNota(1))

    print(Piano1.MostrarInformacion())
    print(Piano1.TocarNota(2), Piano1.TocarNota(0), Piano1.TocarNota(1))


