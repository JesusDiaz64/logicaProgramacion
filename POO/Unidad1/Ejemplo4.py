
def signo_Zodiacal():
    
    print("Escriba su fecha de nacimiento...\n")
    
    while True: 
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        
        if 1 <= dia <= 31 and 1 <= 1 <= mes <= 12:
            break
        else:
            print("Por favor, ingrese un dia entre 1 y 31, y un mes entre 1 y 12...")
    
    if dia > 20 and mes == 3 or dia < 21 and mes == 4:
        print("\nSigno: Aries")
    elif dia > 20 and mes == 4 or dia < 21  and mes == 5:
        print("\nSigno: Tauro")
    elif dia > 20 and mes == 5 or dia < 25 and mes == 6:
        print("\nSigno: Géminis")
    elif dia > 24 and mes == 6 or dia < 23 and mes == 7:
        print("\nSigno: Cáncer")
    elif dia > 22 and mes == 7 or dia < 24 and mes == 8:
        print("\nSigno: Leo")
    elif dia > 23 and mes == 8 or dia < 24 and mes == 9:
        print("\nSigno: Virgo")
    elif dia > 23 and mes == 9 or dia < 23 and mes == 10:
        print("\nSigno: Libra")
    elif dia > 23 and mes == 10 or dia < 22 and mes == 11:
        print("\nSigno: Escorpio")
    elif dia > 21 and mes == 11 or dia < 22 and mes == 12:
        print("\nSigno: Sagitario")
    elif dia > 21 and mes == 12 or dia < 20 and mes == 20:
        print("\nSigno: Capricornio")
    elif dia > 19 and mes == 1 or dia < 19 and mes == 2:
        print("\nSigno: Acuario")
    elif dia > 18 and mes == 2 or dia < 21 and mes == 3:
        print("\nSigno: Piscis")
    else:
        print("\nVuelva colocar su fecha...")
        
signo_Zodiacal()