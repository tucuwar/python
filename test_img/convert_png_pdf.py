import os
from PIL import Image


### fue necesario instalar: 
# sudo pip install Pillow  #para convertir imagenes a pdf

 


print("Seleccionar archivo para convertir a PDF ")
print("-----------------------------------------")
os.system("ls ./test_img/")
##os.system("dir ./test_img/")
print("")
archivo = raw_input("Ingrese nombre de archivo que desea convertir(incluir extension): ")
#print(archivo)

filename = "./test_img/%s" %(archivo)
im = Image.open(filename)
if im.mode == "RGBA":
    im = im.convert("RGB")
nombre_nuevo = raw_input("Ingrese nuevo nombre (sin extension): ")
new_filename = "./test_img/%s.pdf" %(nombre_nuevo)
if not os.path.exists(new_filename):
    im.save(new_filename,"PDF",resolution=100.0)

print("")
os.system("ls ./test_img/")

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