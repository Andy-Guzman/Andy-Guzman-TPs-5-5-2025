"""Crea una clase "Estudiante" con propiedades para el nombre,
la edad y la carrera, y métodos para obtener y establecer estas propiedades,
así como un método para calcular la nota media de un conjunto de exámenes."""

class Estudiante:

    def __init__(Self, Edad, Carrera, Nota):

        Self.Edad = Edad
        Self.Carrera = Carrera
        Self.Nota = Nota

    def ObtenerEdad(Self):

        return Self.Edad 

    def ObtenerCarrera(Self):
        
        return Self.Carrera

    def ObtenerNota(Self):

        return Self.Nota


    def EstablecerEdad(Self, E):
        
        A = Self.Edad = E

        return A

    def EstablecerCarrera(Self, C):

        B = Self.Carrera = C

        return B

    def EstablecerNota(Self, N):

        Suma = sum(N)

        Suma = Suma/len(N)

        Nota = Self.Nota = Suma

        return Nota

if __name__ == "__main__":
    
    Figura = Estudiante(0, "Null", 0)

    E = int(input("Establece edad al alumno.\n"))

    Figura.EstablecerEdad(E)
    
    while True:

        C = str(input("Establece carrera al alumno.\n"))

        if not C.isdigit():

            break

    Figura.EstablecerCarrera(C)

    print("Establece notas de examen en numero al alumno(Ingrese un numero menor a 1 para detenerse.).\n")

    Aux = []

    N = 1
    
    while(N >= 1 and N <= 10):

        N = int(input())

        if(N >= 1 and N <= 10):

            Aux.append(N)
        
    Figura.EstablecerNota(Aux)
    
    print(f"Edad: {Figura.ObtenerEdad()}\n")
    print(f"Carrera: {Figura.ObtenerCarrera()}\n")
    print(f"Nota: {Figura.ObtenerNota()}\n")
