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
import herramientas

def ingresar_nueva_prenda():
    # Solicitar valores al usuario
    id = herramientas.generar_id()
    nombre = str(input('Ingresar nombre: '))
    categoria = str(input('Ingresar categoria: '))
    color = str(input('Ingresar color: '))

    # Construir prenda a insertar en nuestro ropero (csv)
    prenda = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "color": color
    }

    # Abrir archivo CSV y agregar la nueva prenda
    with open('prendas.csv', 'a', newline = '') as csvfile:
        
        # Especificar cuales serán las columnas del CSV
        header = ['id', 'nombre', 'categoria', 'color']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, header)

        # Agregar nuestra prenda al CSV
        writer.writerow(prenda)


def eliminar_prenda_por_nombre():
    nombre = str(input('Ingresar nombre: '))

    '''
    Recordatorio: Para modificar un csv, el procedimiento es el siguiente
        1. Leer todo el archivo y almacenar su resultado en una variable
        2. Modificar la variable con la modificación que deseamos hacer sobre el archivo
        3. Sobrescribir el archivo con nuestra variable modificada
    '''

    # Abrir el archivo CSV en modo lectura
    with open('prendas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    # Vamos a crear una variable para indicar si se encontró a la prenda que se buscaba o no, ya que
    # al ser la variable nombre un valor ingresado por el usuario, ese nombre podría no existir
    prenda_encontrada = False

    # Recorrer la variable data, en busca de la prenda que coincida con el nombre
    for prenda in data:

        if prenda.get('nombre') == nombre:
            herramientas.eliminar_de_lista(data, prenda)
            prenda_encontrada = True
            break
    
    # Si no se encontró la prenda, mostrar un mensaje de error y finalizar ejecución
    if not prenda_encontrada:  # prenda_encontrada == False:
        print(f'No se pudo encontrar la prenda con nombre {nombre}')
        
        # Finalizar la ejecución de la función (volver a bloque main)
        return
    
    # Ahora que ya modificamos la variable data, procedemos a sobrescribir en el CSV
    with open('prendas.csv', 'w') as csvfile:
        # Especificar cuales serán las columnas del CSV
        header = ['id', 'nombre', 'categoria', 'color']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, fieldnames = header)

        # Escribir el header del archivo (nombres de las columnas)
        writer.writeheader()

        # Escribir las prendas
        writer.writerows(data)

    # Reordenar IDs del CSV
    herramientas.reordenar_ids()


def generar_outfit():
    # Primero que nada, vamos a leer el archivo, de ahí vamos a sacar todas las prendas
    with open('prendas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    # Ahora, vamos a buscar una prenda de cada categoria
    prenda_superior = herramientas.buscar_por_categoria(data, 'prenda superior')
    prenda_inferior = herramientas.buscar_por_categoria(data, 'prenda inferior')
    calzado = herramientas.buscar_por_categoria(data, 'calzado')
    accesorio = herramientas.buscar_por_categoria(data, 'accesorio')

    # Validar que se haya obtenido un valor para cada tipo de prenda
    if not(prenda_superior and prenda_inferior and calzado and accesorio):
        print('No se puede crear un outfit: se necesita poseer una prenda de cada tipo')
        return

    # Imprimir el outfit generado, solamente mostrando los nombres de las prendas encontradas
    print('Prenda superior:', prenda_superior.get('nombre'))
    print('Prenda inferior:', prenda_inferior.get('nombre'))
    print('Calzado:', calzado.get('nombre'))
    print('Accesorio:', accesorio.get('nombre'))


if __name__ == '__main__':

    # 1. Preguntarle al usuario qué desea hacer
    menu = '''\n
    Seleccione una opcion:
    1. Ingresar una nueva prenda
    2. Eliminar una prenda
    3. Solicitar un outfit
    Opcion elegida:'''

    while True:
        opcion = int(input(menu))
        print(f'Elegiste la opción: {opcion}')  # Mostrarle al usuario que elección se guardó

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
        