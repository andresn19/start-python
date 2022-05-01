PI = 3.14
valores = [1, 4, 11, 50, 100] # radios de las circunferencias
nuevoArray = []

def obtenerCircunferencia(radio):
    return 2 * PI * radio;

for i in valores:
    nuevoArray.append(obtenerCircunferencia(i))


print(f"Circunferencias => {nuevoArray}")