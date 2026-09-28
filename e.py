def sumar(a, b):
    return a + b 
def restar(a, b): 
    return a - b 
def multiplicar(a, b): 
    return a * b 
def dividir(a, b): 
    return a / b 


while True: 
      print("\n ---calculadora---")
      print("1. sumar")
      print("2. restar")
      print("3. multiplicar") 
      print("4. dividir") 
      print("5. salir") 

      opcion= int(input("elige una opcion:")) 
      if opcion == 5: 
          print("adios muchacho") 
          break 

      numero1= float(input("ingrese el primer numero:")) 
      numero2= float(input("ingrese el segundo numero:")) 

      match opcion: 
        case 1:
            print(f"-" *20)
            print("has elegido la suma:")
            print("el resultado es:",sumar(numero1, numero2)) 
             

        case 2: 
            print(f"-" *20)
            print("has elegido la resta") 
            print("el resultado es:", restar(numero1, numero2))

        case 3: 
            print(f"-" *20)
            print("has elegido la multiplicacion") 
            print("el resultado es:", multiplicar(numero1, numero2)) 

        case 4: 
            print(f"-" *20)
            print("has elegido la division") 
            if numero2 != 0: 
                print("el resultado es:", dividir(numero1, numero2))
            else:
                print("error: no se puede dividir entre cero mano entienda") 
