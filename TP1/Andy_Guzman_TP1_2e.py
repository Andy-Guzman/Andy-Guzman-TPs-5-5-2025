A = 0

C = 0

A = int(input("Ingrese un numero.\n"))

for X in range(A):

    B = X + 1

    B_str = str(B)

    B_len = int(len(B_str) - 1)

    if B_str[-1] in ('1', '3', '5', '7', '9'):

        C = C + B

print("Esta es la suma de todos los numeros impares hasta llegar al anterior ingresado por usted: ", C)
