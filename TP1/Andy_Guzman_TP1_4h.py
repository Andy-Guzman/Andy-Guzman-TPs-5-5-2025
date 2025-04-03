import random

def ChooseWord():

    Words = ["python", "aula", "estrella", "entretenimiento", "computacion"]

    return random.choice(Words)

def HideWord(Word):
    
    return ["_" for _ in Word]

def ShowWord(List):

    print(" ".join(List))

def Game():

    Word = ChooseWord()#Agarra una palabra aleatoria en ChooseWords usando random.choice en una lista predefinida de palabras.

    Hidden = HideWord(Word)#Oculta la palabra haciendo que por cada letra en palabra se devuelva "_".

    Tries = 0 #Intentos que le tomo al jugador para adivinar la palabra.
    
    print("Adivina la palabra:\n")
    
    while ("_" in Hidden):

        Repetida = True
        
        while (Repetida == True):

            ShowWord(Hidden)#Muestra la palabra oculta por "_", solo las que aun no se adivinan.

            print("")

            Letter = str(input("Ingresa una letra:\n").lower())

            Tries += 1
            
            if (Letter in Hidden):

                print("Esta letra ya fue ingresada. Intenta con otra.\n")

            else:

                Repetida = False

        if (Letter in Word):

            for I in range(len(Word)):

                if (Word[I] == Letter):

                    Hidden[I] = Letter

        else:

            print("Error. La letra ingresada fue incorrecta.\n")
    
    print(f"Felicidades! Adivinaste la palabra '{Word}' en {Tries} intentos.\n")

Game()
