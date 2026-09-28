cantidad_a = int(input("¿Cuántos números tiene el primer arreglo?: "))
cantidad_b = int(input("¿Cuántos números tiene el segundo arreglo?: "))

a = []
b = []

for i in range(cantidad_a):
    numero = int(input("Ingrese un número del primer arreglo: "))
    a.append(numero)

for i in range(cantidad_b):
    numero = int(input("Ingrese un número del segundo arreglo: "))
    b.append(numero)

contador = 0

for numero in range(1, 101):

    cumple = True

    for numero_a in a:

        if numero % numero_a != 0:
            cumple = False

    for numero_b in b:

        if numero_b % numero != 0:
            cumple = False

    if cumple == True:
        contador = contador + 1
print(f"-"*50) 
print(contador)