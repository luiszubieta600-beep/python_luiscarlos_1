agenda = {}

cantidad = int(input("Cantidad de contactos: "))

for i in range(cantidad):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    agenda[nombre] = telefono

buscar = input("Buscar contacto: ")

if buscar in agenda:
    print("Teléfono de", buscar + ":", agenda[buscar])
else:
    print("Contacto no encontrado")