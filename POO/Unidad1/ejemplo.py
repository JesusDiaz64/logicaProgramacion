

def numero_Par_Impar():
    num = int(input("Coloque un numero entero: "))
    
    if num % 2 and num > 0: 
        print(f"El número {num} es impar y positivo")
        
    elif num % 2 and num < 0:
        print(f"El número {num} es impar y negativo") 
        
    elif num % 2 == 0 and num > 0:
        print(f"El número {num} es par y positivo")
        
    elif num % 2 == 0 and num < 0:
        print(f"El número {num} es par y negativo")
        
    else:
        print("El numero que introdujo es nulo!")
    
numero_Par_Impar()