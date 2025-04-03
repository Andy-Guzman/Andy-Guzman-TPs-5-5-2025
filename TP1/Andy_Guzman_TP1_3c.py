A = 0

B = 0

print("Ingrese un numero NEGATIVO para parar de poner más numeros.\n")

while(A >= 0):

    A = int(input("Ingrese un numero POSITIVO para sumar al final del proceso.\n"))

    if(A >= 0):

        B = B + A

print(f"Suma de todos los numeros ingresados sin contar el negativo: {B}.")
