x1 = int(input("Ingrese la posición del primer canguro: "))
v1 = int(input("Ingrese la distancia de salto del primer canguro: "))

x2 = int(input("Ingrese la posición del segundo canguro: "))
v2 = int(input("Ingrese la distancia de salto del segundo canguro: "))

encontrado = "NO"

for i in range(10000):

    posicion1 = x1 + (v1 * i)
    posicion2 = x2 + (v2 * i)

    if posicion1 == posicion2:
        encontrado = "YES"

print(encontrado)