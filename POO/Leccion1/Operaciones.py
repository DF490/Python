class operaciones:

    def __init__(self, dato1 , dato2):
        self.dato1 =  dato1
        self.dato2 = dato2

    def suma(self):

        return self.dato1 + self.dato2

    def resta(self):

        return self.dato1 - self.dato2

    def multiplicacion(self):

        return  self.dato1 * self.dato2

    def division(self):

        return self.dato1 / self.dato2


resultado = operaciones(63,96)
print(f'La suma de los valores es: {resultado.suma()}')
print(f'La resta de los valores es: {resultado.resta()}')
print(f'La multiplicación de los valores es: {resultado.multiplicacion()}')
print(f'La división de los valores es: {resultado.division():.1f}')