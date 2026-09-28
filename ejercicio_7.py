precio_original= int(input("ingrese el precio del producto:")) 
descuento= int(input("descuento:")) 

valor_descuento= (precio_original * descuento) / 100 
precio_final= precio_original - valor_descuento

print(f"\nsalida esperadas") 
print(f"precio orifinal: $ {precio_original}")
print(f"descuento aplicado: $ {descuento}") 
print(f"prcio final: $ {precio_final}") 
