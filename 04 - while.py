# -*- coding: utf-8 -*-
"""
Created Mar 09, 2020

@author: Pablo Sao
@email: sao11530@uvg.edu.gt
"""

# Variable para controlar loop
control_loop = True

while control_loop:
    respuesta = input("Desea salir del Loop? (Y/N): ")

    if(respuesta[0].upper() == 'Y' ):
        print('Salio del loop')
        # Saliendo del loop
        break
    elif(respuesta[0].upper() == 'N'):
        pass
    else:
        print("\nsigue en el loop...\n")


control_despliegue = 0

while control_despliegue < 10:
    # Sumandole 1 al control de despliegue
    control_despliegue = control_despliegue + 1

    print("Mensaje No. {0}".format(control_despliegue))

    #control_despliegue = control_despliegue + 1