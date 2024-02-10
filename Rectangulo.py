class Rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        area = self.base * self.altura
        return area

altura1 = int(input('Proporciona la base: '))
base1 = int(input('Proporciona la altura: '))

calculoRectangulo = Rectangulo(base1, altura1)

print(f'El Area del Rectangulo es: {calculoRectangulo.calcular_area()}')