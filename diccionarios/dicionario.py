diccionario={
    "Programar":"Programar es transformar instrucciones en codigo",
     "POO":"Programacion orientada a objetos",
     "MVC":"Modelo vista controlador"
}


print(diccionario["POO"])

numeros={"1":"uno",
          "2":"dos",
          "3":"tres",
          "4":"cuatro",
          "5":"cinco",
          "6":"seis",
          "7":"siste",
          "8":"ocho",
          "9":"nueve",
          "0": "cero"
}

texto=input("Ingrese un numero: ")
textofinal=''
for letra in texto:
    textofinal+=numeros[letra]+ " "

print(textofinal)