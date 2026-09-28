s = int(input("Ingrese el inicio de la casa: "))
t = int(input("Ingrese el final de la casa: "))

a = int(input("Ingrese la posición del manzano: "))
b = int(input("Ingrese la posición del naranjo: "))

cantidad_manzanas = int(input("¿Cuántas manzanas hay?: "))
cantidad_naranjas = int(input("¿Cuántas naranjas hay?: "))

manzanas = []
naranjas = []

for i in range(cantidad_manzanas):
    manzana = int(input("Ingrese la distancia de la manzana: "))
    manzanas.append(manzana)

for i in range(cantidad_naranjas):
    naranja = int(input("Ingrese la distancia de la naranja: "))
    naranjas.append(naranja)

contador_manzanas = 0
contador_naranjas = 0

for manzana in manzanas:

    posicion = a + manzana

    if posicion >= s and posicion <= t:
        contador_manzanas = contador_manzanas + 1

for naranja in naranjas:

    posicion = b + naranja

    if posicion >= s and posicion <= t:
        contador_naranjas = contador_naranjas + 1

print(f"-"*50)
print("Manzanas que cayeron en la casa:", contador_manzanas)
print("Naranjas que cayeron en la casa:", contador_naranjas)