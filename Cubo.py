class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho1 = int(input('Proporcione el ancho: '))
alto1 = int(input('Proporcione el alto: '))
profundo1 = int(input('Proporcione el profundo: '))

volumen_cubo = Cubo(ancho1, alto1, profundo1)

print(volumen_cubo.calcular_volumen())
