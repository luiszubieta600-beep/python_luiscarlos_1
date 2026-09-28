lado1= int(input("lado 1:")) 
lado2= int(input("lado 2:")) 
lado3= int(input("lado 3:")) 

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1: 
    print("si es posible formar un triangulo") 
else:
    print("no es posible formar un triangulo")    