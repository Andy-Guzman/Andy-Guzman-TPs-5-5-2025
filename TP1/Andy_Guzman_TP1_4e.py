List = []

C = 0

print("Ingrese 5 numeros para ver cual es el promedio final.\n")

for X in range(5):

    A = int(input("Ingrese un numero.\n"))

    B = str(A)
    
    List.append(B)

for Y in range(5):

    B = List[Y]

    if B[-1] in ('0', '2', '4', '6', '8'):

        print(f"\n--{List[Y]}")
        C = C + 1

print(f"\n--{C} elementos del arreglo son pares.")
