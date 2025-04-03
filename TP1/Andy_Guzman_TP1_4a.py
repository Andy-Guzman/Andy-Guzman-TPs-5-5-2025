Arreglo_Array_List = []

B = 0

print("Ingrese 5 numeros para sumar al final.\n")

for X in range(5):

    A = int(input("Ingrese un numero.\n"))
    Arreglo_Array_List.append(A)

for Y in range(5):

    B = B + Arreglo_Array_List[Y]    

print(f"Resultado: {B}")
