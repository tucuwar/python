# -*- coding: utf-8 -*-

### Seguimiento de los cambios del dolar 

#Librerias:
# pip install matplotlib

import matplotlib.pyplot as plt  
import numpy as np
from pylab import *


#El argumento --pylab hace que al iniciar 
# la sesión se carguen los módulos matplotlib.pylab 
# y NumPy con los alias mpl y np, respetivamente.



dolar_compra = [28.3, 28.2, 28.6, 28.8, 28.7]
dolar_venta = [26.1, 25.8, 26.9, 27.1, 27.2]

#dolar_dia = [L, M, Mi, J, V]
  
#plt.title("Título")    # Establece el título del gráfico
#plt.xlabel("abscisa")  # Establece el título del eje x 
#plt.ylabel("ordenada") # Establece el título del eje y

#plt.plot(dolar_compra)  # Dibuja el gráfico
#plt.plot(dolar_venta)  # Dibuja el gráfico

plt.plot(dolar_compra, label = "Dolar Comprador")
plt.plot(dolar_venta, label = "Dolar Vendedor")
plt.legend()

plt.show()