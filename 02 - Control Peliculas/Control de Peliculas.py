
"""

"""
import subprocess
import sys
import time
import textwrap
import os

# Importamos libreria necesaria para ejecutar programa
try:
    from clear_screen import clear
except ImportError:
    print("No posee la libreria 'clear_screen'. El programa se encuentra instalandolo.\n")

    # Si no existe la libreria, se instala
    subprocess.call([sys.executable, "-m", "pip", "install", 'clear_screen'])
    print("Instalación terminada....")
finally:
    # Luego de instalarse se importa nuevamente la libreria
    from clear_screen import clear


"""
Variables estáticas
"""
OPCION_SALIR = 0     # Nos indica en que posición queda la opción salir
CEND = '\033[0m'     # código de escape, para indicar donde termina el cambiar color en la terminarl
CGREEN = '\033[92m'  # código de escape, cambiar color del texto en la terminarl
CBLUE = '\033[94m'   # código de escape, cambiar color del texto en la terminarl
CYELLOW = '\033[93m' # código de escape, cambiar color del texto en la terminarl

# menu principal
MENU_PRINCIPAL = CBLUE + """
\t\tMenú\033[0m
\t1. Agregar Pelicula"""

# Variable de tipo diccionario que contendra las peliculas
PELICULAS = {"acción":{
                        1: {'nombre':'John Wick: Capítulo 3 - Parabellum',
                            'año': 2019,
                            'director':'Chad Stahelski',
                            'descripción':'John Wick está huyendo después de matar a un miembro del gremio internacional de asesinos, y con un precio de $ 14 millones en la cabeza, es el blanco de sicarios en todas partes.'},
                        2: {'nombre':'Spenser: Confidencial',
                            'año': 2020,
                            'director':'Peter Berg',
                            'descripción':'Cuando dos policías de Boston son asesinados, el ex policía Spenser se une a su compañero de cuarto, Hawk, para acabar con los criminales.'}
                      },
              "drama":{
                        1: {'nombre':'Doctor Sleep',
                            'año': 2019,
                            'director':'Mike Flanagan',
                            'descripción':'Años después de los eventos de "The Shining", Dan Torrance, ahora adulta, debe proteger a una joven con poderes similares de un culto conocido como The True Knot, que se aprovechan de los niños con poderes para permanecer inmortales.'}
                      }
             }

def es_entero(digito):
    """
    Método para identificar si todo un string es un digito o número
    :param digito: String que deseamos verificar si es un entero
    :return: True or False
    """
    # Verificamos si tiene signo al inicio
    if(digito[0] in ('-', '+')):
        return digito[1:].isdigit()
    return digito.isdigit()

def string_lleno(string_evaluar):
    """
    :arg string_evaluar: variable que se evaluara
    :return True si no esta vacío, False si está vacío
    """
    return bool(string_evaluar and string_evaluar.strip())

def get_generos():
    """
    Método que retorna en una lista las llaves de la variable PELICULAS
    :return: lista con los generos de pelicula
    """
    return list(PELICULAS.keys())

def display_menu_principal(generos_peliculas):
    """
    Arma las opciones de los generos para consultar las peliculas agregadas
    :generos_peliculas: lista con los generos de las peliculas creadas
    :return String con las opciones para consultar el genero en el menu
    """

    #tomamos la base del menu principal
    mensajes = MENU_PRINCIPAL

    #agregamos el código de escape para mostrar las opciones del genero de color verde
    mensajes += CGREEN

    numero_opcion = 0
    for genero in range(len(generos_peliculas)):
        # obtenemos el número de opción que le corresponde al género en el menu
        numero_opcion = (genero + 2)
        # Concatenamos la opción a la variable que contendra el menu final.
        mensajes += '\n\t{0}. "{1}"'.format(numero_opcion,generos_peliculas[genero].capitalize())

    # Terminamos de indicar el cambio del color con el código de escape
    mensajes += CEND

    # obtenemos el número de opción que le corresponde a la opción salir
    opcion_salir = numero_opcion + 1

    #Agregamos la opción salir al menu
    mensajes += "\n\t{0}. Salir\n".format(opcion_salir)

    # Mostramos el menú en la terminal
    print(mensajes)

    # Retornamos el número actualizado de la opción salir
    return opcion_salir

def get_nextKey(lista):
    """
    :arg lista: listado de las peliculas creada en un género
    :return llave de la siguiente pelicula
    """
    return (len(lista) + 1)

def get_datosPelicula():
    """
    Metodo para realizar la petición de información de una pelicula.

    :return: Diccionario con los datos ingresados de la pelicula
    """
    # Creamos el diccionario que contendra la información
    datos = {}

    try:
        # Solicitamos Nombre de pelicula
        nombre_pelicula = ""
        while True:
            nombre_pelicula = input(CBLUE + "Nombre de la Pelicula: " + CEND)
            if(string_lleno(nombre_pelicula)):
                # Si la cadena no va vacía, salimos de la solicitud
                break

            # Si no se ingreso nada, mostramos mensaje para que usuario ingrese nuevamente la información
            print(CYELLOW +"\n\t Debe Ingresar el Nombre de la Pelicula.\n" + CEND)

        # Solicitando año de la pelicula
        anio_pelicula = 0
        while True:
            anio_pelicula = input(CBLUE + "Año de la Pelicula: " + CEND)
            if(es_entero(anio_pelicula)):
                anio_pelicula = int(anio_pelicula)
                if(anio_pelicula > 0): #Puede cambiarse a un año en especifico
                    # Si el año es mayor a 0, pasamos a la siguiente solicitud
                    break
            # Si se ingresa un dato invalido, mostramos mensaje para que usuario ingrese nuevamente la información
            print(CYELLOW + "\n\tDebe Ingresar un valor númerico, positivo.\n" + CEND)

        director_pelicula = ""
        while True:
            director_pelicula = input(CBLUE + "Director de la Pelicula: " + CEND)
            if (string_lleno(director_pelicula)):
                # Si la cadena no va vacía, salimos de la solicitud
                break
            # Si no se ingreso nada, mostramos mensaje para que usuario ingrese nuevamente la información
            print(CYELLOW + "\n\tDebe Ingresar el Director de la Pelicula.\n" + CEND)

        descripcion_pelicula = ""
        while True:
            descripcion_pelicula = input(CBLUE + "Descripción de la Pelicula: " + CEND)
            if (string_lleno(descripcion_pelicula)):
                # Si la cadena no va vacía, salimos de la solicitud
                break
            # Si no se ingreso nada, mostramos mensaje para que usuario ingrese nuevamente la información
            print(CYELLOW + "\n\tDebe Ingresar la Descripcion de la Pelicula.\n" + CEND)

        # Almacenamos los datos en el diccionario

        datos["nombre"] = nombre_pelicula
        datos["año"] = anio_pelicula
        datos["director"] = director_pelicula
        datos["descripción"] = descripcion_pelicula
    # Lectura de excepción en terminar por interrución de teclado ( Ctrl + C )
    except KeyboardInterrupt:
        # Tomamos la interrupción de teclado y regresamos al menu principal sin guardar ningun dato.
        print(CYELLOW + '\n\n\t\tRregresando al menuprincipal' + CEND)
        time.sleep(2)

    return datos

def get_pelicula(listado_peliculas):
    """
    Metodo para obtener el listado de peliculas del genero solicitado, para mostrarle al usuario
    :param listado_peliculas: Lista con las peliculas del genero seleccioando por el usuario
    :return: String con el listado de peliculas.
    """
    mensaje = ""
    for genero in listado_peliculas:
        for peli in listado_peliculas[genero]:
            mensaje += "\n"+ textwrap.fill("{0}{1}:{3} {2}".format(CBLUE,peli.capitalize(),listado_peliculas[genero][peli],CEND),width=70)


        mensaje += "\n"

    return mensaje


################################################################################################################
##
##  Programa principal
##
################################################################################################################

try:

    while True:
        # Limpiamos la terminal
        clear()

        # obtenemos los generos actuales en el sistema
        generos_actuales = get_generos()

        # Armamos de forma automatica el menu y actualizamos opcion para salir del sistema
        OPCION_SALIR = display_menu_principal(generos_actuales)

        # Leemos opcion seleccionada por el usuario
        opmenu_principal = input("Ingrese el número de la opción del menú: ")

        #Verificando si no se ingreso valor
        if(string_lleno(opmenu_principal)):

            #Verificamos si se ingreso un digito entero
            if(es_entero(opmenu_principal)):

                opmenu_principal = int(opmenu_principal)

                # Verificamos si el usuario desea salir
                if(opmenu_principal == OPCION_SALIR):
                    print(CYELLOW + '\n\t\tSaliendo del Programa' + CEND)
                    # Saliendo del programa
                    exit()
                # Verificamos si desea agregar una pelicula
                elif(opmenu_principal == 1):
                    # Limpiamos la pantalla
                    clear()
                    print(CBLUE + '\t\tAgregando pelicula\n' + CEND)

                    # Solicitamos el ingreso de un genero
                    genero_pelicula = ""
                    while True:
                        try:
                            genero_pelicula = input(CBLUE + "\nIngrese el Genero de la Pelicula: " + CEND)
                            if (string_lleno(genero_pelicula)):
                                # Si el valor ingresado no es vacio, ponemos en minuscula el genero de la pelicula
                                genero_pelicula = genero_pelicula.lower()
                                # Salimos de la solicitudd del genero de la pelicula
                                break
                            # Si el dato va vacio en el ingreso, mostramos mensaje de que debe ingresar un genero y volvemos
                            # a solicitar
                            print(CYELLOW + "\n\tDebe Ingresar el Genero de la Pelicula.\n" + CEND)
                        # Si hay una interrupción de teclado ( Ctrl + C ) tomamos el error
                        except KeyboardInterrupt:
                            # Mostramos mensaje de que no se seguira ingresando información y regresamos al menu principal.
                            print(CYELLOW + '\n\n\t\tRregresando al menu principal' + CEND)
                            # Esperamos 2 segundos para que lea el usuario el mensaje
                            time.sleep(2)
                            # Salimos del ingreso de genero de pelicula
                            break

                    if(string_lleno(genero_pelicula)):

                        datos = get_datosPelicula()

                        if(len(datos) > 0):
                            next_key = 0
                            if(genero_pelicula in generos_actuales):
                                next_key = get_nextKey(PELICULAS[genero_pelicula])
                            else:
                                next_key = 1

                            if(next_key == 1):
                                PELICULAS[genero_pelicula] = {next_key:datos}

                            PELICULAS[genero_pelicula].update({next_key:datos})

                            # Mostrando mensaje de que se agrego pelicula
                            print(CYELLOW + "\nSe agrego la nueva pelicula al listado" + CEND)
                            time.sleep(2)

                # de lo contrario desea listar peliculas de un genero
                elif(0 < opmenu_principal < OPCION_SALIR):
                    # Limpiamos la pantalla
                    clear()

                    # obteniendo peliculas del genero deseado
                    obtener_genero = generos_actuales[opmenu_principal - 2]

                    # Desplegando Genero seleccionado
                    print('\n\t{0}Peliculas Vistas del Genero {1}"{2}" {3}'.format(CBLUE,CGREEN,obtener_genero.upper(),CEND))
                    # desplegando peliculas
                    print( get_pelicula(PELICULAS[obtener_genero]) )

                    # Detenemos el regreso al menu, solicitando al usuario que ingrese cualquier dato para
                    # continuar
                    input("Para regresar al menu ingrese cualquier letra o digito: ")
                else:
                    print(CYELLOW + "\nDebe ingresar un numero dentro del rango de opciones" + CEND)
                    time.sleep(2)

            else:
                print(CYELLOW + "\nDebe ingresar el numero de la opcion deseada" + CEND)
                time.sleep(2)

        else:
            print(CYELLOW + "\nDebe ingresar la opcion deseada" + CEND)
            time.sleep(2)
except KeyboardInterrupt:
        print(CYELLOW +'\n\n\t\tSaliendo del Programa'+CEND)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)