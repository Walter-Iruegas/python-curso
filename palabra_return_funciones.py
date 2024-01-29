# El comando "return" se utiliza dentro de una función en Python para devolver o "retornar" un valor desde la función
# a quien la invocó. Algunos puntos clave sobre el uso de return:

# Permite que una función devuelva un valor para usarlo en el resto del programa. Sin un return, las funciones solo ejecutarían código pero no devolverían nada.
# Puede devolver cualquier tipo de dato (números, strings, listas, diccionarios, etc).
# Puede usarse para detener la ejecución de la función, devolviendo el control al código que la llamó.
# Se pueden tener múltiples returns en una función, para devolver valores diferentes en base a diferentes condiciones.
def suma(a, b):
    return a + b


resultado = suma(1, 4)
print(f'Resultado de la suma : {resultado}')
print(f'Resultado de la suma : {suma(1, 4)}')


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(es_par(10))  # Imprime True

# Permite que una función devuelva un valor para usarlo en el resto del programa. Sin un return, las funciones solo ejecutarían código pero no devolverían nada.
# Se refiere a lo siguiente:
# Cuando defines una función en Python, se ejecutará todo el código que esa función contenga cuando sea llamada. Por ejemplo:
def mi_funcion():
  print("Hola!")
  print("Estoy dentro de una función")

mi_funcion()

#Aquí cuando llamamos a mi_funcion(), se imprimirán los dos mensajes. Así que la función ejecuta código.
#Sin embargo, nótese que la función no devuelve nada. Una vez que se ejecuta todo su código interno, la función termina y el control vuelve al lugar desde donde fue llamada.
valor = mi_funcion()
print(valor)

#Esto causaría un error, porque la función no está devolviendo ningún valor que podamos asignar a valor.


#Con return dentro de la función, sí estamos devolviendo un valor que el código que la llama pueda usar o almacenar.

#En resumen:

#Sin return una función ejecuta código pero no devuelve un valor
#Con return la función puede devolver un valor para usarlo fuera de el