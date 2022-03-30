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

