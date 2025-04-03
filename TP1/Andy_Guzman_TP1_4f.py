import random

List = []

RNG = random.randint(1, 100)

A = -1

print("Adivina un numero aleatorio.\n")

while(A != RNG):

    A = int(input("Ingrese un numero.\n"))

    if(A == RNG):

        print("Felicidades. Adivinaste el numero aleatorio.")

    elif(A < RNG):

        print("El numero ingresado es MAYOR que el numero aleatorio.\n")

    elif(A > RNG):

        print("El numero ingresado es MENOR que el numero aleatorio.\n")
