# 1Definir una clase
class Persona:
    # Metodo inicializador
    def __init__(self):  # self una refenrencia del objeto, solo se declara no se pasa ningun valor
        self.nombre = 'Alberto'
        self.apellido = 'Perez'
        self.edad = 30


persona1 = Persona()

# Acceder a los atributos de la clase
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
