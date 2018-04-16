import os

print("Leer un archivo")
print("---------------")
print("Lista de archivos disponibles")
os.system("dir")
print("")
archivo = raw_input("Ingrese nombre de archivo que desea leer(incluir extension): ")
#print(archivo)

archivo = open(archivo, 'r')
archivo1 = archivo.read()
#archivo = archivo.readline()  leer una linea
print archivo1


#lectura = open(archivo, "r")
#leer = lectura.read()
#print(leer)