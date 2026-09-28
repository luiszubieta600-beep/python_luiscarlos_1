palabra = input("Palabra: ")

contador = {}

for letra in palabra:
    if letra in contador:
        contador[letra] = contador[letra] + 1
    else:
        contador[letra] = 1

for letra, cantidad in contador.items():
    print(letra, ":", cantidad)