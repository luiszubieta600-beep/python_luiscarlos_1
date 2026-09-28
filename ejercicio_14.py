edad= int(input("ingrese su edad pollo:")) 

if edad >= 60: 
    print("certificado:","adulto mayor") 
else: 
    if edad >= 18: 
        print("certificado:","adulto") 
    else:
        if edad >= 15:
            print("certificado:","adolecente") 
        else:
            print("certificado:","niño")    

                   