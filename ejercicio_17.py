num1= int(input("ingresa el primer numero:")) 
num2= int(input("ingrese el segundo numero:")) 
operacion= int(input("ingrese la operacion deceada:"))


if operacion == 1: 
    suma= num1 + num2 
    print("resultado:", suma) 
else:
    if operacion == 2: 
        resta= num1 - num2 
        print("resultado: ", resta) 
    else: 
        if operacion == 3: 
            multi= num1 * num2 
            print("resultado:", multi) 
        else: 
            if operacion == 4: 
                divi= num1 / num2 
                print("resultado", divi)      
