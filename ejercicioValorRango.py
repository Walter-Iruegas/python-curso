valor = int(input("Escribe el valor: "))

valorMinimo = 0
valorMaximo = 5

valorRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if valorRango:
    print(f'El valor {valor} esta dentro del Rango')
else:
    print(f'El valor {valor} esta fuera del Rango')