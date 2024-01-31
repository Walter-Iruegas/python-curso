# Cuantas paginas tienen la suma de estos tres libros 50, 150, 100 Recursividad en programación se refiere a cuando
# una función o método se llama a sí mismo. Esto permite que la función resuelva problemas similares pero más
# pequeños, hasta llegar a un caso base sencillo.

def totalPaginas(Libros):
    if len(Libros) == 1:
        return Libros[0]
    return Libros[0] + totalPaginas(Libros[1:])


resp = totalPaginas([150, 100, 50])
print(resp)

# Este código define una función recursiva llamada `totalPaginas` que calcula la suma total de páginas de una lista
# de libros. Analicémoslo paso a paso:

# def totalPaginas(Libros):

# Define la función `totalPaginas` que recibe como parámetro la lista de libros `Libros`.

# if len(Libros) == 1:

# Este es el caso base. Si la longitud de la lista es 1, significa que sólo hay un libro,
# así que podemos retornar directamente el número de páginas de ese libro con `return Libros[0]`.

# return Libros[0] + totalPaginas(Libros[1:])

# Aquí está la llamada recursiva. Si hay más de un libro, entonces se retorna
# el número de páginas del primer libro (Libros[0]) más el resultado de llamar
# `totalPaginas` con el resto de la lista, excepto el primer elemento (Libros[1:]).

# Esto hace que en cada llamada recursiva la lista se vaya reduciendo,
# hasta que llegue al caso base de un solo elemento.

# Luego se ejecuta:

# resp = totalPaginas([150, 100, 50])
# print(resp)

# Donde pasamos una lista de 3 libros de 150, 100 y 50 páginas.
# La recursión los irá sumando uno a uno hasta retornar 150 + 100 + 50 = 300, que es lo que se imprime.

# Así es como funciona, usando el caso base para detener la recursión y
# las llamadas recursivas para ir reduciendo el problema hasta que se pueda resolver directamente.
