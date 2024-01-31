#Imprmir numeros de 5 a 1 de manera descendente usando funciones  recursivas.
#Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de , debe imprimir:5 4 3 2 1
#En caso de pasar el valor de 3, deber imprimir: 3 2 1
#Si  se pasan valores negativos no imprime nada

def funcion_recursiva(numero):
    if numero >= 1:
        print(numero)
        funcion_recursiva(numero-1)
    elif numero < 0:
        return
    elif  numero < 0:
        print("Valor incorrecto...")

funcion_recursiva(5)