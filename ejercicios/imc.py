##### calcular la masa muscular #####
peso=float(input("Ingrese peso KG: "))
altura=int(input("Ingrese altura Centimetros: "))
alturaenmetros=altura / 100

imc= peso / (alturaenmetros * alturaenmetros)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print ("Estado de delgadez")
if imc >= 20 and imc < 26:
    print ("peso normal")
if imc >= 26 and imc < 30:
    print("Estado de sobrepeso")
if imc >=30:
    print("Estado de obesidad")