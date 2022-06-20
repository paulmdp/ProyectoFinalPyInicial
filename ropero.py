#!/usr/bin/env python

'''
Ejercicio integrador [Python]
-----------------------------
Autor: Inove Coding School
Version: 1.0

Descripción: Ejercicio integrador del curso PYTHON INICIAL. El objetivo es poner en práctica
los conceptos aprendidos en el curso:
    - Variables
    - Condicionales
    - Bucles
    - Funciones
    - Manejo de diccionarios
    - Manejo de archivos CSV (Comma Separated Values)
'''


import csv


def ingresar_nueva_prenda():
    '''
    IMPORTANTE: No generar los IDs a mano, utilizar la función generar_id()
    '''
    print("¡Aún no implementado!")


def eliminar_prenda_por_nombre():
    '''
    Recordatorio: Para modificar un csv, el procedimiento es el siguiente
        1. Leer todo el archivo y almacenar su resultado en una variable
        2. Modificar la variable con la modificación que deseamos hacer sobre el archivo
        3. Sobrescribir el archivo con nuestra variable modificada

    IMPORTANTE: Al finalizar esta función, Reordenar los IDs del CSV.
    '''

    print("¡Aún no implementado!")


def generar_outfit():
    print("¡Aún no implementado!")


if __name__ == '__main__':

    # 1. Preguntarle al usuario qué desea hacer
    menu = '''\n
    Seleccione una opcion:
    1. Ingresar una nueva prenda
    2. Eliminar una prenda
    3. Solicitar un Outfit
    Opcion elegida:'''

    while True:
        opcion = int(input(menu))
        print(f'\nElegiste la opción: {opcion}\n')  # Mostrarle al usuario que elección se guardó

        if opcion == 1:
            # Ingresar una nueva prenda
            ingresar_nueva_prenda()

        elif opcion == 2:
            # Eliminar una prenda por su nombre
            eliminar_prenda_por_nombre()

        elif opcion == 3:
            # Solicitar un outfit
            generar_outfit()

        else:
            # Finalizar ejecución
            break
        