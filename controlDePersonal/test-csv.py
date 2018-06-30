# -*- coding: utf-8 -*-

import csv
import os
import easygui as eg
import pandas as pd   #sudo pip install pandas - para ordenar el listado





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
        print ("===========INICIO DE LISTADO CRUDO=============")
        for reg in entrada:
            print(reg)  # Cada línea se muestra como una lista de campos
        print ("===========FIN DE LISTADO=============")
        print(" ")
        print("LISTADO ORDENADO POR AC-No ")
        #Listado ordenado con PANDAS
        movies = pd.read_csv(archivo)
        movies = movies.sort_values(['AC-No.'], ascending=True)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        #movies = pd.read_csv('Top20_Media_Yesterday.csv', nrows=21)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        print movies
        print("FIN LISTADO ORDENADO POR AC-No ")
        print(" ")
    csvarchivo.close()
    raw_input("Pulsa una tecla para continuar...")

def ModoControlAsistencia():
    ### Abre ventana para seleccionar csv ¡¡ UN SOLO DIA !!
    extension = ["*.csv"]  
    archivo = eg.fileopenbox(msg="Seleccionar archivo de Asistencia",
                            title="Control: fileopenbox",
                            default='',
                            filetypes=extension,
                            multiple=False)
    eg.msgbox(archivo, "Lista de Archivos", ok_button="Seleccionar")
    
    #Abre archivo csv
    with open(archivo) as csvarchivo:
        #entrada = csv.reader(csvarchivo)
        #print ("===========INICIO DE LISTADO CRUDO=============")
        #for reg in entrada:
        #    print(reg)  # Cada línea se muestra como una lista de campos
        #print ("===========FIN DE LISTADO=============")
        #print(" ")
        print("LISTADO ORDENADO POR Fecha:Hora ")
        #Listado ordenado con PANDAS
        listado_hora = pd.read_csv(csvarchivo)
        listado_hora = listado_hora.sort_values(['Marc.'], ascending=False)
        print listado_hora
        print("FIN LISTADO ORDENADO POR Fecha:Hora ")
        print(" ")
    csvarchivo.close()
    raw_input("Pulsa una tecla para continuar...")
    
# Test de lectura de archivo csv
#with open('asistencia201806_24_26m.csv') as csvarchivo:
#    entrada = csv.reader(csvarchivo)
#    for reg in entrada:
#        print(reg)  # Cada línea se muestra como una lista de campos


def menu():
    os.system('clear')
    print("")
    print chr(27)+"[1;41m"+"===========Control de Asistencia============"+chr(27)+"[0m"
    print("1 - Cargar archivo .CSV de asistencia")
    print("2 - Control asistencia")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("0 - Salir")
    print chr(27)+"[1;41m"+"==========================================="+chr(27)+"[0m"

while True:
    menu()
    opt_menu=raw_input("Opcion: ")
    if opt_menu == "1":
        print "Cargar archvio .CSV de Asistencia"
        ModoSelectCSV()
        raw_input("Pulsa una tecla para continuar...") 
    elif opt_menu == "2":
        print "Control Asistencia "
        ModoControlAsistencia()
        raw_input("Pulsa una tecla para continuar...") 
    elif opt_menu == "3":
        print " "
        
    elif opt_menu == "4":
        print " "
        
    elif opt_menu == "5":
        print " "
        
    elif opt_menu == "6":
        print " "  
       
    elif opt_menu == "7":
        print " "  
       
    elif opt_menu == "8":
        print " "
        
    elif opt_menu == "9":
        print " "

    elif opt_menu == "0":
        #Mensaje de salida, una vez que el ciclo ha terminado.
        print "Programa terminado - Exit"
        break

