# # # # # nombres = ['Juan', 'Carla', 'Pablo', 'Facundo']
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # nombres[3] = 'Nicolas'
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # print(len(nombres))
# # # # #
# # # # # nombres.append('Jorgelina')
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # nombres.insert(1, 'Octavio')
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # nombres.remove('Jorgelina')
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # nombres.pop()
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # del nombres[0]
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # nombres.clear()
# # # # #
# # # # # print(nombres)
# # # # #
# # # # # del nombres
# # # # #
# # # # # print(nombres)
# # # #
# # # # for i in range(0, 11, 1):
# # # #     if i % 3 == 0:
# # # #         print(i)
# # # #
# # # # print('------------------------')
# # # #
# # # # for i in range(2, 7, 1):
# # # #         print(i)
# # # #
# # # # print('------------------------')
# # # #
# # # # for i in range(3, 11, 2):
# # # #         print(i)
# # #
# # # frutas = ('Manzana', 'Banana', 'Naranja')
# # #
# # # print(len(frutas))
# # #
# # # print(frutas[1])
# # #
# # # print(frutas[-1])
# # #
# # # print(frutas[ :2])
# # #
# # # for fruta in frutas:
# # #     print(fruta, end=' ') # Evitar salto de linea
# # #
# # # print('-----------------')
# # #
# # # frutasLista = list(frutas)
# # #
# # # del frutas
# # #
# # # print(frutas)
# # #
# # # frutasLista[0] = 'Uva'
# # #
# # # frutas = tuple(frutasLista)
# # #
# # # print(frutas)
# # #
# #
# # tupla = (13, 1, 8, 3, 2, 5, 8)
# #
# # lista = []
# #
# # for i in tupla:
# #     if i < 5:
# #         lista.append(i)
# #
# # print(lista)
# #
#
# planetas = {'Marte', 'Venus', 'Júpiter'}
#
# print(len(planetas))
#
# print('Marte' in planetas)
#
# planetas.add('Pluton')
#
# planetas.remove('Marte') # Posible error al no encontrar la KEY
#
# planetas.discard('Pluton') # No se elimina o arroja error si no se encuentra la KEY
#
# planetas.clear()
#
# del planetas
#
# print(planetas)

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

print(len(diccionario))

print(diccionario['OOP'])

print(diccionario.get('IDE'))

diccionario['OOP'] = 'oop'

print(diccionario)

for key, value in diccionario.items(): # Keys & Values
    print(key, value)

for key in diccionario.keys(): # Keys
    print(key)

for value in diccionario.values(): # Values
    print(value)

print('IDE' in diccionario)

diccionario['PK'] = 'Primary Key'

diccionario.pop('DBMS')

diccionario.clear()

del diccionario

print(diccionario)