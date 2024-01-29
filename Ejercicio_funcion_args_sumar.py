"""
Crear una funcion para sumar los valores recibidos de tipo numerico, utilizando argumnetos variables * args como
paramtros de la funcion y regresa como resultado la suma de todos
<<<<<<< HEAD
"""


def sumar_valores(*args) -> int:
    resultado = 0
    # iteramos cada elementos
    for valor in args:
        resultado += valor
    return resultado


print(sumar_valores(1, 2, 3, 4))
=======
"""
>>>>>>> ca0d17b (Leccion 5 python)
