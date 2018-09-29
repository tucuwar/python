# -*- coding: utf-8 -*-
#Curso Python para Principiantes - Eugenia Bahit

# pagina 70
# ejercicio 3

#Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y
#que los valide utilizando los módulos generados en los dos ejercicios anteriores.
#Ayuda: para contar la cantidad de caracteres de una cadena, en Python se utiliza la
#función incorporada: len(cadena)

import pag70_ej_1 as u 
import pag70_ej_2 as p 


print ("Ingrese usuario y contraseña")
print (""" Recuerde:
        El nombre de usuario:
                            debe contener un mínimo de 6 caracteres y un máximo de 12.
                            puede ser alfanumérico.

        La contraseña debe contener:
                            un mínimo de 8 caracteres.
                            letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
                            y no puede contener espacios en blanco.
        """)

usuario = raw_input("Usuario: ")
password = raw_input("Contraseña: ")
user = u.validaUsr(usuario)   #  Guardo el resultado de la funcion que valida usuario
pwd = p.validaPass(password)  #  Guardo el resultado de la funcion que valida password


if (user and pwd) is True:
    print ("Usuario y Contraseña - Aceptado")
else: print ("Usuario o Contraseña mal formado")

