# Ejercicio Práctico Proyecto Final
# Python Inicial
# Autor: Pablo Damián Fiore
# Version: 1.0

'''
Breve descripción:
Este proyecto se basa en recolectar y procesar los datos generados desde un dispositivo construido 
para sensar temperatura y humedad ambiente y humedad de suelo dentro de un invernadero de cultivo.
Importar los datos desde este dispositivo y procesarlos para brindar información significativa 
para la toma de decisiones, será la misión de este programa.
Detalles del proyecto y diagramas:
https://github.com/paulmdp/ProyectoFinalPyInicial/blob/main/readme.md
'''

from atexit import register
import os
import csv
import time
from datetime import datetime

def importar():
    os.system('cls')
    print("Importar Datos desde SD")
    print("Selecciona una opción")
    print("\t 1 - Importar Datos TH (Temperatura y Humedad)")
    print("\t 2 - Importar Datos CA (Caudal)")
    print("\t 9 - Menú Principal")
    # solicituamos una opción al usuario
    opcion_menu = input("Ingresa la opción y luego pulsa <INTRO> >> ")
    if opcion_menu=="1":
        # solicituamos una opción al usuario
        userfile = input("Ingrese la ruta y nombre del archivo de TH (Ej. D:\dataTH.csv) >> ")
        # Abro archivo de TH 
        try:
            with open(userfile) as fileTH:
            # Leo los datos y almaceno en lista
                dataTH = list(csv.reader(fileTH))
                print(dataTH)
        except FileNotFoundError:
            print("Nombre de archivo No encontrado\nIntente nuevamente")  
            time.sleep(4)
            return
                       
        try:
            with open('masterTH.csv','a', newline='') as masterTH:
                writer=csv.writer(masterTH)
                # escribo en master los datos de la lista
                writer.writerows(dataTH)
        except:
            print("Error al abrir el archivo masterTH")
            time.sleep(4)
            return
            
    elif opcion_menu=="2":
        # solicituamos una opción al usuario
        userfile = input("Ingrese la ruta y nombre del archivo de CA (Ej. D:\dataCA.csv) >> ")
        # Abro archivo de TH 
        try:
            with open(userfile) as fileCA:
                # Leo los datos y almaceno en lista
                dataCA = list(csv.reader(fileCA))
                print(dataCA)
        except FileNotFoundError:
            print("Nombre de archivo No encontrado\nIntente nuevamente")           
            time.sleep(4)
            return
        
        try:
            with open('masterCA.csv','a', newline='') as masterCA:
                writer=csv.writer(masterCA)
                # escribo en master los datos de la lista
                writer.writerows(dataCA)
        except:
            print("Error al abrir el archivo masterCA")
            time.sleep(4)
            return
               
    elif opcion_menu=="9":
        return
    else:
        print ("")
        input("La opción elegida es incorrecta...\nPulsa una tecla para continuar")

    input("Proceso completado..\nPulsa una tecla para continuar")
# --------------------------------

def listar():
    os.system('cls')
    print("Listar Registros")
    print("Selecciona una opción")
    print("\t 1 - Listar Registros TH (Temperatura y Humedad)")
    print("\t 2 - Listar Registros CA (Caudal)")
    print("\t 9 - Menú Principal")
    # solicituamos una opción al usuario
    opcion_menu = input("Ingresa la opción y luego pulsa <INTRO> >> ")
    if opcion_menu=="1":
        # Solicito fechas al usuario
        while(1):
            try:        
                fdesde=input("Ingrese fecha inicial (dd-mm-aaaa): ")
                fhasta=input("Ingrese fecha final (dd-mm-aaaa): ")   
                # Convierto los str a datetime
                fdesde_dt=datetime.strptime(fdesde, "%d-%m-%Y")
                fhasta_dt=datetime.strptime(fhasta, "%d-%m-%Y")
            except ValueError:
                print("Fechas invalidas ingrese nuevamente...")
            else: 
                break    
        # Abro archivo de TH 
        try:
            with open('masterTH.csv') as masterTH:
                # Leo los datos y almaceno en lista
                dicTH = list(csv.DictReader(masterTH))
                os.system('cls')
                print('\n\n')
                print('\t', "Hora",'\t', "Fecha", '\t\t ',"Temp. 1", '\t',"Temp. 2", '\t',"Temp. 3", '\t',"Hum. 1", '\t',"Hum. 2", '\t',"Hum. 3")
                print('\t',"--------------------------------------------------------------------------------------------------------------------")
                fila=0
                for r in dicTH:
                    freg=datetime.strptime(r.get('fecha_registro'), "%d/%m/%Y")
                    if (freg >= fdesde_dt and freg <= fhasta_dt):
                        fila+=1
                        print('\t', r.get('hora_registro'),'\t', r.get('fecha_registro'),'\t ', r.get('sensor_T01'), '\t\t',r.get('sensor_T02'), '\t\t',r.get('sensor_T03'), '\t\t',r.get('sensor_H01'), '\t\t',r.get('sensor_H02'), '\t\t',r.get('sensor_H03'))
                    if (fila==40): 
                        fila=0
                        print ("")
                        input("Pulsar <INTRO> para continuar...")
                        os.system('cls')
                        print('\n\n')
                        print('\t', "Hora",'\t', "Fecha", '\t\t ',"Temp. 1", '\t',"Temp. 2", '\t',"Temp. 3", '\t',"Hum. 1", '\t',"Hum. 2", '\t',"Hum. 3")
                        print('\t',"--------------------------------------------------------------------------------------------------------------------")
        except FileNotFoundError:
            print("Error al abrir el archivo masterTH")           
            time.sleep(4)
            return
        
            
    elif opcion_menu=="2":
        # Solicito fechas al usuario
        while(1):
            try:        
                fdesde=input("Ingrese fecha inicial (dd-mm-aaaa): ")
                fhasta=input("Ingrese fecha final (dd-mm-aaaa): ")   
                # Convierto los str a datetime
                fdesde_dt=datetime.strptime(fdesde, "%d-%m-%Y")
                fhasta_dt=datetime.strptime(fhasta, "%d-%m-%Y")
            except ValueError:
                print("Fechas invalidas ingrese nuevamente...")
            else: 
                break    
        # Abro archivo de CA 
        try:    
            with open('masterCA.csv') as masterCA:
                # Leo los datos y almaceno en lista
                dicCA = list(csv.DictReader(masterCA))
                os.system('cls')
                print('\n\n')
                print('\t\t', "Hora",'\t', "Fecha", '\t','\t',"Caudal", '\t',"Volumen")
                print('\t\t',"-------------------------------------------------------------")
                fila=0
                for r in dicCA:
                    freg=datetime.strptime(r.get('fecha_registro'), "%d/%m/%Y")
                    if (freg >= fdesde_dt and freg <= fhasta_dt):
                        fila+=1
                        print('\t\t', r.get('hora_registro'),'\t', r.get('fecha_registro'),'\t', r.get('caudal_max'), '\t','\t',r.get('volumen_lts'))
                    if (fila==40): 
                        fila=0
                        print ("")
                        input("Pulsar <INTRO> para continuar...")
                        os.system('cls')
                        print('\n\n')
                        print('\t\t', "Hora",'\t', "Fecha", '\t','\t',"Caudal", '\t',"Volumen")
                        print('\t\t',"----------------------------------------------------------")
        except FileNotFoundError:
            print("Error al abrir el archivo masterCA")           
            time.sleep(4)
            return
        
             
    elif opcion_menu=="9":
        return
    else:
        print ("")
        input("La opción elegida es incorrecta...\nPulsa una tecla para continuar")
  
    input("Proceso completado..\nPulsa una tecla para continuar")
# --------------------------------


def informes():
    os.system('cls')
    print("Informes Estadísticos")
    print("Selecciona una opción")
    print("\t 1 - Informe Estadístico TH (Temperatura y Humedad)")
    print("\t 2 - Informe Estadístico (Caudal)")
    print("\t 9 - Menú Principal")
    # solicituamos una opción al usuario
    opcion_menu = input("Ingresa la opción y luego pulsa <INTRO> >> ")
    if opcion_menu=="1":
        #Inicializo variables
        T01_max=0.0
        T02_max=0.0
        T03_max=0.0
        T01_min=99.0
        T02_min=99.0
        T03_min=99.0
        
        H01_max=0.0
        H02_max=0.0
        H03_max=0.0
        H01_min=99.0
        H02_min=99.0
        H03_min=99.0

        T_acu=0.0
        H_acu=0.0

        # Solicito fechas al usuario
        while(1):
            try:        
                fdesde=input("Ingrese fecha inicial (dd-mm-aaaa): ")
                fhasta=input("Ingrese fecha final (dd-mm-aaaa): ")   
                # Convierto los str a datetime
                fdesde_dt=datetime.strptime(fdesde, "%d-%m-%Y")
                fhasta_dt=datetime.strptime(fhasta, "%d-%m-%Y")
            except ValueError:
                print("Fechas invalidas ingrese nuevamente...")
            else: 
                break    
        # Abro archivo de TH 
        try:    
            with open('masterTH.csv') as masterTH:
                # Leo los datos y almaceno en lista
                dicTH = list(csv.DictReader(masterTH))
                os.system('cls')
                print('\n')
                print('\n\t\t\tInforme Estadístico de Temperatura y Humedad Ambiente')
                registros=0
                for r in dicTH:
                    # r.get('hora_registro'),'\t', r.get('fecha_registro'),'\t ', r.get('sensor_T01'), '\t\t',r.get('sensor_T02'), '\t\t',r.get('sensor_T03'), '\t\t',r.get('sensor_H01'), '\t\t',r.get('sensor_H02'), '\t\t',r.get('sensor_H03')
                    freg=datetime.strptime(r.get('fecha_registro'), "%d/%m/%Y")
                    if (freg >= fdesde_dt and freg <= fhasta_dt):
                        registros+=3 # Incremento de a 3 porque acumulo los 3 valores de T y H
                        #Acumulopara promedios
                        T_acu += (float(r.get('sensor_T01')) + float(r.get('sensor_T02')) + float(r.get('sensor_T03')))
                        H_acu += (float(r.get('sensor_H01')) + float(r.get('sensor_H02')) + float(r.get('sensor_H03')))
                        
                        # Convierto str a float
                        sensor_T01=float(r.get('sensor_T01'))
                        sensor_T02=float(r.get('sensor_T02'))
                        sensor_T03=float(r.get('sensor_T03'))
                        sensor_H01=float(r.get('sensor_H01'))
                        sensor_H02=float(r.get('sensor_H02'))
                        sensor_H03=float(r.get('sensor_H03'))
                        
                        # Determino máximos
                        if(sensor_T01 > T01_max):
                            T01_max = sensor_T01
                            fecha_maxT01 = r.get('fecha_registro')
                            hora_maxT01 = r.get('hora_registro')
                        if(sensor_T02 > T02_max):
                            T02_max = sensor_T02
                            fecha_maxT02 = r.get('fecha_registro')
                            hora_maxT02 = r.get('hora_registro')
                        if(sensor_T03 > T03_max):
                            T03_max = sensor_T03
                            fecha_maxT03 = r.get('fecha_registro')
                            hora_maxT03 = r.get('hora_registro')

                        if(sensor_H01 > H01_max):
                            H01_max = sensor_H01
                            fecha_maxH01 = r.get('fecha_registro')
                            hora_maxH01 = r.get('hora_registro')
                        if(sensor_H02 > H02_max):
                            H02_max = sensor_H02
                            fecha_maxH02 = r.get('fecha_registro')
                            hora_maxH02 = r.get('hora_registro')
                        if(sensor_H03 > H03_max):
                            H03_max = sensor_H03
                            fecha_maxH03 = r.get('fecha_registro')
                            hora_maxH03 = r.get('hora_registro')
                        
                        # Determino mínimos
                        if(sensor_T01 < T01_min):
                            T01_min = sensor_T01
                            fecha_minT01 = r.get('fecha_registro')
                            hora_minT01 = r.get('hora_registro')
                        if(sensor_T02 < T02_min):
                            T02_min = sensor_T02
                            fecha_minT02 = r.get('fecha_registro')
                            hora_minT02 = r.get('hora_registro')
                        if(sensor_T03 < T03_min):
                            T03_min = sensor_T03
                            fecha_minT03 = r.get('fecha_registro')
                            hora_minT03 = r.get('hora_registro')

                        if(sensor_H01 < H01_min):
                            H01_min = sensor_H01
                            fecha_minH01 = r.get('fecha_registro')
                            hora_minH01 = r.get('hora_registro')
                        if(sensor_H02 < H02_min):
                            H02_min = sensor_H02
                            fecha_minH02 = r.get('fecha_registro')
                            hora_minH02 = r.get('hora_registro')
                        if(sensor_H03 < H03_min):
                            H03_min = sensor_H03
                            fecha_minH03 = r.get('fecha_registro')
                            hora_minH03 = r.get('hora_registro')
                        
                # Promedios        
                if(registros):
                    promedioT = T_acu/registros
                    promedioH = H_acu/registros
                else:
                    promedioT = 0
                    promedioH = 0   
                    
        except FileNotFoundError:
            print("Error al abrir el archivo masterTH")           
            time.sleep(4)
            return
        
        # Muestro resultados
        if(registros):
            print("\n\t\tTemperatura Máxima registrada Sensor 01:", T01_max, "°C el día:",fecha_maxT01, "a las", hora_maxT01, "Hs.")
            print("\t\tTemperatura Mínima registrada Sensor 01:", T01_min, " °C el día:",fecha_minT01, "a las", hora_minT01, "Hs.")
            print("\n\t\tTemperatura Máxima registrada Sensor 02:", T02_max, "°C el día:",fecha_maxT02, "a las", hora_maxT02, "Hs.")
            print("\t\tTemperatura Mínima registrada Sensor 02:", T02_min, " °C el día:",fecha_minT02, "a las", hora_minT02, "Hs.")
            print("\n\t\tTemperatura Máxima registrada Sensor 03:", T03_max, "°C el día:",fecha_maxT03, "a las", hora_maxT03, "Hs.")
            print("\t\tTemperatura Mínima registrada Sensor 03:", T03_min, "°C el día:",fecha_minT03, "a las", hora_minT03, "Hs.")
            print("\n\t\tHumedad Máxima registrada Sensor 01:", H01_max, "% el día:",fecha_maxH01, "a las", hora_maxH01, "Hs.")
            print("\t\tHumedad Mínima registrada Sensor 01:", H01_min, "% el día:",fecha_minH01, "a las", hora_minH01, "Hs.")
            print("\n\t\tHumedad Máxima registrada Sensor 02:", H02_max, "% el día:",fecha_maxH02, "a las", hora_maxH02, "Hs.")
            print("\t\tHumedad Mínima registrada Sensor 02:", H02_min, "% el día:",fecha_minH02, "a las", hora_minH02, "Hs.")
            print("\n\t\tHumedad Máxima registrada Sensor 03:", H03_max, "% el día:",fecha_maxH03, "a las", hora_maxH03, "Hs.")
            print("\t\tHumedad Mínima registrada Sensor 03:", H03_min, "% el día:",fecha_minH03, "a las", hora_minH03, "Hs.")
            print("\n\t\tTemperatura Promedio:", round(promedioT,2), "°C")
            print("\t\tHumedad Relativa Promedio:", round(promedioH,2), "%")
        else:
            print("\n\t\t No hay registros para este período...")        
           
    elif opcion_menu=="2":
        #Inicializo variables
        caudal_max=0.0
        caudal_min=999999.0
        caudal_acu=0.0
        volumen_max=0.0
        volumen_min=999999.0
        volumen_acu=0.0
        # Solicito fechas al usuario
        while(1):
            try:        
                fdesde=input("Ingrese fecha inicial (dd-mm-aaaa): ")
                fhasta=input("Ingrese fecha final (dd-mm-aaaa): ")   
                # Convierto los str a datetime
                fdesde_dt=datetime.strptime(fdesde, "%d-%m-%Y")
                fhasta_dt=datetime.strptime(fhasta, "%d-%m-%Y")
            except ValueError:
                print("Fechas invalidas ingrese nuevamente...")
            else: 
                break    
        # Abro archivo de CA 
        try:    
            with open('masterCA.csv') as masterCA:
                # Leo los datos y almaceno en lista
                dicCA = list(csv.DictReader(masterCA))
                os.system('cls')
                print('\n')
                print('\n\t\t\tInforme Estadístico de Riego')
                registros=0
                for r in dicCA:
                    freg=datetime.strptime(r.get('fecha_registro'), "%d/%m/%Y")
                    if (freg >= fdesde_dt and freg <= fhasta_dt):
                        registros+=1
                        caudal_acu += float(r.get('caudal_max'))
                        volumen_acu += float(r.get('volumen_lts'))
                        caudal=float(r.get('caudal_max'))
                        volumen=float(r.get('volumen_lts'))
                        
                        #Determino máximos
                        if(caudal > caudal_max):
                            caudal_max = caudal
                            fecha_maxCA = r.get('fecha_registro')
                            hora_maxCA = r.get('hora_registro')
                        if(volumen > volumen_max):
                            volumen_max = volumen
                            fecha_maxVOL = r.get('fecha_registro')
                            hora_maxVOL = r.get('hora_registro')       
                        # Determino mínimos                             
                        if(caudal < caudal_min):
                            caudal_min = caudal
                            fecha_minCA = r.get('fecha_registro')
                            hora_minCA = r.get('hora_registro')
                        if(volumen < volumen_min):
                            volumen_min = volumen
                            fecha_minVOL = r.get('fecha_registro')
                            hora_minVOL = r.get('hora_registro')                                
                        
                # Promedios        
                if(registros):
                    promedioCA = caudal_acu/registros
                    promedioVOL = volumen_acu/registros
                else:
                    promedioCA = 0
                    promedioVOL = 0
                    

        except FileNotFoundError:
            print("Error al abrir el archivo masterCA")           
            time.sleep(4)
            return
        
        # Muestro resultados si hay registros
        if(registros):
            print("\n\t\t\tCaudal Máximo:", caudal_max, " Lts/minuto el día:",fecha_maxCA, "a las", hora_maxCA, "Hs.")
            print("\t\t\tCaudal Mínimo:", caudal_min, " Lts/minuto el día:",fecha_minCA, "a las", hora_minCA, "Hs.")
            print("\t\t\tCaudal Promedio:", round(promedioCA,2), "Lts/minuto")
            print("\n\t\t\tVolumen Máximo:", volumen_max, "Litros aplicados el día:",fecha_maxVOL, "a las", hora_minVOL, "Hs.")
            print("\t\t\tVolumen Mínimo:", volumen_min, " Litros el día:",fecha_minVOL, "a las", hora_minVOL, "Hs.")
            print("\t\t\tVolumen Promedio:", round(promedioVOL,2),"Litros")
            print("\t\t\tVolumen Total Aplicado:", round(volumen_acu,2),"Litros")
        else:
            print("\n\t\t No hay registros para este período...")        
             
    elif opcion_menu=="9":
        return
    else:
        print ("")
        input("La opción elegida es incorrecta...\nPulsa una tecla para continuar")
     
    
    
    input("\n\nProceso completado..\nPulsa una tecla para continuar")
    
# --------------------------------
def menu():
    os.system('cls')
    print("Sistema de análisis de datos de Invernadero")
    print("Selecciona una opción")
    print("\t 1 - Importar Datos desde SD")
    print("\t 2 - Listar Registros entre fechas")
    print("\t 3 - Informe Estadístico entre fechas")
    print("\t 9 - Finalizar")
 

if __name__ == '__main__':
    
    # Si no existen los archivos master, los creo con sus respectivas cabeceras
    # listos para importar datos
    try:
        with open('masterTH.csv','r', newline='') as fileTH:
        # Leo los datos y almaceno en lista de diccionarios
            dataTH = list(csv.reader(fileTH))
    except:
        header=["num_registro","hora_registro","fecha_registro","sensor_T01","sensor_T02","sensor_T03","sensor_H01","sensor_H02","sensor_H03"]
        # Crea el archivo con la cabecera
        archivo = open('masterTH.csv', 'w',newline='')
        # Generar un "escritor" para modificar el archivo creando la cabecera
        writer = csv.DictWriter(archivo, fieldnames=header)
        writer.writeheader()
        archivo.close()

    try:
        with open('masterCA.csv','r',  newline='') as fileCA:
        # Leo los datos y almaceno en lista de diccionarios
            dataCA = list(csv.reader(fileCA))
    except:
        header=["num_registro","hora_registro","fecha_registro","caudal_max","volumen_lts"]
        # Crea el archivo con la cabecera
        archivo = open('masterCA.csv', 'w', newline='')
        # Generar un "escritor" para modificar el archivo creando la cabecera
        writer = csv.DictWriter(archivo, fieldnames=header)
        writer.writeheader()
        archivo.close()        
    while True:
        # Mostramos el menu
        menu()
    
        # solicituamos una opción al usuario
        opcion_menu = input("Ingresa la opción y luego pulsa <INTRO> >> ")
    
        if opcion_menu=="1":
            importar()
        elif opcion_menu=="2":
            listar()
        elif opcion_menu=="3":
            informes()
        elif opcion_menu=="9":
            break
        else:
            print ("")
            input("La opción elegida es incorrecta...\nPulsa una tecla para continuar")

        print("El programa ha finalizado")




