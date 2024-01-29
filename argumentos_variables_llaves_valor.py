#Los dobles asteriscos  indican que esta es una parámetro tipo **kwargs. kwargs arguments
# Esto permite pasar un número variable de argumentos keyword a la función en forma de diccionario.
#Algunos puntos clave:
#**kwargs será un diccionario dentro de la función.
#Se pueden pasar cero o más argumentos keyword al llamar la función.
#Los keys del diccionario serán los nombres de los argumentos keyword.
#Los values serán los valores pasados para esos argumentos.
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(DBMS='Database Managment System')

#Si tenmeos vario paramatros que tenemos que pasar a nuestra funcion debemos pasarlos de maenra independiente primero

def funcion(nombre, *nombres, **terminos):
    print(nombre)
    print(nombres)
    print(terminos)

funcion('Alejandro', 'Jean', 'Cesar', edad=23, nombre1="Alex")