# Funcion recursiva= es una funcion que se manda a llamar asi misma para completar una cierta tarea
# def factorial(numero):
#    if numero == 1:
#        return 1
#    else:
#        return numero * factorial(numero-1)

# resultado = factorial(5)
# print(f'El factorial de 5 es {resultado}')


def factorial(numero):
    if numero == 1:
        print(f'Numero actual {numero}')
        print('Resultado 1 \n')
        return 1
    else:
        print(f'Numero actual {numero}')
        print(f'{numero} * factorial({numero - 1}) \n')
        fact = factorial(numero - 1)
        resultado = numero * fact
        print(f'{numero} * {fact}')
        print(f'Resultado {resultado} \n')
        return resultado


resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')

# def factorial(numero):
#    if numero == 0 or numero == 1:
#        return 1
#    else:
#        numero * factorial(numero - 1)

# numero = int(input('Ingrese el numero para hallar el factorial: '))
# resultado = factorial(numero)
# print(f'El factorial de {numero} es: {resultado}')


# Una función recursiva es aquella que se llama a sí misma.
# Esto permite resolver problemas que tienen una estructura recursiva,
# como por ejemplo calcular el factorial de un número.

# Veamos un ejemplo de una función recursiva para calcular el factorial:


# def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial(n-1)
# Analicemos cómo funciona:


# Si n == 1, se retorna 1. Esta es la condición de parada de la recursión.
# Caso recursivo:
# Si n es mayor a 1, entonces se llama a factorial(n-1).
# El resultado se multiplica por n.
# De esta forma se va reduciendo n en cada llamada hasta llegar al caso base.
# Ejemplo de ejecución para calcular 5!:

# factorial(5) retorna 5 * factorial(4)
# factorial(4) retorna 4 * factorial(3)
# factorial(3) retorna 3 * factorial(2)
# factorial(2) retorna 2 * factorial(1)
# factorial(1) retorna 1
# Y se van resolviendo esas multiplicaciones de abajo hacia arriba:

# 1 * 2 * 3 * 4 * 5 = 120

# Las funciones recursivas requieren tener un caso base que permita parar la recursión.
# También hay que tener cuidado con problemas de rendimiento y la profundidad de las llamadas.
