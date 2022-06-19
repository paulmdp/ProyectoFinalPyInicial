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
        print(f'Elegiste la opción: {opcion}')  # Mostrarle al usuario que elección se guardó

        if opcion == 1:
            # Ingresar una nueva prenda
            pass

        elif opcion == 2:
            # Eliminar una prenda por su nombre
            pass

        elif opcion == 3:
            # Eliminar una prenda por su ID
            pass

        elif opcion == 4:
            # Solicitar un outfit
            pass

        elif opcion == -1:
            # Salir del bucle
            pass
        