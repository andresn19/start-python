n1= int(input("nota 1:"))
n2= int(input("nota 2: "))
n3= int(input ("nota 3: "))

promedio = (n1 + n2 + n3) / 3
print("su promedio es: ", promedio)


#############promediar equis notas ################################
suma= 0
total=0
i=0
promedio2=0

notas= int(input("Introduzca cantidad de notas: "))

for i in range(notas):
    suma = int(input("dame calificacion: "))
    total+= suma

promedio2= total / notas
print("tu promedio definitivo es de: ", promedio2)




