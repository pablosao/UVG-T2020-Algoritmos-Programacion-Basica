"""
@author: Pablo Sao
@email: sao11530@uvg.edu.gt

Ejemplo palabras palindromas:
    ama
    oso
    oro
    reconocer
    sometemos
"""

palabra_identificar = input("Ingrese Palabra a Identificar: ")

# Revirtiendo orden de la palabra
palabra_inversa = ''.join(reversed(palabra_identificar))

if(palabra_identificar == palabra_inversa):
    print("\nLa palabra es palindroma")
else:
    print("\nLa palabra no es palindroma")
