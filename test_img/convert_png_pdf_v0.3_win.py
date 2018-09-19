# -*- coding: utf-8 -*-

import os
from PIL import Image
import easygui as eg
#from fpdf import FPDF
from PyPDF2 import PdfFileMerger

# v0.3 22/03/2018 
# autor: Carlos Alvarez Toledo
# Ministerio de Desarrollo Soial - Tucumán

### fue necesario instalar: 
#v0.0 para convertir imagenes a pdf     # sudo pip install Pillow 
#v0.1 para manejo de ventanas           # sudo pip install easygui 
#v0.1 para manejo de ventanas           # sudo apt-get install python-tk
#v0.2 varias imagenes a pdf             #sudo apt-get install imagemagick    #convert images.jpeg png.png tux.jpg imagenes.pdf
#v0.2 varios pdf a uno solo             # sudo pip install PyPDF2 para MODO CARPETA    #https://steemit.com/spanish/@sethroot/el-poder-de-python-pegar-varios-pdfs-en-1-solo-pdf-learning

# NO FUE USADO: sudo pip install fpdf #v0.2 para MODO CARPETA #https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

#v0.3 CORREGIR
# ModoCarpeta(): falta ordenar archivos(hojas) en pdf resultado


#Opciones de MENU:
# MODO IMG-PDF: Por CADA archivo de la CARPETA convierte un archivo pdf
# MODO CARPETA: todos los arcvhios que se encuentren en la carpeta se concatenan en un solo PDF
# MODO SELECCION MULTIPLE: permite seleccionar los archivos para luego concatenarlos en un solo PDF

def ModoImgPdf():
    ### Convierte a pdf CADA ARCHIVO de imagen que encuentra
    directorio = eg.diropenbox(msg="Abrir directorio:",
                               title="Seleccionar Carpeta",
                               default='')
    eg.msgbox(directorio, "diropenbox", ok_button="Continuar")
    for dirName, subDirList, fileList in os.walk(directorio):
        for fname in fileList:
            ruta_archivo = dirName+"/"+fname
            im = Image.open(ruta_archivo)
            if im.mode == "RGBA":
                im = im.convert("RGB")
            #destination = ruta+nombre de cada archivo(sin extension) + .pdf
            destination = os.path.splitext(ruta_archivo)[0] +".pdf"
            im.save(destination,"PDF",resolution=100.0)

def ModoCarpeta():
    ### falta ordenar archivos(hojas) en pdf resultado
    pdfs = []
    merger = PdfFileMerger()
    directorio = eg.diropenbox(msg="Abrir directorio:",
                               title="Seleccionar Carpeta",
                               default='')
    eg.msgbox(directorio, "diropenbox", ok_button="Continuar")
    for dirName, subDirList, fileList in os.walk(directorio):
        for fname in fileList:
            ruta_archivo = dirName+"/"+fname
            im = Image.open(ruta_archivo)
            if im.mode == "RGBA":
                im = im.convert("RGB")
            #ruta_archivo_pdf = dirName+"/"+fname+".pdf"
            destination = os.path.splitext(ruta_archivo)[0] +".pdf"
            im.save(destination,"PDF",resolution=100.0)
            ###Convertimos los pdfs a un solo pdf
            pdfs.append(destination)
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(directorio + "/RESOLUCION.pdf")
    #raw_input("Pulsa una tecla para continuar...")
    
def ModoSelect():
    ### El pdf resultado queda ordenado por nombre de archivos incluidos
    merger = PdfFileMerger()
    pdfs_select = [] #guardo los archivos seleccionados en la lista
    extension = ["*.jpeg","*.png","*.jpg"]  
    archivos = eg.fileopenbox(msg="Seleccionar archivos",
                            title="Control: fileopenbox",
                            default='',
                            filetypes=extension,
                            multiple=True)
    eg.msgbox(archivos, "Lista de Archivos", ok_button="Convertir")
    # la lista archivos contiene los elementos con la ruta de cada archivo
    for fname in archivos:
            im = Image.open(fname)
            if im.mode == "RGBA":
                im = im.convert("RGB")
            ruta_archivo_pdf = fname +".pdf"
            im.save(ruta_archivo_pdf,"PDF",resolution=100.0)
            ###Convertimos los pdfs a un solo pdf
            pdfs_select.append(ruta_archivo_pdf)
    #destination = ruta del archivo
    destination = os.path.split(fname)[0]
    #raw_input("Pulsa una tecla para continuar...")   
    for pdf in pdfs_select:
        merger.append(pdf)
    merger.write(destination +"/RESOLUCION.pdf")
    
    

def menu():
    print("")
    os.system('cls')
    
    print("+============== Convertir imagenes a PDF ==============+") 
    print("| 1 - Convertir CADA archivo de imagen de la CARPETA   |")
    print("| 2 - Convertir Modo CARPETA                           |")
    print("| 3 - Convertir en Modo SELECCION MULTIPLE             |")
    print("| 0 - Salir                                            |")
    print("+======================================================+")

while True:
    menu()
    opt_menu=raw_input("Opcion: ")
    if opt_menu == "1":
        print "Modo Img-Pdf"
        print "Por cada archivo de imagen convierte un archivo pdf"
        print " "
        ModoImgPdf()
    if opt_menu == "2":
        print "Modo Carpeta"
        print "Convierte todos los arcvhios que se encuentren en la carpeta en un solo PDF"
        print "El nombre del archivo es RESOLUCION.pdf"
        print " "
        ModoCarpeta()
    elif opt_menu == "3":
        print "Modo Selección Múltiple"
        print "Permite seleccionar los archivos para luego convertirlos en un solo PDF"
        print " "
        ModoSelect()
    elif opt_menu == "0":
        print "Programa terminado - Exit"
        break

#codigo original jpeg/jpg/png a pdf
#filename = "./test_img/images.jpeg"
#im = Image.open(filename)
#if im.mode == "RGBA":
#    im = im.convert("RGB")
#new_filename = "./test_img/images.pdf"
#if not os.path.exists(new_filename):
#    im.save(new_filename,"PDF",resolution=100.0)