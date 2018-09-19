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
        list_order_ACNo = pd.read_csv(archivo)
        list_order_ACNo = list_order_ACNo.sort_values(['AC-No.'], ascending=True)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        #movies = pd.read_csv('Top20_Media_Yesterday.csv', nrows=21)
        #movies = movies.to_csv("Top20_Media_Yesterday.csv")
        print list_order_ACNo
        print("FIN LISTADO ORDENADO POR AC-No ")
        print(" ")
    csvarchivo.close()
    #raw_input("Pulsa una tecla para continuar...")

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
        print("LISTADO ORDENADO POR Fecha:Hora ")
        #Listado ordenado con PANDAS
        listado_hora = pd.read_csv(csvarchivo, header=0) #header=0 para ordenar los index
        listado_hora = listado_hora.pd.to_datetime(csvarchivo)
        #listado_hora = listado_hora.sort_values(['Marc.'], ascending=False)  #AC-No.
        print listado_hora
        print("FIN LISTADO ORDENADO POR Fecha:Hora ")
        print(" ")
        #print (listado_hora(['Nombre'])
        #print (listado_hora.ix[0:10])
        #print (listado_hora.sort_values(by='Marc.', ascending=True))
    csvarchivo.close()
    #raw_input("Pulsa una tecla para continuar...")
    
# Test de lectura de archivo csv
#with open('asistencia201806_24_26m.csv') as csvarchivo:
#    entrada = csv.reader(csvarchivo)
#    for reg in entrada:
#        print(reg)  # Cada línea se muestra como una lista de campos

def abm_listado_personal():
    ### Carga un csv con TODO el personal, permite ABM sobre registros
    extension = ["*.csv"]  
    listapersonal = eg.fileopenbox(msg="Seleccionar archivo de PERSONAL",
                            title="Control: fileopenbox",
                            default='',
                            filetypes=extension,
                            multiple=False)
    eg.msgbox(listapersonal, "Lista de Personal: AC-No y Apellido_Nombre", ok_button="Seleccionar")
    #Abre archivo csv
    with open(listapersonal) as csvarchivo_personal:
        print("LISTADO DE  PERSONAL ")
        #Listado ordenado con PANDAS
        csvarchivo_personal = pd.read_csv(csvarchivo_personal) #header=0 para ordenar los index
        csvarchivo_personal = csvarchivo_personal.sort_values(['Estado'], ascending=True)
        print csvarchivo_personal
        print("FIN LISTADO ")
        


def menu():
    os.system('clear')
    print("")
    print chr(27)+"[1;41m"+"===========Control de Asistencia============"+chr(27)+"[0m"
    print("1 - Cargar archivo .CSV de asistencia")
    print("2 - Control asistencia")
    print("3 - ")
    print("4 - ")
    print("5 - ABM Listado Personal")
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
        print "ABM Listado Personal"
        abm_listado_personal()
        raw_input("Pulsa una tecla para continuar...") 
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

