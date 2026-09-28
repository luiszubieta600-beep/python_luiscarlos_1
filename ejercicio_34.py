numeros = []

cantidad = int(input("Cantidad de números: "))

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

buscar = int(input("Número a buscar: "))

for i in range(len(numeros)):
    if numeros[i] == buscar:
        print("El número", buscar, "se encuentra en la posición", i)