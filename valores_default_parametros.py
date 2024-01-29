#parametros por default
#Se puede agregar el tipo de dato opcional, puede considerarse redundante
def resta(a:int = 5, b:int = 2) -> int: #se puede poner un tipo de pista de loq ue va regresar, pero no quiere decir que obligatoriamente sea asi
    return a - b

print(resta())

print(resta(8,2)) # se pueden reemplazar el valor al llamar la funcion 