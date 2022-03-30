''' Calcular el área de un rectangulo'''

class calcularArea:

        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def operacion(self):
            return self.base * self.altura

baseIn = int(input('Ingrese la base del rectangulo : '))
alturaIn = int(input('Ingrese la altura del rectangulo : '))

resultado = calcularArea(baseIn, alturaIn)

print(f'El área del rectangulo es : {resultado.operacion()}')