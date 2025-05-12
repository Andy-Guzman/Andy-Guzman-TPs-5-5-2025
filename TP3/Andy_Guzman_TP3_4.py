"""
Crea una clase llamada Libro con atributos titulo, autor y año_publicacion.
Implementa un método que devuelva una descripción del libro y otro que verifique
si el libro es considerado un clásico (publicado hace más de 50 años).
"""


class Libro:
    
    def __init__(self, Titulo, Autor, AñoPublicacion):
        self._Titulo = Titulo
        self._Autor = Autor
        self._AñoPublicacion = AñoPublicacion

    def MostrarInformacion(self):
        
        return f"Cuenta Bancaria: {self._Titulo}\nAutor: {self._Autor}\nNumero de Cuenta: {self._AñoPublicacion}\n"

    def GetTitulo(self):

        return self._Titulo

    def GetAutor(self):

        return self._Autor

    def GetAñoPublicacion(self):

        return self._AñoPublicacion

    def NewAñoPublicacion(self, Año):

        self._AñoPublicacion = Año

        return print(f"Cuenta Bancaria: {self._Titulo}\nAutor: {self._Autor}\nNumero de Cuenta: {self._AñoPublicacion}\n")

    def Descripcion(self):

        return print("Harry Potter nunca ha oido hablar de Hogwarts\nhasta que empiezan a caer unas misteriosas cartas\nen el felpudo del número 4 de Privet Drive. Aunque\nsus horripilantes tios se apresuran a confiscar-\nlas, el dia que Harry cumple once años, Rubeus\nHagrid, un hombre gigantesco cuyos ojos brillan\ncomo escarabajos negros, irrumpe con una noticia\nextraordinaria: Harry Potter es un mago, y le han\nconcedido una plaza en el Colegio Hogwarts de\nMagia y Hechiceria. ¡Esta a punto de comenzar una\naventura increible!\n")

    def Verificar(self):

        A =  2025 - self._AñoPublicacion

        if(A >= 50):

            return print("Este libro se considera un clásico.\n")

        else:

            return print("Este libro NO se considera un clásico.\n")
        
if __name__ == "__main__":

    Libro1 = Libro("Harry Potter y la piedra filosofal", "J. K. Rowling", 1997)

    print(Libro1.MostrarInformacion())

    Libro1.Descripcion()

    Libro1.Verificar()

    print("Despues de cambiar la fecha de publicacion:\n")

    Libro1.NewAñoPublicacion(1950)

    Libro1.Verificar()
    
