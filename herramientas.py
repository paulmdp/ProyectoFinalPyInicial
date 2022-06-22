#!/usr/bin/env python

'''
Herramientas para resolver el ejercicio Ropero [Python]
-----------------------------
Autor: Inove Coding School
Version: 1.0

Descripción: Este módulo contiene las funciones
    - Buscar una prenda según su categoría
    - Generar un ID para una prenda
    - Reordenar IDs de un archivo CSV
    - Eliminar una prenda de una lista
'''

import csv

def generar_id():
    '''
    Funcion de ayuda, nos obtiene el ID para que insertemos una nueva prenda, el ID que devuelve
    es el último ID registrado + 1

    Ejemplo de funcionamiento
    CSV de entrada
        |----|-----------------|-----------------|------------|
        | id | nombre          | categoria       | color      |
        |----|-----------------|-----------------|------------|
        |  1 | saco viejo      | prenda superior | negro      |
        |----|-----------------|-----------------|------------|
        |  2 | camisa moderna  | prenda superior | multicolor |
        |----|-----------------|-----------------|------------|
        |  3 | remera basica   | prenda superior | blanco     |
        |----|-----------------|-----------------|------------|

    Valor de retorno → 3 + 1 → 4
    '''
    with open('prendas.csv', 'r') as csvfile:
        # Leer archivo CSV y almacenar los resultados en data
        data = list(csv.DictReader(csvfile))

    # Obtener ultima fila del CSV leído
    ultima_fila = data[-1]

    # Obtener el ID de la última fila
    ultimo_id = int(ultima_fila.get('id'))
    
    # Aumentar en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1


def reordenar_ids():
    '''
    Función que reordena los IDs del CSV de prendas
    No tiene valor de retorno.
    
    Ejemplo de funcionamiento:

    CSV de entrada
        |----|-----------------|-----------------|------------|
        | id | nombre          | categoria       | color      |
        |----|-----------------|-----------------|------------|
        |  2 | saco viejo      | prenda superior | negro      |
        |----|-----------------|-----------------|------------|
        |  4 | camisa moderna  | prenda superior | multicolor |
        |----|-----------------|-----------------|------------|
        |  7 | remera basica   | prenda superior | blanco     |
        |----|-----------------|-----------------|------------|

    CSV de salida
        |----|-----------------|-----------------|------------|
        | id | nombre          | categoria       | color      |
        |----|-----------------|-----------------|------------|
        |  1 | saco viejo      | prenda superior | negro      |
        |----|-----------------|-----------------|------------|
        |  2 | camisa moderna  | prenda superior | multicolor |
        |----|-----------------|-----------------|------------|
        |  3 | remera basica   | prenda superior | blanco     |
        |----|-----------------|-----------------|------------|
    '''

    with open('prendas.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))

    for i in range(len(data)):
        # Asignar como id de una prenda, su índice en la lista + 1, para no asignarle a nadie el ID = 0
        data[i]['id'] = i + 1

    with open('prendas.csv', 'w') as csvfile:
        # Especificar cuales serán las columnas del CSV
        header = ['id', 'nombre', 'categoria', 'color']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, fieldnames = header)

        # Escribir los nombres de las columnas
        writer.writeheader()

        # Escribir las prendas
        writer.writerows(data)


def buscar_por_categoria(prendas, categoria_buscada):
    '''
    Función que se encarga de buscar una prenda de una categoría dentro de una lista de prendas
    
    Valores de retorno
    - Si la función encuentra una prenda de la categoría deseada, devuelve la prenda: 
        {"id": <id>, "nombre": <nombre>, "categoria": categoria_buscada, "color": <color>}.
        
    - Si la función no encuentra ninguna prenda de la categoría deseada, devuelve None.
    '''
    for prenda in prendas:

        # Si la clave 'categoria' de la prenda, es igual a la categoría buscada, devolver esa prenda
        if prenda.get('categoria') == categoria_buscada:
            return prenda
    
    # Si no se encontró ninguna prenda de dicha categoría, devolver None (nada)
    return None


def eliminar_de_lista(lista, elemento):
    '''
    Esta función se encarga de eliminar un elemento de una lista
    ¿Cómo funciona?
    
    1. La función busca el índice de dicho elemento usando él método .index(elemento)
        lista = ['a', 'e', 'i', 'o', 'u']
        indice_i = lista.index('i')
        print(indice_i)
        >>> 2

    2. La función utiliza el método .pop(indice) para eliminar un elemento de la lista
        lista = ['a', 'e', 'i', 'o', 'u']
        indice_i = lista.index('i')
        lista.pop(indice_i)
        print(lista)
        >>> ['a', 'e', 'o', 'u']
    '''
    lista.pop(lista.index(elemento))