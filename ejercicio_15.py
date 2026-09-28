valor_compra= int(input("ingrese la cantidad de la compra:")) 


if valor_compra > 500000:
    descuento= valor_compra * 0.10 
    
else:
    descuento = 0 

total_a_pagar= valor_compra - descuento

print("descuento: $", int(descuento)) 
print("tatal a pagar: $", int(total_a_pagar)) 