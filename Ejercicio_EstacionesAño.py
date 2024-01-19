#Ejercicio
#Solcitar el mes del año, un valor entre 1 y 12 y segun el valor del mes que haya proporcionado  vamos a indicar la estacion del año a la que corresponde
#primavera marzo - mayo
#verano junio septiembre
#otoño septiembre - noviembre
#invierno diciembre - febrero

mes = int(input("Proporciona Mes del Año(1-12): "))
#None valor para indicar que la variable no tiene ningun valor
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
    print(f'Para el mes  {mes} la estacion es:  {estacion}')
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
    print(f'Para el mes  {mes} la estacion es:  {estacion}')
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
    print(f'Para el mes  {mes} la estacion es:  {estacion}')
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
    print(f'Para el mes  {mes} la estacion es:  {estacion}')
else:
    estacion = 'Mes incorrecto'
    print(f'Para el mes  {mes}  la estacion es: {estacion}')



