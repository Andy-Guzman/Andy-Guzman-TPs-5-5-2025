"""
Crea una clase llamada CuentaBancaria que tenga atributos como titular, saldo y numero_cuenta.
Implementa métodos para depositar y retirar dinero, asegurándote de que el saldo no se vuelva negativo.
"""


class CuentaBancaria:
    def __init__(self, Titular, Saldo, NumeroCuenta):
        self._Titular = Titular
        self._Saldo = Saldo
        self._NumeroCuenta = NumeroCuenta

    def MostrarInformacion(self):
        
        return f"Cuenta Bancaria: {self._Titular}\nSaldo: {self._Saldo}\nNumero de Cuenta: {self._NumeroCuenta}\n"

    def MostrarSaldo(self):
        
        return f"Saldo: {self._Saldo}\n"

    def GetTitular(self):

        return self._Titular

    def GetSaldo(self):

        return self._Saldo

    def DepositoRetiro(self, Saldo):

        A = self._Saldo + Saldo
        
        if (A >= 0):

            self._Saldo = A

        else:

            print("Transaccion invalida. No alcanza saldo para retirar.\n")

        return self._Saldo

    def GetNumeroCuenta(self):

        return self._NumeroCuenta

if __name__ == "__main__":

    CuentaBancaria1 = CuentaBancaria("Steve", 25000, 98808845)

    print(CuentaBancaria1.MostrarInformacion())
    
    N = int(input("Ingrese su numero de cuenta antes de hacer cambios.\n"))

    if(N == 98808845):

        while True:
            
            A = int(input("1) Retirar.\n2) Depositar.\nPara salir ingrese algun numero que no corresponda a un comando en pantalla.\n"))

            if(A == 1):

                A = int(input("Ingrese una cantidad para retirar.\n"))

                if (A >= 0):

                    A = A * -1

                    CuentaBancaria1.DepositoRetiro(A)

                else:

                    print("Operacion cancelada.")
                    
            elif(A == 2):

                A = int(input("Ingrese una cantidad para depositar.\n"))

                if (A >= 0):

                    CuentaBancaria1.DepositoRetiro(A)

                else:

                    print("Operacion cancelada.")

            elif(A != 1):

                print("Operacion Terminada.")

                break

            print("Cambios realizados.\n")

            print(CuentaBancaria1.MostrarSaldo())

        
    else:

        print("El numero ingresado fue incorrecto. Intentelo denuevo más tarde.")
