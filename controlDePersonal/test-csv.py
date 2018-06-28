# -*- coding: utf-8 -*-

import csv




# Test de lectura de archivo csv
with open('asistencia2018l.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg)  # Cada línea se muestra como una lista de campos