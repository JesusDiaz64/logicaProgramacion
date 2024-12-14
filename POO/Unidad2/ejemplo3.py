from datetime import datetime

class CuentaBancaria:
    def __init__(self, Numero_Cuenta, Titular_Cuenta, Saldo_Total_Cuenta,
                 Periodo_Cuenta):
        self.Numero_Cuenta = Numero_Cuenta
        self.Titular_Cuenta = Titular_Cuenta
        self.Saldo_Total_Cuenta = Saldo_Total_Cuenta                                            
        self.Periodo_Cuenta = Periodo_Cuenta
        
    def Deposito(self,monto):
        if monto > 0:
            self.Saldo_Total_Cuenta += monto
            return self.Saldo_Total_Cuenta
        else:
            raise ValueError("El monto del depósito debe ser positivo.")
        
    def Retiro(self, monto):
        if 0 < monto <=self.Saldo_Total_Cuenta:
            self.Saldo_Total_Cuenta -= monto
            return self.Saldo_Total_Cuenta
        else:
            raise ValueError("El monto del retiro no es válido o excede el saldo disponible.")
        
    def __str__(self):
        return(f"""
                Cuenta Bancaria: \n
                Número de cuenta: {self.Numero_Cuenta}\n
                Titular: {self.Titular_Cuenta}\n
                Saldo total: ${self.Saldo_Total_Cuenta:.2f}\n
                Periodo de la cuenta: {self.Periodo_Cuenta.strftime("%d/%m/%Y")}
                """)
        
if __name__ == "__main__":
    cuenta = CuentaBancaria(
        Numero_Cuenta = 123456,
        Titular_Cuenta = "Jesus Diaz",
        Saldo_Total_Cuenta = 5000.00,
        Periodo_Cuenta = datetime(2024, 12, 12)
    )
    
    cuenta.Periodo_Cuenta = datetime(2025, 1, 1)
    print(f"""
          {cuenta}
          \n Realizando un depósito de $1500...
          {cuenta.Deposito(1500)}
          \nActualizando el periodo de la cuenta a 01/01/2025...
          {cuenta}
          """)
    
    cuenta.Periodo_Cuenta = datetime(2025, 1, 24)
    print(f"""
          \n Realizando un retiro de $2000...
          {cuenta.Retiro(2000)}
          \n Actualizando el periodo de la cuenta a 24/01/2025...
          {cuenta}
          """)