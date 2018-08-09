# -*- coding: utf-8 -*-

# Agenda de internos MDS
# ABM de internos

# web referencia
# https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-archivos.html
# http://chuwiki.chuidiang.org/index.php?title=Leer_y_escribir_ficheros_en_python



import locale
print(locale.getpreferredencoding())


archivo = open("agenda.txt")

archivo.write(cadena1 + '\n')


archivo.close()