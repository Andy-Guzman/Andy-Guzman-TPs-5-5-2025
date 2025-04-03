A = 0
Aux = ["A","E","I","O","U","a","e","i","o","u"]
Vocal = False

A = str(input("Ingrese una letra.\n"))

for X in Aux:
    
    if(A == X):

        print("La letra ingresada es una vocal.")
        Vocal = True

if(Vocal == False):

    print("La letra ingresada es una consonante.")
    

