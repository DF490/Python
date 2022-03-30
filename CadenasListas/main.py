# nombres = ['Juan','Maria','Ana','Lorena']
#
# # for nom in nombres:
# #     if nom == nombres[0]:
# #         print("nombre accesado: " + nombres[0])
# #         print("frase creada: " + nom[-1]+nom[-3]+nom[-2])
# #
# # print(f'Elementos encontrados: {len(nombres)}')
# # print(nombres)
# #
# # # Agrega un elemento al final de la lista
# # nombres.append('Jaime')
# # print(f'''
# # Se ha agregado un nuevo elemento:
# # {nombres}''')
# # print(f'Elementos encontrados: {len(nombres)}')
# #
# # # Agrega un elemento en el indice en este caso 0
# # nombres.insert(0, 'Claudia')
# # print(f'''
# # Se agregó a la posición inicial un nuevo elemento:
# # {nombres}''')
# # print(f'Elementos encontrados: {len(nombres)}')
# #
# # # Remueve un elemento especifico
# # nombres.remove('Ana')
# # print(f'''
# # Se ha removido un valor: {nombres}''')
#
# # Remueve el último valor agregado
# '''
# nombres.pop()
# print(nombres)
# '''
#
# # Remover un elemento en un indice indicado
# '''
# del nombres[0]
# print(nombres)
# '''
#
# # Remover todos lo elementos de la lista
# '''
# nombres.clear()
# print(nombres)
# '''
# # Remover lista por completo
# '''
# del nombres
# print(nombres)
# '''
# # Imprimir un rango
# print(nombres[0:2]) # Sin incluir el indice 2
#
# # Ir del inicio ed la lista al índice (sin incluirlo)
# print(nombres[:3])
#
# # Recorrer lista desde el índice indicado hasta el final de la lista
# print(nombres[1:])
#
# # Cambiar el valor de un índice
# nombres[3] = 'Karla'
# print(nombres)
#
# # Iterar una lista
#
# for nom2 in nombres:
#     print(nom2)
# else:
#     print('No hay mas elementos por mostrar')

#################################################
# TUPLAS ELEMENTOS NO MUTABLES O MODIFICABLES  ##
#################################################

alimentos = ('Pollo' ,'Arroz','Queso','Mango')
# print(f'Cantidad de elementos encontrados en la Tupla: {len(alimentos)}')
# print(alimentos)
# print(alimentos[2])
# print(alimentos[0:2])
# print(alimentos[2:])

# # Iteración con end para cambiar salto de linea \n por espacio en blanco
# for i in alimentos:
#     print(i, end = " " )

# Modificar tuplas, pasando a lista
# alimentosLista = list(alimentos)
# alimentosLista[0] = 'Carne'
# alimentos = tuple(alimentosLista)
# print(alimentos)

###########################################################
# SET listas sin índice no tiene un orden al imprimir    ##
# Acepta atributos como Add, remove, clear, del, discard ##
###########################################################
# vehiculos = {'Chevrolet','Mazda','Subaru'}
# print(vehiculos)
# vehiculos.add('Hyunday')
# print(vehiculos)

#############################################
# Diccionarios--Estructura (key, value)----##
#############################################
#
# diccionario = {
#     'LAN':'Local Area Network',
#     'WAN':'World Area Network',
#     'MAN':'Metropolitan Area Network'
# }
# print(diccionario)
# print(len(diccionario))
# # Acceder a un elemento por su (KEY)
# print(diccionario['MAN'])
# # Segunda forma de acceder al elemento
# print(diccionario.get('LAN'))
# # Modificar elementos
# diccionario['LAN'] = 'Local-Area-Network'
# print(diccionario)
# print(len(diccionario))
# diccionario.pop('LAN')
# print(diccionario)
# print(len(diccionario))