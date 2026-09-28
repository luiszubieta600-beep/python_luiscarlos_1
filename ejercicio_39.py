numeros = []

cantidad = int(input("Cantidad de números: "))

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

mayor = numeros[0]
segundo = numeros[0]

for numero in numeros:
    if numero > mayor:
        segundo = mayor
        mayor = numero

    elif numero > segundo and numero != mayor:
        segundo = numero

print("El segundo número mayor es:", segundo)