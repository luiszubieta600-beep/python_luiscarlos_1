palabras = []

cantidad = int(input("Cantidad de palabras: "))

for i in range(cantidad):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)

print("Lista invertida:")

for i in range(len(palabras) - 1, -1, -1):
    print(palabras[i]) 