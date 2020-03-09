# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 07:58:04 2020

@author: Pablo Sao
@email: sao11530@uvg.edu.gt
"""

"""
En Python existen 3 formas más para almacenar colecciones de datos que
pueden ser de diferente tipo, diferenciandose por su sintaxis y su
forma de manipulación (Bahit, 2012).

"""

# Tuplas

"""
Es una variable que permite almacenar datos, donde sus valores no pueden
ser modificados (Bahit, 2012).
"""

# Formas para crear una tupla 
crear_tupla = ()

crear_tupla = tuple()


## Creando una tupla con datos
tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print()
print("Obteniendo el segundo valor de la tupla:")
print(tupla[1])

## Conviertiendo una lista a una tupla

lista = [1,2,3]

print()
print("Lista a convertir")
print(lista)


tupla = tuple(lista)

print()
print("Lista convertida a Tupla")
print(tupla)


# Listas

creando_lista = []

creando_lista = list()

## Creando una lista con datos
lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]

## Obteniendo el segundo valor de la lista

print()
print("Obteniendo el segundo valor de la lista:")
print(lista[1])

## Agregando valor al final de la lista

lista.append('Nuevo Dato')

print()
print('Mostando lista con "Nuevo Dato"')
print(lista)

## Agregando un nuevo dato en la posicion que deseamos

lista.insert(1,"Dos")

print()
print('Mostando lista con "Nuevo Dato"')
print(lista)

## Eliminando registro por indice

lista.remove("Dos")
print()
print('Mostando lista Con valor Eliminado - Metodo 1')
print(lista)

## Eliminando registro por indice

del lista[0]
print()
print('Mostando lista Con valor Eliminado - Metodo 2')
print(lista)

## Conociendo el tamaño de la lista

print()
print("Tamaño de una Lista")
print(len(lista))

## Obteniendo valores dentro de un rango de la lista
print()
print("Rango de una Lista")
print()
print(lista)
print()
print(lista[1:5])

##  Obteniendo valores, segun cada intervalo
print()
print("Rango de una lista Lista por Intervalo")
lista = [0, 1, 2, 3, 4, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print()
print(lista)
print()
print(lista[1:12:2])

## Obteniendo la posición que es multiplo de 5 en toda la lista

print("Obteniendo valores en posiciones multiplos de 5")
print()
print(lista)
print()
print(lista[::5])

## Ordenando una lista de menor a mayor

print()
print("Ordenando lista de menor a mayor")
lista = [4, 7, 5, 6, 2, 1, 3]
print()
print(lista)
print()
print(sorted(lista))


## Ordenando una lista de mayor a menor
print()
lista = [1, 2, 3, 4, 5]
print()
print("Ordenando lista de mayor a menor")
print(lista)
print()

lista.reverse()

#print(list(reversed(lista)))


print(lista)

"""
Diccionarios
"""

# Creación de una variable diccionario

variable_diccionario = {}

# Estructura de un diccionario

fruta = {1:"Pera",'dos': "Manzana"}

print("\nFrutas: {0}".format(fruta))

# Creando diccionario compuesto de diccionarios
vehiculos = {1:{'marca':'Audi','linea':'A4','año':2030},2:{'marca':'Toyota','linea':'RAV4','año':2050}}

print("\nVehículos: {0}".format(vehiculos))

# Accesando a un dicionario, dentro de otro diccionario

key = 1
carro = vehiculos[key]

print("\nAccesando a la lista con la llave {0}, obteniendo: {1}".format(key,carro))


print("\nLeyendo datos\n\tVehículo: {0} \taño:{1}".format(carro['marca'],carro['año']))


# Obteniendo el valor de una llave dentro de un diccionario

linea_carro = vehiculos.get(1).get('linea')

print("\nLinea del Carro 1: {0}".format(linea_carro))


# Cambiando valor de un parametro
vehiculos[1]['año'] = 2020

print("\nLeyendo Datos Actualizados\n\tVehículo: {0} \taño:{1}".format(vehiculos[1]['marca'],vehiculos[1]['año']))

# Creando parametro en diccionario
vehiculos[1]['disponibles'] = 5

print("\nLeyendo Nuevos Datos\n\tVehículo: {0} ".format(vehiculos))

# Copiando diccionario a nueva variable
carro = vehiculos.copy()

# Eliminando un registro

del vehiculos[2]

print("\nEliminando Vehículo con key 2:\n\t{0}".format(vehiculos))

# Eliminando todos los registros

print("\nDiccionario antes de eliminar:\n\t{0}".format(carro))

# Eliminando todos los registros del diccionario
carro.clear()

print("\nDiccionario limpio:\n\t{0}".format(carro))

# Creando datos dentro de diccionario
carro1 = {1: {'marca': 'Audi', 'linea': 'A4', 'año': 2020, 'disponibles': 5}}
carro2 = {2: {'marca': 'Toyota', 'linea': 'RAV4', 'año': 2050}}


carro.update(carro1)
carro.update(carro2)

print("\nDiccionario Actualizado:\n\t{0}".format(carro))

## Creando un tercer dato dentro de diccionario

carro.update({len(carro) + 1: {'marca': 'Renault', 'linea': 'RS', 'año': 2020,'disponibles':1}})

print("\nDiccionario Actualizado con nuevo Vehículo:\n\t{0}".format(carro))