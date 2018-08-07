# -*- coding: utf-8 -*-

### Seguimiento de los cambios del dolar 

#webs referencia
# https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html

#Librerias:
# pip install matplotlib

import matplotlib.pyplot as plt  
import numpy as np
from pylab import *


#El argumento --pylab hace que al iniciar 
# la sesión se carguen los módulos matplotlib.pylab 
# y NumPy con los alias mpl y np, respetivamente.


#fecha = raw_input("Ingrese semana: dd al dd de MM/AAAA")


#dolar_compra = [28.3, 28.2, 28.6, 28.8, 28.7]
#dolar_venta = [26.1, 25.8, 26.9, 27.1, 27.2]

dolar_compra = []
dolar_venta = []
dolar_dia = ["Lun", "Mar", "Mie", "Jue", "Vie"]



plt.title(raw_input("Fecha: "))     # Establece el título del gráfico   
print("Ingrese los valores del Dolar en la semana establecida")

for d in dolar_dia:
    print("Valor Dolar día %s. ")%(d)
    c = float(raw_input("Comprador: "))
    v = float(raw_input("Vendedor: "))
    dolar_compra.append(c)
    dolar_venta.append(v)
    print (" ")


#plt.xlabel("Valor dolar")          # Establece el título del eje x = abscisa
#plt.ylabel("Días de la semana")    # Establece el título del eje y = ordenada

print("Comprador",dolar_compra)
print("Vendedor",dolar_venta)

raw_input("Pulsa una tecla para continuar...")

plt.plot(dolar_compra, marker='x', linestyle='-', color='b',  label = "Dolar Comprador")    # Dibuja el gráfico
plt.plot(dolar_venta, marker='x', linestyle='--', color='r',  label = "Dolar Vendedor")     # Dibuja el gráfico
plt.grid(True)                      # Activa cuadrícula del gráfico pero no se muestra

# EJE DE X abscisa
indice = np.arange(5)               # Declara un array
plt.xticks(indice, ("L", "M", "Mi", "J", "V")) 

plt.legend()
plt.show()

