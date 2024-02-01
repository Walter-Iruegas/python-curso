# una clase es una plantilla: posee atributos y metodos
# un objeto es una instancia de una clase : una "instancia" se refiere a un objeto
# particular creado a partir de una clase específica.

# El nombre de la clase asi como de la archivlleve la notacion de mayusculas y minusculas

class Persona:
    # palabra reservaba para indicar que no se va a procesar algo mas
    # se usa tambien en funciones y unicamente se quiere declarar la funcion pero ni agregar el contenido
    # Es para que cree que la funcion y clase pero no contiene ningun contenido
    pass

    # El método __init__ (metodo de tipo dunder)en Python es un método especial que se utiliza para inicializar las
    # instancias de una clase. Este método se ejecuta cuando se crea un nuevo objeto de una clase es decir,
    # cuando se hace: mi_objeto = MiClase() Al hacer esto, se está creando una nueva instancia de MiClase y se está
    # llamando a __init__ automáticamente. self hace referencia al objeto instanciado mismo. Es pasado como primer
    # argumento de forma automática. self es una referencia objeto en si mismo
    def __init__(self):
        self.nombre = 'Alberto'
        self.apellido = 'Perez'
        self.edad = 30


# Creacion de objeto
# Se almacena la referencia con una vriable y se usa el nombre de la clase y posteriormente entre parentesis
# estamos indicando que se manda a llamar el constructor de la clase
# y se llama de manera indirecta el metodo init
# La variable de self esta apuntando al objeto que se esta creando
# se crea con self los atributos del objeto
persona1 = Persona()

print(persona1.nombre)
