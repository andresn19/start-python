notas = [94, 92, 57, 84, 53, 87, 67, 98, 99,
    95, 96, 98, 94, 88, 84, 83, 78, 74, 75]
peorNota = 100
mejorNota = 0
notaPromedio = 0

# Agrega aquí el código para solucionar el problema
suma = 0

for nota in notas:
    if nota > mejorNota:
       mejorNota = nota
    if nota < peorNota:
       peorNota = nota
    suma = suma + nota

notaPromedio = suma / len(notas)

# NO CAMBIAR
print(f"Peor nota => {peorNota}")
print(f"Mejor nota => {mejorNota}")
print(f"notaPromedio nota => {notaPromedio}")