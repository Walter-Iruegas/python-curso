#Una lista es una estructura de datos que permite almacenar una colección ordenada de elementos.
#Puedes crear una lista utilizando corchetes [] y separando los elementos por comas. Los elementos pueden ser de diferentes tipos (números, cadenas, booleanos, otras listas, etc.).

mi_lista = [1, 2, 3, "cuatro", True]

for lista in mi_lista:
    print(lista)

#Definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
#Imprimir una lista
print(nombres)
#acceder a los elmentos de una lista
print(nombres[0])
print(nombres[1])
print(nombres[2])
#acceder a los elementos de manera inversa
print(nombres[-1])
#imprimir rango
print(nombres[0:2])
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final, sin incluir el ultimo
print(nombres[1:])
#cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar lista
#las listas son con variables en plural y cada uno de los elementos que se van a recorrer la variable es en singular
for nombre in nombres:
    print(nombre)
else:
    print("No exiten mas nombres en la lista")