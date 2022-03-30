####################
# Funciones Python #
####################

# def primeraFuncion(Placa, vehiculo, Marca, Color):
#     print(f'''
#     Placa: {Placa},
#     Vehiculo: {vehiculo},
#     Marca: {Marca},
#     Color: {Color}''')
#
# primeraFuncion('AHL908', 'Carro', 'Mazda', 'Gris')
# primeraFuncion('QPL71A', 'Moto', 'Suzuki','Negro')

# Sumar mediante una función usando RETURN.

# def sumar(a, b):
#     return a + b
# resultado = sumar(5,3)
# print(f'El resultado, de la suma es: {resultado}')
#
# # Sin asignar variable en el resultado
# print(f'El resultado de la suma directa es: {sumar(5,3)}')

# Sobre escritura de los valores de la función

# def suma(a = 1, b = 2):
#     return a + b
# result = suma()
# print(f'El resultado de la función con valores fijos es: {result}')
# print(f'El resultado de la suma sobreescribiendo la funcion es: {suma(8, 10)}')

############# EJERCICIO #############

# def resta(a=None, b=None):
#     if a == None or b == None:
#         print("Error, debes enviar dos números a la función")
#         return   # indicamos el final de la función aunque no devuelva nada
#     return a-b
#
# print(resta(1,2))

########## FIN EJERCICIO #########

# Pasando argumentos variables a una función

# def listar_nombres(*nombres): # Al colocar * hace referencia a que no se sabe la cantidad de parámetros
#     for nombre in nombres: # La iteración se hace como en una TUPLA = (Tupla es inmutable) no se puede modificar.
#         print(nombre)
#
# listar_nombres('Diego', 'Paola', 'Luis' '\n')
# listar_nombres('Lisa', 'Homero' '\n')

# Pasando diccionario a una función
#
# def listDiccionario (**diccionario):
#     for key, valor in diccionario.items():
#         print(f'{key}: {valor}')
#
# listDiccionario(KEY = 'Llave de diccionario', PK = 'Llave Primaria')
# listDiccionario(Valor = 'Argumento descriptivo de una llave en un diccionario')

##################################################
#### Distintos tipo de datos como argumentos #####
##################################################
#
# def datosMix (DatoFijo):
#     for DF in DatoFijo:
#         print(DF)
# DatoFijo = ['Dato', 'Fijo']
# datosMix(DatoFijo)
# datosMix(DatoFijo[0])
# datosMix((5,9)) ### Tupla entre parentesis ()###
# datosMix([9,5]) ### Lista entre parentesis []###

#############################################################
######## Función recursiva ##################################
#### Reutilizar la función las veces que sea necesario ######
# Hallar el factorial de un número para función recursiva ###
#############################################################

# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#          return numero * factorial(numero - 1)
#
# valor = int(input(f'Ingrese un valor: '))
# resultado = factorial(valor)
# print(f'El factorial de {valor} es {resultado}')





