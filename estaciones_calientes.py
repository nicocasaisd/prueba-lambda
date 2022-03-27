from collections import Counter
import csv
import datetime

with open('trips_2021.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    diccionario = dict()
    for row in csv_reader:
        nombre_estacion_origen = row['nombre_estacion_origen']
        datetime_str = row['fecha_origen_recorrido']
        datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z')
        if 6 <= datetime_obj.hour < 12:
            try:
                diccionario[nombre_estacion_origen] += 1
            except KeyError:
                diccionario[nombre_estacion_origen] = 1

#print(diccionario)

k = Counter(diccionario)

#print(k)
#print(k.most_common(3))

print("Las 3 estaciones de bicicleta más utilizadas en horario matutino en Buenos Aires: ")
for estacion, numero in k.most_common(3):
    print(f"Estación: '{estacion}' - número de usuarios: '{numero}'")
        
""" 

import csv

with open('trips_reducido.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["id_recorrido"]} ')
        line_count += 1
    print(f'Processed {line_count} lines.')
 """