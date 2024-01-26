#Set: Es una colección desordenada de elementos únicos e inmutables. Se utiliza para almacenar elementos pero no tiene orden ni indexación.
#Los sets se definen con llaves {} o con el constructor set()
#No pueden tener elementos duplicados. Los elementos tienen que ser únicos.
#Son desordenados, no tienen un índice asociado a sus elementos.
#Son muy rápidos para hacer comprobaciones de pertenencia a un set.
#Se pueden realizar operaciones como unión, intersección, diferencia entre sets.
#Se pueden agregar y eliminar elementos después de su creación.
#se pueden agragar y eliminar elementos
#no llevan un orden no hay un indice 0,1,2 etc

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#largo de los elementos
print(len(planetas))

#revisar si un elemento esta prensente
print('Marte' in planetas) #True
print('Martes' in planetas) #False

#agregar un elemento
planetas.add('Tierra')
print(planetas)

#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas) #no se agrego por es duplicado

#eliminar elemento(pisibleemnte arrojando un error)
planetas.remove('Tierra')
print(planetas)
#eliminar elemento en set
planetas.discard('Tierra')

#limpiar set
planetas.clear()

#eleminar el set
del planetas
print(planetas)

