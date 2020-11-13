#Estudiante Rimari Flores Miguel Rolando 
#Codigo 1720539

def ConvertirNumeroALetra(num):   
  
    d=num//10 #decena
    u=num%10  # unidad 
    if (d==1 and u==0):
        print ("Diez")          
    elif (d==1 and u==1):
        print ("Once")
    elif (d==1 and u==2):
        print ("Doce")
    elif (d==1 and u==3):
        print ("Trece")
    elif (d==1 and u==4):
        print ("Catorce")
    elif (d==1 and u==5):
        print ("Quince")
    elif (d==1 and u==6):
        print ("Dicesiseis")
    elif (d==1 and u==7):
        print ("Diecisiete")
    elif (d==1 and u==8):
        print ("Dieciocho")
    elif (d==1 and u==9):
        print ("Diecinueve")
    else:                               
        if  (d==2 and u ==0):
            print ("Veinte")
        elif(d==2 ):
            print("Veinti")

        elif (d==3 and u ==0):
            print ("Treinta")
        elif (d==3):
            print ("Treinta y ")

        elif (d==4 and u ==0):
            print ("Cuarenta")
        elif (d==4):
            print ("Cuarenta y ")

        elif (d==5 and u ==0):
            print ("Cincuenta")
        elif (d==5):
            print ("Cincuenta y ")

        elif (d==6 and u ==0):
            print ("Sesenta")            
        elif (d==6):
            print ("Sesenta y ")

        elif (d==7 and u ==0):
            print ("Setenta")            
        elif (d==7):
            print ("Setenta y ")

        elif (d==8 and u ==0):
            print ("Ochenta")            
        elif (d==8):
            print ("Ochenta y ")

        elif (d==9 and u ==0):
            print ("Noventa")
        elif (d==9):
            print ("Noventa y ")

    if (u==1):
        print ("Uno")
    elif(u==2):
        print ("Dos")
    elif(u==3):
        print ("Tres")
    elif(u==4):
        print ("Cuatro")
    elif(u==5):
        print ("Cinco")
    elif(u==6):
        print ("Seis")
    elif(u==7):
        print ("Siete")
    elif(u==8):
        print ("Ocho")
    elif(u==9):
        print ("Nueve") 
num=int(input("Ingresa un número entre (0 y 100) -->"))    


if (100>num>0):
    ConvertirNumeroALetra(num)
else:
    print ("Ingresar un numero entre 0 y 100")

