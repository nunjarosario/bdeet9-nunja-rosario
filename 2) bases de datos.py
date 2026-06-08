n=int(input("¿Cuántos datos ingresará?"))
datos=[]

for i in range(n):
    valor= float(input(f"Ingrese el dato)){i+1}:"))
    datos. append(valor)
promedio= sum(datos)/n
print(f"Promedio:{promedio}")
 
cantidad=mayores_que(promedio,datos)
print(f"Cantidad de datos mayores al promedio:{cantidad}")
        
    