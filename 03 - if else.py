# -*- coding: utf-8 -*-
"""
Created Mar 09, 2020

@author: Pablo Sao
@email: sao11530@uvg.edu.gt
"""

"""
En python podemos realizar evaluaciones matemáticas y lógicas


    Igual: a == b
    No es Igual: a != b
    Menor que: a < b
    Menor o igual que: a <= b
    mayor que: a > b
    mayor o igual que: a >= b

Podemos negar la condicion lógica con not
"""

a = 10
b = 15

if a != 0:
    print("\nEl valor distinto a cero es: {0}".format(a))

if a < b:
    print("\n{0} es menor que {1}".format(a,b))
elif b < a:
    print("\n{0} es menor que {1}".format(b, a))
elif a == b:
    print("\n{0} es igual que {1}".format(a,b))

# condicionando despliegue
a = 10
b = 15
print("a es menor") if a < b else print("b es menor")


# busqueda dentro de una lista y utilizando condicion else
fruta_permitida = ["pera","manzana"]

buscar_fruta = input("Ingrese el nombre de la fruta a buscar: ")

if buscar_fruta.lower() in fruta_permitida:
    print("\nSi se permite el ingreso de la fruta: {0}".format(buscar_fruta.capitalize()))
else:
    print("No se permite el ingreso de la fruta: {0}".format(buscar_fruta.capitalize()))


# utilizando AND
a = 10
b = 15
c = "pera"


if(a < b and c == 'pera'):
    print("\nA es menor que B y si tiene una pera")

#utilizando OR

## Cuando primer parametro es falso
if(a > b or c == 'pera'):
    print("\nA no es mayor que B y si tiene una pera")

## Cuando primer parametro es verdadero
if(a < b or c == 'jocote'):
    print("\nA es menor que B y no sabemos que fruta tiene")

# condiciones anidadas
valor = 40
mensaje = "\n\tEl valor {0}: ".format(valor)

if(valor < 100):
    mensaje += "Es menor a 100,"

    if (valor < 50 ):
        mensaje += " Es menor a 50,"

        if(valor < 25):
            mensaje += " Es menor a 25,"

            if (valor < 10):
                mensaje += " Es menor a 10,"

                if(valor < 0):
                    mensaje += " Es menor a 0,"
else:
    mensaje = "\nEs mayor a 100"

print(mensaje)