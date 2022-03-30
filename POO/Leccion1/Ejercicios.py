''' Calcular el área de un rectangulo'''
#
# class calcularArea:
#
#         def __init__(self, base, altura):
#             self.base = base
#             self.altura = altura
#
#         def operacion(self):
#             return self.base * self.altura
#
# baseIn = int(input('Ingrese la base del rectangulo : '))
# alturaIn = int(input('Ingrese la altura del rectangulo : '))
#
# resultado = calcularArea(baseIn, alturaIn)
#
# print(f'El área del rectangulo es : {resultado.operacion()}')

''' Calular el volumen de un cubo '''

# class Cubo:
#
#      def __init__(self, ancho, alto, profundo):
#          self.ancho = ancho
#          self.alto = alto
#          self.profundo = profundo
#
#      def calular_volumen(self):
#          return self.ancho * self.profundo * self.alto
#
# anchoIn = int(input(f'Ingrese el ancho del cubo : '))
# profundoIn = int(input(f'Ingrese la profundidad del cubo : '))
# altoIn = int(input(f'Ingrese el alto del cubo : '))
#
# resultado = Cubo(anchoIn, profundoIn, altoIn)
# print(f'El volumen del cubo es: {resultado.calular_volumen()}' + 'm3')

''' Calcular el diametro de una circunferencia'''

#
# print(''' Seleccione la opción para hallar el diametro de la circunferencia :
# 1. opción primera. Calcular el diámetro con el rádio del círculo.
# 2. opción segunda. Calcular el diámetro con la circunferencia del circulo.
# 3. opción tercera. Calcular el diámetro con el área del circulo.
# ''')
#
# seleccion = input("Digite la opción que desee utilizar : ")
#
#     if seleccion == 1

class Circunferencia:

    def __init__(self, radio, valor_doble):
          self.radio = radio

    def diam_radio(self):
        return self.radio * 2

rad = int(input('Ingrese el valor del rádio : '))
resultado = Circunferencia(rad, 2)
print(f'La circunferencia del rádio es : {resultado.diam_radio()}')

