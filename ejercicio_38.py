lista1 = []
lista2 = []
lista3 = []

cantidad = int(input("Cantidad de elementos: "))

for i in range(cantidad):
    numero = int(input("Lista 1 - número: "))
    lista1.append(numero)

for i in range(cantidad):
    numero = int(input("Lista 2 - número: "))
    lista2.append(numero)

lista3 = lista1 + lista2

print("Lista combinada:")

for numero in lista3:
    print(numero)