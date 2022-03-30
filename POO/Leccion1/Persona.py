class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    ''' Getter '''
    @property
    def nombre(self):
        return self._nombre

    ''' Setter '''
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'{persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1 = Persona('Alan', 'Grill', '38')
persona1.nombre = 'Alan Britho'
print(persona1.nombre)