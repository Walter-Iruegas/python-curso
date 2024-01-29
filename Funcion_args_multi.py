"""
Crear una funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la multiplicacion de todos los valores pasados como argumentos.
"""


def multiplicar(*numeros):
    resultado = 1
    for valor in numeros:
        resultado *= valor
    return resultado


print(multiplicar(1, 2, 3, 4))
