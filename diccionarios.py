# Un diccionario es una estructura de datos que permite almacenar valores de diferente tipo y acceder a
# ellos rápidamente a través de una clave.
#Se definen entre llaves {}:
#midiccionario = {"clave1": "valor1", "clave2": "valor2"}
#Son mutables, se pueden modificar después de su creación.
#Las claves deben ser únicas e inmutables (cadenas, números enteros).
#Los valores pueden ser cualquier objeto válido en Python.
#El acceso a los valores es mediante sus claves entre corchetes []:
#midiccionario["clave1"]
# "valor1"
#Si la clave no existe, se genera un error.
#Algunas operaciones útiles son:
#midiccionario["nuevaclave"] = "nuevovalor" # Insertar nueva pareja
#del midiccionario["clave1"] # Eliminar un par clave-valor
#"clave1" in midiccionario # Verificar existencia

#dict (key, value)

diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

#largo
print(len(diccionario))

#no existen indices en le diccionario, par apoder acceder a un elemento (key)
print(diccionario['IDE'])

#otra fomra de recuperar un elemento unando .get()
print(diccionario.get('OOP'))

#modificando elementos
diccionario['IDE'] = 'integrated deleopment environment'