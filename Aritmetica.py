class Aritmetica:
    # comentarios DOcString = Documentacion de la Clase en Python
    """
    Clase Aritmetica para realizar las operadones de sumar, restar, tec
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)

print(f'Suma {aritmetica1.sumar()}')

print(f'Suma {aritmetica1.restar()}')

print(f'Suma {aritmetica1.multiplicar()}')

#para poner el formato de que cantidad digitos depues del punto poner
#esto se hace al imprimir con f, numero flotantes :.2f
print(f'Suma {aritmetica1.dividir():.2f}')
