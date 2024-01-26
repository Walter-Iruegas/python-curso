#Son inmutables: Una vez creada una tupla, no se puede modificar, agregar o eliminar elementos.
#Se definen mediante paréntesis (): se pueden crear tuplas vacías con solo poner tupla = ().
#Pueden almacenar cualquier tipo de objetos: enteros, cadenas, listas, otras tuplas, etc.
#Se puede acceder a los elementos individuales mediante su índice, al igual que las listas.
#Son más eficientes que las listas en algunas ocasiones ya que Python puede optimizar mejor las tuplas al saber que son inmutables.
#Se pueden desempaquetar en variables individuales muy fácilmente.
# Esto significa que, una vez que se crea una tupla, no puedes modificar sus elementos ni añadir nuevos.
#mutable: que se puede modificar(modificable)
#inmutable: que no se puede modificar(no modificable)
#las tuplas son ()

#En las tuplas si solo tiene un elemento debemos poner una coma (,) al final
frutas = ('Naranja', 'Platano', 'Guayaba')
#saber el largo
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#accerder a un rango
print(frutas[0:2]) # sin incluir el ultimo indice

#tuplas Part 2
#poe default  se pone un salto de linea \n, se usa el parametro end = ' ' conun valor de espacio o cualquier otro valor para que o haga el salto
for fruta in frutas:
     print(fruta, end=' ')

#no es buena practica
#cambiar valor tupla
#converit tupla a lista para poder modificarla
frutaLista = list(frutas)
#modificar el elemento una vez sea una lista
frutaLista[0] = 'Pera'
#convertir nuevamente en tu´pla
fruta = tuple(frutaLista)
#imprimir
print('\n',fruta)

#eleiminar la tupla por completo
del fruta
print(frutas)