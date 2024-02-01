"""
Ejercicio: convertidor de Temperatura
Realiza dos funciones para convertir de grados celsius a fahrenheit y viceversa.
Grados centígrados = (grados Fahrenheit − 32) / 1.8
Grados Fahrenheit = (grados centígrados × 1.8) +32.
"""


# Funcion que convierte de fahrenheit a celsius
def faranheit_celsius(g_fahrenheit):
    return (g_fahrenheit - 32) / 1.8


# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(g_celsius):
    return (g_celsius * 1.8) + 32


celsius = float(input('Proporciona su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)

# impirmir
print(f'{celsius} C a F: {resultado:.2f}')

fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado2 = faranheit_celsius(fahrenheit)

print(f'{fahrenheit} F a C: {resultado2:.2f}')
