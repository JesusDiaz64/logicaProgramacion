"""

* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

"""

# Funciones aritmeticos

def suma (a = 2, b = 1): 
    return a + b

def resta (a = 2, b = 1):
    return a - b

def multiplicacion (a = 2, b = 1):
    return a * b

def division (a = 4, b = 2):
    return a / b

# Funciones aritmeticos

# Funciones logicos

def logicoAnd (a = 10, b = 2):
    return a < b and b < a

def logicoOr (a = 10, b = 2):
    return a > b or a > 20

def logicoNot (valor = True):
    return valor != valor

# Funciones logicos

# Funciones comparacion

def mayor_que(a = 5, b = 10):
    return a > b

def mayor_o_igual(a = 10, b = 10):
    return a >= b

def menor_que(a = 5, b = 10):
    return a < b

def menor_0_igual(a = 10, b = 5):
    return a <= b

def igualdad(a = 3, b = 3):
    return a == b

def desigualdad(a = 3, b = 3):
    return a != b

# Funciones comparacion

# Condicionales

def condicionales(a = 6, b = 6):
    if (a > b):
        print("a es mayor que b")
    elif a < b:
        print("a es menor que b")
    else:
        print("Los dos numeros son iguales")        

# Condicionales


# Impresiones

print(f""" Impresion de funciones aritmeticas:
      Suma: {suma()}
      Resta: {resta()}      
      Multiplcacion: {multiplicacion()}
      Division: {division()}
      """)

print(f""" Impresion de funciones logicos:
      And: {logicoAnd()}
      Or: {logicoOr()}
      Not: {logicoNot()}
      """)

print(f""" Impresion de funciones de comparacion:
      Mayor que: {mayor_que()}
      Mayor o igual que: {mayor_o_igual()}
      Menor que: {menor_que()}
      Menor o igual que: {menor_0_igual()}
      Igualdad: {igualdad()}
      Desigualdad: {desigualdad()}
      """)

print(condicionales())