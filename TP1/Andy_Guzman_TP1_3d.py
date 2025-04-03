import random

Jugador1 = 0

Jugador2 = 0

Meta = 99

Tiempo = 0

while(Jugador1 <= Meta and Jugador2 <= Meta):

    Tiempo = Tiempo + 1
    
    One = random.randint(1 , 5)

    Two = random.randint(1 , 5)

    if(Jugador1 <= Meta and Jugador2 <= Meta):

        Jugador1 = Jugador1 + One
    
        Jugador2 = Jugador2 + Two

    print("Corredor 1: ", Jugador1,".")
    print("Corredor 2: ", Jugador2,".\n")


if(Jugador1 == Jugador2):

    print(f"Empate. Tiempo de la carrera: {Tiempo} segundos.")
    
elif(Jugador1 >= Jugador2):

    print(f"Gano el corredor 1. Tiempo de la carrera: {Tiempo} segundos.")

else:

    print(f"Gano el corredor 2. Tiempo de la carrera: {Tiempo} segundos.")
