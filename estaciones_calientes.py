""" Ejercicio 2 * Estaciones calientes * Lambda

Consigna:
    Hacer un programa que analice el archivo de recorridos de Bicicletas de la Ciudad y devuelva las tres
    estaciones de origen más “calientes” (de las que salen más recorridos) en la mañana (de 6 a 11:59).

Este script lee el archivo 'trips_2021.csv' que contiene información del uso de bicicletas en el sistema
de CABA, disponible en 'https://data.buenosaires.gob.ar/dataset/bicicletas-publicas'. La información
es analizada y se imprimen las 3 estaciones de las que parten más viajes en horario matutino (de 6 a 11:59 hrs).
Se utilizan el módulo 'csv' para cargar y leer del archivo .csv, el módulo 'datetime' para convertir la fecha tipo string
en un objeto datetime y el contenedor 'Counter' para obtener las estaciones más usadas a partir de la cuenta realizada.
 """

from collections import Counter
import csv
import datetime

def estaciones_calientes(n):
    """Analiza el archivo .csv y devuelve las 'n' estaciones más "calientes" en horario matutino.
    
    Args:
        n: número de estaciones que deseamos que nos devuelva.
    Returns:
        Devuelve un diccionario con 'n' elementos que informan el 
        nombre de la estación y la cantidad de usuarios que partieron de las mismas.
    """
    with open('trips_2021.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        cantidad_usos_matutinos = dict()
        for row in csv_reader:
            nombre_estacion_origen = row['nombre_estacion_origen']
            datetime_str = row['fecha_origen_recorrido']
            datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z')
            if 6 <= datetime_obj.hour < 12:
                try:
                    cantidad_usos_matutinos[nombre_estacion_origen] += 1
                except KeyError:
                    cantidad_usos_matutinos[nombre_estacion_origen] = 1

    counter = Counter(cantidad_usos_matutinos)

    return counter.most_common(n)



dicc_estaciones_calientes = estaciones_calientes(3)
print("Las 3 estaciones de bicicleta más utilizadas en horario matutino en Buenos Aires: ")
for estacion, numero in dicc_estaciones_calientes:
    print(f"Estación: '{estacion}' - número de usuarios: '{numero}'")