import random

A = 0

RNG = random.randint(0, 10000)

print(RNG)

while(A != RNG):

    A = int(input("Ingrese un numero para adivinar un numero secreto.\n"))

    if(A < RNG):

        print("El numero ingresado es MENOR al numero secreto.\n")

    elif(A > RNG):

        print("El numero ingresado es MAYOR al numero secreto.\n")

print("Felicidades. Ingresaste el numero correcto.\n")
