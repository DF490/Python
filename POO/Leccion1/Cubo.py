''' Calular el volumen de un cubo '''

class Cubo:

     def __init__(self, ancho, alto, profundo):
         self.ancho = ancho
         self.alto = alto
         self.profundo = profundo

     def calular_volumen(self):
         return self.ancho * self.profundo * self.alto

anchoIn = int(input(f'Ingrese el ancho del cubo : '))
profundoIn = int(input(f'Ingrese la profundidad del cubo : '))
altoIn = int(input(f'Ingrese el alto del cubo : '))

resultado = Cubo(anchoIn, profundoIn, altoIn)
print(f'El volumen del cubo es: {resultado.calular_volumen()}' + 'm3')