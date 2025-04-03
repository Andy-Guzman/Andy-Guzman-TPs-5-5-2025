A = 0
Aux = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

A = int(input("Ingrese un numero en el rango de 1 al 7.\n"))

if(A < 1 or A > 7):

    print("Error. El numero ingresado no corresponde a estar en el rango de 1 al 7.")
    
else:
    
    for X in range(8):
    
        if(A == X):

            print("El numero corresponde al dia: ",Aux[X-1],".")

