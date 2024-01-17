#comentarios """Comentarios""" docstring o cadenas para documentar
"""
instrucciones de la tarea:
-En el siguiente ejercicio se solicita calcular el área y el perimetro de un Rectangulo,
para ello deberemos crear las siguietes variables:
alt()int
ancho()
-El usuario debe proporcionar los valores de largo y ancho,
 y despues se debe imprimir el resultado en el siguiente formato
 (no usar acentos y respetar los espacios, mayusculas, minusculas y saltos de liena):
 Propociona el alto:
 Proporciona el ancho:
 Area: <area>
 Perimetro:<perimetro>
 Formulas para calc
 ular el area y el perimetro de un rectangulo son:
 Area: alto * ancho
 Perimetro: (alto + ancho) * 2
"""

alto = int(input("Proporciona el alto del rectangulo:"))
ancho = int(input("Proporciona el ancho del rectangulo:"))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'El area del rectangulo es: {area}')
print(f'El perimetro del rectangulo: {perimetro}')