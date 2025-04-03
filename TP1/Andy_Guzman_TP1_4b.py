List = []

print("Ingrese 5 numeros para ver cual es el mayor al final.\n")

for X in range(5):

    A = int(input("Ingrese un numero.\n"))
    List.append(A)

B = List[0]

for Y in range(5):

    if(List[Y] > B):

        B = List[Y]    

print(f"Resultado: {B}")
