# Ejercicio : Calculadora de impuestos
# Crear una funcion para calcular el toatal de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Funcion que calcula el total de un pago incluyendo el impuesto
def calculadora_total_impuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total


pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto: '))

print(calculadora_total_impuesto(pago_sin_impuesto, impuesto))
