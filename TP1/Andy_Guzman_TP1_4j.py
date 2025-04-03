
import random

def ChooseWord():

    Words = ["electricidad", "escuela", "constelacion", "diversion", "maquina"]

    return random.choice(Words)

def HideWord(Word):

    Hidden = ["_" for _ in Word]

    Hidden[0] = Word[0]  # Mostrar la primera letra.

    return Hidden

def ShowWord(List):

    print(" ".join(List))

def Game():
    
    Word = ChooseWord()

    Hidden = HideWord(Word)

    Tries = 0
    
    print("Adivina la palabra:\n")
    
    Index = 1  # Comienza a adivinar en la segunda letra.
    
    while ("_" in Hidden):

        Repetir = True

        while (Repetir == True):

            ShowWord(Hidden)

            print("")
            
            Letter = str(input("Ingresa la siguiente letra:\n").lower())

            Tries += 1
            
            if (Hidden.count(Letter) == Word.count(Letter)):

                print("Esta letra ya no tiene más repeticiones. Intenta con otra.\n")

            elif (Letter != Word[Index]):

                print("Error. La letra ingresada no es la correcta en esta posición.\n")
                
            else:

                Repetir = False
        
        Hidden[Index] = Letter

        Index += 1
    
    print(f"Felicidades! Adivinaste la palabra '{Word}' en {Tries} intentos.\n")

Game()
