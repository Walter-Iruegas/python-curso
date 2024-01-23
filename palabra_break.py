# La instrucción break se utiliza para salir de un bucle de manera prematura. Cuando se encuentra la palabra clave
# break, el bucle se detiene inmediatamente, incluso si la condición del bucle aún es verdadera. Se utiliza para
# salir del bucle cuando se cumple una condición específica.

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        # Rompe el ciclo, es util cunado se esta buscando un elmeneto en una lista de datos una vez encontrado romper
        # el cilo y que se detenga una vez encontado el dato
        break
else:
    print('Fin ciclo For')

for letra in "Hola mundo":
    if letra == 'o':
        print(f'Primera letra encontrada de Hola mundo: {letra}')
        break
else:
    print('Ciclo terminado')
