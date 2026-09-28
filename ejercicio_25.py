cantidad= int(input("cantidad de notas :")) 
suma = 0

for i in range(cantidad): 
    notas=float(input("ingrese las notas:"))
    suma= suma + notas 

promedio= suma / cantidad 

print("el promedio de las notas es:", round(promedio, 2)) 
    