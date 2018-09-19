import os
from PIL import Image
import easygui as eg

### fue necesario instalar: 
# sudo pip install Pillow           #v0.0 para convertir imagenes a pdf
# sudo pip install easygui          #v0.1 para manejo de ventanas
# sudo apt-get install python-tk    #v0.1 para manejo de ventanas 

# Utiliza ventana para seleccionar archivo 1 archivo

extension = ["*.jpeg","*.png","*.jpg"]
 
print("Seleccionar archivo para convertir a PDF ")
print("-----------------------------------------")

archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='./test_img/',
                         filetypes=extension)
                           
eg.msgbox(archivo, "fileopenbox", ok_button="Convertir")

#os.system("ls ./test_img/")
##os.system("dir ./test_img/")
#print("")
#archivo = raw_input("Ingrese nombre de archivo que desea convertir(incluir extension): ")

#filename = "./test_img/%s" %(archivo)

im = Image.open(archivo)
if im.mode == "RGBA":
    im = im.convert("RGB")

archivo = im
extension_pdf = ["*.pdf"]
archivo = eg.filesavebox(msg="Guardar archivo",
                         title="Control: filesavebox",
                         default='./test_img/',
                         filetypes=extension_pdf)
                           
eg.msgbox(archivo, "filesavebox", ok_button="guardar")

im.save(archivo,"PDF",resolution=100.0)

#nombre_nuevo = raw_input("Ingrese nuevo nombre (sin extension): ")
#new_filename = "./test_img/%s.pdf" %(nombre_nuevo)
#if not os.path.exists(new_filename):
#    im.save(new_filename,"PDF",resolution=100.0)

#print("")
#os.system("ls ./test_img/")





#archivo = open(archivo, "r")
#archivo = archivo.read()
##archivo = archivo.readline()  leer una linea
#print (archivo)


#codigo original jpeg/jpg/png a pdf
#filename = "./test_img/images.jpeg"
#im = Image.open(filename)
#if im.mode == "RGBA":
#    im = im.convert("RGB")
#new_filename = "./test_img/images.pdf"
#if not os.path.exists(new_filename):
#    im.save(new_filename,"PDF",resolution=100.0)