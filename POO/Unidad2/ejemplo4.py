
def Contrasena():
    try:
        while True:
            password = int(input("Contraseña: "))
                
            if (password == 1231):
                print("La contraseña es correcta, Bienvenido Pedro!")  
                break  
            else:
                print("Sigue intentando...")
    except:
        print("La contraseña es de tipo texto, intenta con valor numerico...")
            
Contrasena()