# Creacion de objetos con argumentos
class Persona1:
    # los comun es asar valores al momento de rear los objetos
    # Un constructoe es una metodo para poder crear un objeto
    def __init__(self, nombre, apellido, edad):
        # Atributos  = parametros
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona = Persona1('Walter', 'Iruegas', 32)
print(f'Objeto Persona 1 : {persona.nombre} {persona.apellido} {persona.edad}')

#Modificar atributos de un objeto
persona.nombre = "Juan Carlos"
persona.apellido = "Juarez"
persona.edad = 40
print(f'Objeto Persona 1 : {persona.nombre} {persona.apellido} {persona.edad}')


# Creacion de mas objetos
persona2 = Persona1('Karla', 'Gomez', 30)
print(f'Objeto Persona 2 : {persona2.nombre} {persona2.apellido} {persona2.edad}')

#Modifcar Atributos
persona2.nombre = "Alejandra"
persona2.apellido = "Bautista"
persona2.edad = 33

print(f'Objeto Persona 2 : {persona2.nombre} {persona2.apellido} {persona2.edad}')

# La variable self : es una variable que apunta a
# nuestro objeto que se esta ejecuntando en este momento
