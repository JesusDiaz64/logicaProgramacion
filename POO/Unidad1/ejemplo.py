

def numero_Par_Impar():
    
    print("Número par o impar sin retornar...")
    num = int(input("Coloque un número entero: "))
    
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

def retorno_Numero_Par_Impar(num):
    
    print("Número par o impar retornar...")
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
    
retorno_Numero_Par_Impar(int(input("Coloque un otro número entero: ")))