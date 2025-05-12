class Coche:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def mostrar_informacion(self):
        return f"Coche: {self._marca} {self._modelo}, Año: {self._año}"

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_año(self):
        return self._año

    def set_año(self, año):
        if año > 1885:  # El primer coche fue inventado en 1886
            self._año = año
        else:
            print("Año no válido. El año debe ser mayor que 1885.")






# Ejemplo de uso

if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 2020)
    print(coche1.mostrar_informacion())
    
    # Cambiar la marca y el año
    coche1.set_marca("Honda")
    coche1.set_año(2021)
    print("Después de cambiar la marca y el año:")
    print(coche1.mostrar_informacion())
    
    # Intentar establecer un año no válido
    coche1.set_año(1800)  # Esto mostrará un mensaje de error

