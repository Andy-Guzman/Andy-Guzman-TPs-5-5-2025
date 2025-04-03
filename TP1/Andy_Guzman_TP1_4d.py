List = []

print("Ingrese 5 numeros para ver cual es el promedio final.\n")

for X in range(5):

    A = int(input("Ingrese un numero.\n"))
    List.append(A)

B = 0

for Y in range(5):

    B = B + List[Y]

B = B / len(List)

print(f"Resultado: {B}")
