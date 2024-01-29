# Un diccionario es una estructura de datos que permite almacenar valores de diferente tipo y acceder a
# ellos rápidamente a través de una clave.
# Se definen entre llaves {}:
# midiccionario = {"clave1": "valor1", "clave2": "valor2"}
# Son mutables, se pueden modificar después de su creación.
# Las claves deben ser únicas e inmutables (cadenas, números enteros).
# Los valores pueden ser cualquier objeto válido en Python.
# El acceso a los valores es mediante sus claves entre corchetes []:
# midiccionario["clave1"]
# "valor1"
# Si la clave no existe, se genera un error.
# Algunas operaciones útiles son:
# midiccionario["nuevaclave"] = "nuevovalor" # Insertar nueva pareja
# del midiccionario["clave1"] # Eliminar un par clave-valor
# "clave1" in midiccionario # Verificar existencia

# dict (key, value)

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

# largo
print(len(diccionario))

# no existen indices en le diccionario, par apoder acceder a un elemento (key)
print(diccionario['IDE'])

# otra fomra de recuperar un elemento unando .get()
print(diccionario.get('OOP'))

# modificando elementos
diccionario['IDE'] = 'integrated deleopment environment'

# Acceder alas claves(termino)
for termino in diccionario:
    print(termino)
# Acceder a las clave con la funcion .keys()
for termino in diccionario.keys():
    print(termino)

# Acceder al valor directamente se usa una funcion usando .items()
for clave, valor in diccionario.items():
    print(clave, valor)
# acceder al valor con la funcion .values()
for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algun elemento
print('IDE' in diccionario)

# agregar un elemnto (no es posible agregar llaves duplicadas, si agregamos una llave existente sobreescribe la llave
# con el nuevo valor)
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento con la funcion pop()
diccionario.pop('DBMS')
print(diccionario)

# limpiar los elementos sin eliminar la variable
diccionario.clear()
print(diccionario)

# elminar la variable
del diccionario
