import random

Opciones = ["Piedra", "Papel", "Tijeras"]

RNG = random.randint(1, 3)

A = RNG

print("Piedra, Papel O Tijeras.\n")

while(A == RNG):

    A = int(input("Porfavor elija su jugada ingresando el numero detras del ')'.\n1)Piedra.\n2)Papel.\n3)Tijeras.\nOtro)Rendirse.\n"))

    if (A == RNG):

        print("Es un empate!\n")

        RNG = random.randint(1, 3)
        A = RNG

    elif (A == 1 and RNG == 3):

        print(f"Ganaste!\nEl rival escogio: {Opciones[RNG-1]}.\n")

    elif (A == 2 and RNG == 1):

        print(f"Ganaste!\nEl rival escogio: {Opciones[RNG-1]}.\n")

    elif (A == 3 and RNG == 2):

        print(f"Ganaste!\nEl rival escogio: {Opciones[RNG-1]}.\n")

    elif (A <= 0 or A >= 4):

        print("Te rendiste!")

    else:

        print(f"Perdiste!\nEl rival escogio: {Opciones[RNG-1]}.")
