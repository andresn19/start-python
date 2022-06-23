###### aprender a buscar en stackoverflow ######
### get emojis
palabra=True

while palabra:
        
    texto= input('>')
    if texto=='salir':
        palabra = False
    texto=texto.replace(':)','😆')
    texto=texto.replace('--','😎')
    print(texto)


 