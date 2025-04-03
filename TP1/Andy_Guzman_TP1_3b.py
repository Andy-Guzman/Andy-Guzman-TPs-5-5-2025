A = "a"

Letra = "ab"

A = str(input("Ingrese una cadena de texto.\n"))
    
while(len(Letra) != 1):

    Letra = str(input("Ingrese un solo caracter/letra.\n"))

    Cantidad = A.upper().count(Letra.upper())

print(f"La letra '{Letra}' ingresada se encontro {Cantidad} de veces.\n")
