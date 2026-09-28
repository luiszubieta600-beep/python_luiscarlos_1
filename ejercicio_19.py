lado1= int(input("lado 1 :"))  
lado2= int(input("lado 2 :"))
lado3= int(input("lado 3 :")) 

if lado1 == lado2 and lado2 == lado3: 
    print("el triangulo es equilatero") 
else: 
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
        print("el triangulo es isosceles") 
    else:
        print("el triangilo es escaleno")    