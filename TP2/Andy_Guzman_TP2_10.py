"""Crea una clase "Libro" con propiedades para el título, el autor,
el género y el número de páginas, y métodos para obtener y establecer estas propiedades,
así como un método para comprobar si el libro es de ficción o no."""

class Libro:

    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def ObtenerTitulo(self):

        return self.titulo

    def ObtenerAutor(self):

        return self.autor

    def ObtenerGenero(self):

        return self.genero

    def ObtenerPaginas(self):

        return self.paginas

    def EstablecerTitulo(self, nuevo_titulo):

        self.titulo = nuevo_titulo

    def EstablecerAutor(self, nuevo_autor):

        self.autor = nuevo_autor

    def EstablecerGenero(self, nuevo_genero):

        self.genero = nuevo_genero

    def EstablecerPaginas(self, nuevas_paginas):

        self.paginas = nuevas_paginas

    # Método para verificar si es ficción
    def EsFiccion(self):

        generos_ficcion = ["novela", "cuento", "fantasía", "ciencia ficción", "terror", "aventura"]

        return self.genero.lower() in generos_ficcion

if __name__ == "__main__":
    
    libro = Libro("El Hobbit", "J.R.R. Tolkien", "fantasía", 310)

    print(f"Título: {libro.ObtenerTitulo()}\n")
    print(f"Autor: {libro.ObtenerAutor()}\n")
    print(f"Género: {libro.ObtenerGenero()}\n")
    print(f"Páginas: {libro.ObtenerPaginas()}\n")

    if libro.EsFiccion():
        print("Este libro es de ficción.\n")
    else:
        print("Este libro NO es de ficción.\n")
