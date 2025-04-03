import random
import time

Longitud = 5  # Puedes cambiar la cantidad de números

Numeros = [random.randint(0, 9) for _ in range(Longitud)]
    
print("Memoriza estos números:", Numeros)

time.sleep(2)  # Muestra los números por 2 segundos

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  # Agrega múltiples líneas en blanco para "borrar" visualmente ya que la otra manera de borrar la consola
    
R = input(f"Ingresa los {Longitud} números en orden, separados por espacios:\n")

User = list(map(int, R.split()))
    
if (User == Numeros):
    
    print("Felicidades. Los numeros fueron ingresados correctamente.\n")

else:

    print("Incorrecto.\nLos números eran:", Numeros)
