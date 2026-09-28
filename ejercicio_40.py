productos = []

cantidad = int(input("Cantidad de productos: "))

for i in range(cantidad):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

print("Lista de compras:")

for i in range(len(productos)):
    print(i + 1, ".", productos[i])