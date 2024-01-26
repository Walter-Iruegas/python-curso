#Dada la siguiente tupla
#Crear una lista que solo incluya los numeros menores a 5

tupla = (13,1,8,3,2,5,8)

listNumbers = list(tupla)

for listNumber in listNumbers:
    if listNumber < 5:
        print(listNumber, end=',')
else:
    print('Fin del ciclo')


#Definir la lista
lista = []
#Filtar los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

#imprimimos la lista
print(lista)