############ creando unn ejemplo de funciones ####
def hola():
    nombre=input("Introduce nombre: ")
    return("hola " + nombre)

def imprimir():
    print ("ejecuto la funcion hola: {}".format(hola()))

imprimir()
