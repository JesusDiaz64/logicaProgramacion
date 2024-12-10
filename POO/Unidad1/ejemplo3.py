import math

def formula_general(a, b, c):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    
    x = b * b - 4 * a * c

    if x < 0:
        print("No hay solución")
        
    else:
        resultado_positivo = (-b + math.sqrt(x)) / 2 * a
        resultado_negativo = (-b - math.sqrt(x)) / 2 * a
        
        return(print(f""" Formula general
                     X1 = {resultado_positivo}
                     X2 = {resultado_negativo}
                     """))

print(formula_general(4, 8, 2))