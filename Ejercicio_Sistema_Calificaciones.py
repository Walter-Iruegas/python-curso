"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, es como sigue:
El usuario porporconara un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menos a 9: imprimir una B
Si está entre 7 y menos a 8: imprimir una C
Si está entre 6 y menos a 7: imprimir una D
Si está entre 0 y menos a 6: imprimir una F
cualquier otro valor debe imprimir: valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10
A
"""

calificacion = float(input('Proporcione su calificacion: '))
letra= None

if 9 <= calificacion <= 10:
    letra = 'A'
    print(f'Su calificacion es: {letra}')
elif 8 <= calificacion < 9:
    letra = 'B'
    print(f'Su calificacion es: {letra}')
elif 7 <= calificacion < 8:
    letra = 'C'
    print(f'Su calificacion es: {letra}')
elif 6 <= calificacion < 7:
    letra = 'D'
    print(f'Su calificacion es: {letra}')
elif 0 <= calificacion < 6:
    letra = 'F'
    print(f'Su calificacion es: {letra}')