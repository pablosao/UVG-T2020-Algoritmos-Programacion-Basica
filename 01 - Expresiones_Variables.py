# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 07:57:52 2020

@author: Pablo Sao
@email: sao11530@uvg.edu.gt
"""

"""
Una expresión es una coombinación de valores, operadores, funciones
y metodos que dan como resultado un valor
"""

# Suma de número

print("Valor de Suma 1 + 2")
print(1 + 2)

# "Suma" de caracteres. En realidad es una concatenación de Strings

print()
print('"Suma" de Caracteres')
print("Buen " + "día ")

print(("Buen " + "día -- ") * 3 )

print( "Buen día"[1] )

# Resta

print()
print("Valor de Resta 2 - 1")
print(2 - 1)

# Multilicación

print()
print("Valor de Multiplicación 2 * 2")
print(2 * 3)

# División 

print()
print("Valor de División 3 / 2")
print(3 / 2)


# Si queremos que la división nos regrese un entero y no los
# decimales, podemos utilizar dos 'Slash' (//)

print()
print("Valor de División 3 / 2 con respuesta de Entero")
print(3 // 2)


# Expresiones Booleanas (Verdadero o Falso, de igual forma puede
#                        verse como 1 o 0)

print()
print("20 es mayor que 10?")
print(20 > 10)

print()
print("20 es mayor que 10?")
print(20 < 10)

# Modulo, este retorna el residuo

"""
        1
       ________
    2 | 3
      - 2
       --------
        1        <--- Este valor es el que muestra
"""

print()
print("Modulo de 3 entre 2")
print(3 % 2)

"""

Una variable es un espacio para almacenar datos en la memoria, que
pueden ser modificables, donde cada una de estas tiene un nombre
y un valor (Bahit, 2012).

"""

nombre_variable = 10.5
print()
print(nombre_variable)

variable_alfanumerico = "abcd123"
print()
print(variable_alfanumerico)


variable_tupla = (1,2,3)
print()
print(variable_tupla)


variable_lista = [1,2.2,3]
print()
print(variable_lista)


variable_multilinea = """ Variable
Multilinea
    Tipo alfanumerico (string)
"""

print()
print(variable_multilinea)


variable_booleana = True + 4
print()
print(variable_booleana)

variable_booleana = False + 4
print()
print(variable_booleana)

"""

Existe otro tipo de variable denominada constante, la cual tiene
un nombre y un valor; sin embargo, dicho valor no se modificara
(Bahit, 2012).

"""
CONSTANTE_PI = 3.1426
print()
print(CONSTANTE_PI)