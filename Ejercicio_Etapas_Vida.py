#Proporciona tu edad:
#0-10: la infacnia es increible
#10-20: Muchos cambios y mucho estudio
#20-30: Amor y comienza el trabajo
#Cualquier otro valor: Etapa de vida no reconocida

edad = int(input('Proporciona tu edad: '))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infacnia es increible'
    print(f'Tu edad es: {edad}, {mensaje}')
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
    print(f'Tu edad es: {edad}, {mensaje}')
elif 20 <= edad <= 30:
    mensaje = 'Amor y comienza el trabajo'
    print(f'Tu edad es: {edad}, {mensaje}')
else:
    mensaje = 'Etapa de vida no reconocida'
    print(f'{mensaje}')