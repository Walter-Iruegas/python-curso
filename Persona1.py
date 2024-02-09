# Creacion de objetos con argumentos
class Persona1:
    # los comun es asar valores al momento de rear los objetos
    # Un constructoe es una metodo para poder crear un objeto
    def __init__(self, nombre, apellido, edad):
        # Atributos  = parametros
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # Metodos d instancia
        # Self se agrega a todo los metodos de intancia, es obligatorio ponerlo
        # Al estar dentro de la clase en la deficion hay usar el paramtro self para acceder a los atributos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona = Persona1('Walter', 'Iruegas', 32)
print(f'Metodo Objeto Persona 1 : {persona.nombre} {persona.apellido} {persona.edad}')

#Agregar un uevo atributo a un ibjeto, no se comparte con otros
persona.telefono = '3456323'
print(persona.telefono)

# Llamar al metodo
persona.mostrar_detalle()

# Modificar atributos de un objeto
persona.nombre = "Juan Carlos"
persona.apellido = "Juarez"
persona.edad = 40
print(f'Modificado Objeto Persona 1 : {persona.nombre} {persona.apellido} {persona.edad}')

# Llamar al metodo
persona.mostrar_detalle()

#otra fomra de llamar al meotodo
Persona1.mostrar_detalle(persona)

# Creacion de mas objetos
persona2 = Persona1('Karla', 'Gomez', 30)
print(f'Objeto Persona 2 : {persona2.nombre} {persona2.apellido} {persona2.edad}')

# Modifcar Atributos
persona2.nombre = "Alejandra"
persona2.apellido = "Bautista"
persona2.edad = 33

print(f'Modificado Objeto Persona 2 : {persona2.nombre} {persona2.apellido} {persona2.edad}')

# La variable self : es una variable que apunta a
# nuestro objeto que se esta ejecuntando en este momento

# Metodo es una funcion, pero se llama metodo por que se asocia con una Clase

# UML se utiliza para documentar Clases, Obejtos, etc
# Diagrama de clases de tipo  UML se utliza para documentar las clases y la cracion de objetos

# Self: El parametro Self en otro lenguajes de programcion se conoce como operador 'this'
# La variable self no tien que llamarse self obligatoriamente , podria tener otro nombre como this
# que hace refencia al objeto que esta ejecutando en cierto momento
# NOTA: solo que tiene que ser el primer parametro def __init__(self, nombre)
# Cuando mandamos a llamar el un metodo se puede utilizar directamente el nombre de la clase
# Pero ahora si hay que pasar un argumento posicional (es otra fomra, no muy comun)
print(f'Llamada de objeto por el nombre de la clase {Persona1.mostrar_detalle(persona2)}')

