from Empleado import Empleado
from Cliente import Cliente




def cargar():
    respuesta=input("¿Va a agregar un empleado?")
    nombre=input("¿Ingrese nombre? ")
    apellido=input("¿Ingrese apellido? ")
    cedula=input("¿Ingrese Cedula? ")
    telefono=input("¿Ingrese telefono? ")
    
    if (respuesta== 'si'):
        salario= input("Ingrese salario")
        emp=Empleado(nombre, apellido, cedula, telefono, int(salario))
        personas.append(emp)
    else:
        tipo= input("Ingrese el tipo de cliente: ")
        cli=Empleado(nombre, apellido, cedula, telefono, tipo)
        personas.append(cli)

personas=[]
cargar()
cargar()

for persona in personas:
    print(persona)


