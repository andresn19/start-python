######### arreglo multidimensional ##########


historial= [
    [34.5, 45.5, "2022/02/22"],
    [35.5, 45.5, "2022/03/22"],
    [36.5, 45.5, "2022/04/22"],
    [37.5, 45.5, "2022/05/22"],
    [38.5, 45.5, "2022/06/22"],
    [39.5, 45.5, "2022/07/22"],
]

indiceLongitud=0
indicelatitud=1
indicefecha=2

for coordenada in historial:
    print(coordenada[indicefecha])