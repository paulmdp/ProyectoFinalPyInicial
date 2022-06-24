# Proyecto Invernadero -  Alumno: Pablo D. Fiore

![Img Invernadero](img/inverna.png)

Contacto: pablofiore@gmail.com\
Web: [Perfil LinkedIn] https://www.linkedin.com/in/pablo-fiore-22774013

# 🍅Proyecto Final - Curso Python Inicial

Con este ejercicio final, se busca afianzar los siguientes conceptos aprendidos en el curso **Python Inicial**
- Variables
- Control de Flujo — Condicionales y Bucles
- Funciones
- Manejo de Diccionarios
- Manejo de archivos

## - Descripción del proyecto
### -- Contexto de la idea y selección del problema a resolver.
  Durante la pandemia de Covid-19, tuve un requerimiento por parte de un ingeniero agrónomo de su necesidad de obtener datos de las temperaturas y niveles de humedad
  que se registran dentro de un invernadero de cultivo a su cargo, como también el volumen de agua vertido en el cultivo durante períodos delimitados.
  
  Atendiendo este requerimiento diseñé y construí un dispositivo que mide y registra estos datos mediante tres sensores de temperatura y humedad ambiente, otros tres
  sensores capacitivos de humedad de suelo y un caudalímetro de sensor magnético.
  
  El sistema sensa y procesa los datos desde dos placas Arduino, almacenando registros cada tanto tiempo, de acuerdo a la frecuencia de muestreo requerida. 
  Estos registros son almacenados en dos tarjetas de memoria SD, una para los registros de temperatura y humedad en ambiente y suelo, y en la otra tarjeta SD se 
  almacena volumen de agua y caudal máximo registrado en un lapso de tiempo de riego continuo. Todos estos registros almacenan fecha y hora en que se sensaron los
  valores.
  
### -- Objetivos

  Diseñar y construir un programa que permita:

- Importar los datos almacenados en las tarjetas de memoria SD incorporando esa información a dos archivos maestros en el disco duro de la computadora donde esté
  corriendo el programa.

- Visualizar los registros individuales almacenados en dichos archivos maestros.

- Procesar estos registros y generar informes de valores máximos, mínimos y promedios; brindando esa información al operador para la toma de desiciones.

### -- Estructura y organización de los datos

Los datos recolectados en el dispositivo se encuentran en dos memorias SD separadas, una contiene el archivo dataTH.csv y la otra contiene el archivo dataCA.csv.
Cada dos semanas se deben quitar de los dispositivos estas tarjetas de memoria, traspasar los registros a una computadora para su análisis y eliminar los archivos de las tarjetas SD para que se generen los nuevos datos. 

**Para el archivo dataTH.csv se estima una cantidad aproximada de 1350 registros con la siguiente estructura:**

num_registro, (Número del registro generado, inicia desde el registro 1)

hora_registro, (Hora del registro en formato hh:mm)

fecha_registro, (Fecha del registro en formato dd/mm/aaaa)

sensor_T01, (Temperatura en °C registrada por el sensor de ambiente 1)

sensor_T02, (Temperatura en °C registrada por el sensor de ambiente 2)

sensor_T03, (Temperatura en °C registrada por el sensor de ambiente 3)

sensor_H01, (Humedad relativa en porcentaje registrada por el sensor de ambiente 1)

sensor_H02, (Humedad relativa en porcentaje registrada por el sensor de ambiente 2)

sensor_H03, (Humedad relativa en porcentaje registrada por el sensor de ambiente 3)

cap_H01, (Humedad relativa en porcentaje registrada por el sensor de suelo 1)

cap_H02, (Humedad relativa en porcentaje registrada por el sensor de suelo 2)

cap_H03, (Humedad relativa en porcentaje registrada por el sensor de suelo 3)


**Para el archivo dataCA.csv se estima una cantidad aproximada de 30 registros con la siguiente estructura:**

num_registro, (Número del registro generado, inicia desde el registro 1)

hora_registro, (Hora del registro en formato hh:mm)

fecha_registro, (Fecha del registro en formato dd/mm/aaaa)

caudal_max, (Caudal máximo registrado durante el lapso de riego)

volumen_lts, (El volumen en litros aplicado durante el lapso de riego)

### -- Flujo de entrada de datos

El programa deberá crear dos archivos en la unidad de disco duro de la computadora, masterTH.csv y masterCA.csv. En estos archivos se irán agregando los registros extraidos desde los archivos dataTH.csv y dataCA.csv respectivamente desde las memorias SD. Para ello el operador deberá indicarle al programa el nombre y la ubicación
de estos archivos al momento de importarlos a los master.

### -- Procesamiento de los datos

El programa deberá calcular a partir de estos registros, la siguiente información:

Valor máximo y mínimo de temperatura registrada por cada uno de los 3 sensores ambiente, comprendidos en un lapso de tiempo ingresado por el operador.

Valor máximo y mínimo de humedad registrada por cada uno de los 3 sensores ambiente, comprendidos en un lapso de tiempo ingresado por el operador.

Valor promedio de temperaturas registrada por cada uno de los 3 sensores ambiente, comprendidos en un lapso de tiempo ingresado por el operador.

Valor promedio de humedad relativa registrada por cada uno de los 3 sensores ambiente, comprendidos en un lapso de tiempo ingresado por el operador.

### -- Flujo de salida de la información 

La información generada se mostrará por pantalla desde la consola de ejecución.


## Escalabilidad del sistema

La idea y el diseño de este sistema fue pensado en función de ser escalado a medida que avancemos en los conocimientos del lenguaje python y sus herramientas de
programación.

En base a esto, se prevee agregar interface gráfica a futuro para visualizar la información mediante gráficos estadísticos y la visualización en tiempo real de 
los datos generados en tiempo real mediante conexión a la internet transformandolo en una aplicación IOT.


## - Diagramas descriptivos del proyecto

![Img Diagrama](img/diag02.png)
