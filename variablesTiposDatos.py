miVariable = "Hola mundo"
miVariable2 = 2
print(miVariable)
print(miVariable)
print(miVariable2)

# modificar variable

miVariable2 = 4
print(miVariable2)

x = 10
y = 2
z = x + y

print(z)

# direccion de memoria donde se encuentra almacenado la variable

print(id(x))

print(id(z))

# refrencia de memeria ultmos 3 digitos
# 140706479000280
# 140706479000344

# Declaracion de variables
varNombre = "Walter"

varNumero = 899213413

varEmail = "walter@iruegas"

print(varNombre)
print(varNumero)
print(varEmail)

# Tipos de datos
# numerico = interger - float - complex number
# Dictionary
# Boolean
# Set
# Sequence Type = Strings - tuple - lista

x = 10

print(type(x))

y = True

print(type(y))

z = 3.1416

print(type(z))

# cadena (srting)
# miGrupoFavorito = "linkin park"  " "  "The best rock band"
miGrupoFavorito = "linkin park" + " " + "The best rock band"

# concatenacion con +
# print("Mi grupo favorito es: " + miGrupoFavorito)


# agrega un espacio poniendo una coma,
print("Mi grupp favorito es;", miGrupoFavorito)

# Conquetacion de strings
numero1 = "1"
numero2 = "2"

print("Conquetacion:", numero1 + numero2)

print("Suma:", int(numero1) + int(numero2))

word = "mundo"

print("hola", word)

# tipos boolean

miVariableBool = False
print(miVariableBool)

miVariableBool = 3 > 2
print(miVariableBool)

if miVariableBool:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")

# funcion input para procesar la entra del usuario
# input regresa un string
resultado = input("Escribe un mensaje: ")

print(resultado)
print("Fin del programa")

r = input("Escribe aqui")
print(r)
print("Termino el preceso")

numero1 = int(input("Escrobe el primer numero: "))
numero2 = int(input("Escrobe el segundo numero: "))

resultadoSuma = numero1 + numero2

print(resultadoSuma)
