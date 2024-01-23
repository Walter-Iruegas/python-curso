#La instrucción continue se utiliza para omitir el resto del código dentro de un bucle y pasar a la siguiente iteración.
#Cuando se encuentra la palabra clave continue, el control salta directamente al inicio del bucle para la siguiente iteración, ignorando el código que queda por ejecutar en la iteración actual.
#Es útil cuando deseas omitir ciertas iteraciones basándote en una condición específica.

for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')


for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')