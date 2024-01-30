#Funcion recursiva= es una funcion que se manda a llamar asi misma para completar una cierta tarea
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')


def factorial(numero):1
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




#def factorial(numero):
#    if numero == 0 or numero == 1:
#        return 1
#    else:
#        numero * factorial(numero - 1)

#numero = int(input('Ingrese el numero para hallar el factorial: '))
#resultado = factorial(numero)
#print(f'El factorial de {numero} es: {resultado}')
