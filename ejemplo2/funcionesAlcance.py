"""
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# Simple

def saludo():
    print("Hola Mundo!")
    
saludo()

# Simple

# Con retorno

def saludo_retorno():
    return "Hola, retorno"

print(saludo_retorno())

# Con retorno

# Con argumento

def saludo_argumento(saludo):
    print(f"Hola mundo, {saludo}")

saludo_argumento("Python!")

# Con argumento

# Con argumentos

def conArgumentos(saludo, nombre):
    print(f"{saludo}, {nombre}")

conArgumentos("Hola", "Jesus!")

# Con argumentos

# Con un argumento predeterminado

def argumento_definido(saludo = "Hola", nombre = "Jesus"):
    print(f"{saludo}, {nombre}")
    
argumento_definido()

# Con un argumento predeterminado

# Con argumentos y return

def argumento_retornar(nombre = "Jesus", edad= 23):
    return f"{nombre}, edad = {edad}"

print(argumento_retornar())

# Con argumentos y return

# Con retorno de varios valores

def retorna_multiple_saludos():
    return "Hola Jesus", "Hola Edgar", "Hola Fernanda"

jesus, edgar, fernanda = retorna_multiple_saludos()
print(jesus)
print(edgar)
print(fernanda)

# Numero variable de argumentos

def variable_argumento(*names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_argumento(1,2,3,4,5,6,7,8)

# def numeros(*numeros):
#     for numero in numeros:
#         print (f"Estos son los numeros: {numero}")
        
# numeros(1,2,3,4,5)

# Numero variable de argumentos

# Numero variable de argumentos con palabra clave

def datos(**names):
    for value, key in names.items():
        print(f"{value} = {key}")
        
datos(
    language = "Python",
    name = "Jesus",
    alias = "Moy",
    age = 24
)

# Numero variable de argumentos con palabra clave

# Funciones dentro de funciones

def fuera_funcion():
    print("Funcion fuera: Hola Python!")
    def dentro_funcion():
        print("Funcion interna: Hola Python!")
    dentro_funcion()
fuera_funcion()

# Funciones dentro de funciones

# Funciones del lenguaje (built-in)

print(len("MoureDev")) # Cuantas letras hay dentro
print(type(36))
print("MoureDev".upper()) # MAYUSCULAS

# Funciones del lenguaje (built-in)

# Extra

def retorna(texto1, texto2) -> int:
    count = 0
    for number in range(1, 101):
        if number %3 == 0 and number % 5 == 0:
            print(texto1 + texto2)
        elif number % 3 == 0: 
            print(texto1)
        elif number % 5 == 0:
            print(texto2)
        else:
            print((number))
            count += 1
    return count
print(retorna("F", "Buzz"))