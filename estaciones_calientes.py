from collections import Counter
import csv
import datetime

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

print("Las 3 estaciones de bicicleta más utilizadas en horario matutino en Buenos Aires: ")
for estacion, numero in counter.most_common(3):
    print(f"Estación: '{estacion}' - número de usuarios: '{numero}'")