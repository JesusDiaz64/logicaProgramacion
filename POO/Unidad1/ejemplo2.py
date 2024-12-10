
def cambio_moneda():
    cambio_Pesos = 21.37
    cambio_Dolares = 20.24
    
    print(f"El tipo de cambio es de {cambio_Pesos}")
    print(f"El tipo de cambio es de {cambio_Dolares}")
    
    euros = float(input("Euros que desea cambiar: "))
    
    pesos = euros * cambio_Pesos
    
    dolares = pesos / cambio_Dolares
    
    print(f"Este es el cambio a Pesos: {pesos}")
    print(f"Este es el cambio a Pesos: {dolares}")
    
cambio_moneda()