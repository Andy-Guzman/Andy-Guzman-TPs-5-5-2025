Pro = 1

Con = -1

Num = 0

print("Ingrese un numero NEGATIVO para parar de poner más numeros.\n")

while (Num >= 0):

    Num = int(input("Ingrese un numero POSITIVO.\n"))

    Pro = Pro * Num

    Con = Con + 1

    

if(Con > 0):

    print(f"El producto del numero ingresado es {Pro}")

else:
    
    print("No se ingresaron numeros positivos")
