# -*- coding: utf-8 -*-

import csv
import os
import easygui as eg
import pandas as pd
#sudo pip install pandas





def ModoSelectCSV():
    ### Abre ventana para seleccionar csv
    extension = ["*.csv"]  
    archivo = eg.fileopenbox(msg="Seleccionar archivo de Asistencia",
                            title="Control: fileopenbox",
                            default='',
                            filetypes=extension,
                            multiple=False)
    eg.msgbox(archivo, "Lista de Archivos", ok_button="Seleccionar")
    
    #Abre archivo csv
    with open(archivo) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        print ("===========INICIO DE LISTADO=============")
        for reg in entrada:
            print(reg)  # Cada línea se muestra como una lista de campos
        print ("===========FIN DE LISTADO=============")
        print(" ")
        print("LISTADO ORDENADO POR AC-No ")
        
        movies = pd.read_csv(archivo)
        movies = movies.sort_values(['AC-No.'], ascending=True)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        #movies = pd.read_csv('Top20_Media_Yesterday.csv', nrows=21)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        
        #entrada.sort()
        #print entrada
        print movies
        print("FIN LISTADO ORDENADO POR AC-No ")
        print(" ")
    csvarchivo.close()
    raw_input("Pulsa una tecla para continuar...")
    
    #Ordeno de menor a mayor los registros "AC-No."

    
print ("BIENVENIDA - MENU de OPCIONES")
ModoSelectCSV()


# Test de lectura de archivo csv
#with open('asistencia201806_24_26m.csv') as csvarchivo:
#    entrada = csv.reader(csvarchivo)
#    for reg in entrada:
#        print(reg)  # Cada línea se muestra como una lista de campos