class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'{persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1 = Persona('Alan', 'Grill', '38')
persona1.mostrar_detalle()