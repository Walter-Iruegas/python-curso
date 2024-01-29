# El asterisco * indica que se empaquetarán los argumentos en una tupla. (*nombres) significa que esta función acepta
# cualquier número de argumentos posicionales. El asterisco * indica que se empaquetarán los argumentos en una tupla.
# esto es cuando no sabemos la cantidad elementos que se van a recibir se antepone un asterisco
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Alberto', 'Karal', 'Maria', 'Ernesto')

#Un argumento variable en Python es una forma de pasar un número variable de argumentos a una función. Esto se logra anteponiendo un asterisco (*) al nombre del parámetro en la definición de la función.
def suma(*numeros):
  total = 0
  for n in numeros:
    total += n
  return total

print(suma(1, 2)) # 3
print(suma(1, 2, 3)) # 6
print(suma(1, 2, 3, 4)) # 10