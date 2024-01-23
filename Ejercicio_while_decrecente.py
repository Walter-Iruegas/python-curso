# Sintaxis: El bucle while se ejecuta mientras una condición sea verdadera.

# while condicion: Código a ejecutar mientras la condición sea verdadera Uso: Se utiliza cuando no se conoce de
# antemano cuántas veces se debe repetir el bloque de código. La condición se evalúa antes de cada iteración,
# y si es verdadera, el bucle continúa.

# Imprimir numeros de 5 a 1 de manera descendente
contador = 5
minimo = 1

while contador >= minimo:
    print(contador)
    contador -= 1
    # contador = contador - 1
else:
    print("Fin del ciclo")
