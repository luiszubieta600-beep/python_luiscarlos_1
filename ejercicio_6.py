segundos= int(input("segundos:")) 

hora= segundos // 3600 
minutos = (segundos % 3600) // 60 
segundos= segundos % 60 

print(f'segundo equivalen a:') 
print(f'hora', hora ) 
print(f'minutos', minutos) 
print(f'segundos',segundos)


