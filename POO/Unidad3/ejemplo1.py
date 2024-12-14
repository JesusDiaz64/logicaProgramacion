
def dolares_a_pesos(pesos):
    dolares = pesos / 20
    print(f"Este es su cambio a dolares: ${dolares}")

def pesos_a_dolares(dolares):
    pesos = dolares * 20
    print(f"Este es su cambio a pesos: ${pesos}")

while True:
    opcion = input("\nDesea cambiar su dinero?")
    
    if(opcion != "no"):
        opcion2 = int(input("\nQué moneda desea cambiar? (1) Pesos a dolares o (2) Dolares a pesos... "))
        
        if(opcion2 == 1):
            print("\nPesos a dolares.")
            pesos = float(input("\nIngrese su dinero: "))
            dolares_a_pesos(pesos)
        
        elif(opcion2 == 2):
            print("\nDolares a pesos.")
            dolares = float(input("\nIngrese su dinero: "))
            pesos_a_dolares(dolares)
            
        else:
            print("Opción no valida...")
            
    else:
        print("Saliendo del programa!")
        break