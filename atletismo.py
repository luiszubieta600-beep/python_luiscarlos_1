cantidad = int(input("Cantidad de atletas: "))

tiempos = []

for i in range(cantidad):
    tiempo = float(input("Ingrese el tiempo del atleta: "))
    tiempos.append(tiempo)


menor = tiempos[0]
mayor = tiempos[0]
total = 0

for tiempo in tiempos:
    if tiempo < menor:
        menor = tiempo

    if tiempo > mayor:
        mayor = tiempo

    total += tiempo


promedio = total / cantidad


cantidad_menor_promedio = 0

for tiempo in tiempos:
    if tiempo < promedio:
        cantidad_menor_promedio += 1

print("Mejor tiempo:", menor, "s")
print("Peor tiempo:", mayor, "s")
print("Tiempo promedio:", round(promedio, 2), "s")
print("Atletas por debajo del promedio:", cantidad_menor_promedio)