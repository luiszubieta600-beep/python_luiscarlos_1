vendedores = {}

cantidad = int(input("Cantidad de vendedores: "))

for i in range(cantidad):
    nombre = input("Nombre: ")
    venta = int(input("Total vendido: "))

    vendedores[nombre] = venta

mejor_vendedor = ""
mayor_venta = 0

for nombre, venta in vendedores.items():
    if venta > mayor_venta:
        mayor_venta = venta
        mejor_vendedor = nombre

print("Mayor vendedor:")
print(mejor_vendedor, "-> $", mayor_venta)