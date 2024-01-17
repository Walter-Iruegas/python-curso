print(f'Proporciones los siguientes datos del libro: ')
nombreLibro = input("Proporciona el nombre: ")
idLibro = int(input("Proporcione el ID: "))
precioLibro = float(input("Proporcione el Precio: "))
envio = input("Indica si es envio gratuito (True/False): ")

if envio == 'true':
    print(f'El envio es gratis')
elif envio == 'false':
    print(f'El envio no es gratis')
else:
    envio = 'Valor incorrecto debe escribir true o false'

    #impresion con string """ """
print(f'''
Nombre: {nombreLibro}
Id: {id}
Precio Libro {precioLibro}
Envio Gratuito?: {envio}
''')
