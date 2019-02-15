# -*- coding: utf-8 -*-

datos_basicos = {
    "nombres":"Fran",
    "apellidos":"Pardo Garcia",
    "numero":"145548",
    "fecha_nacimiento":"03111980",
    "lugar_nacimiento":"Madrid, Espana",
    "nacionalidad":"Portuguesa",
    "estado_civil":"Casado"}
print ("Detalle del diccionario")
print ("=======================\n")
print ("Claves del diccionario:", datos_basicos.keys())
print ("Valores del diccionario:", datos_basicos.values())
print ("Elementos del diccionario:", datos_basicos.items())
# Ejemplo practico de los diccionarios
print ("Inscripcion de Curso")
print ("====================")
print ("Datos de participante")
print ("---------------------")
print ("Cedula de identidad:", datos_basicos['numero'])
print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
print ("=====**************************************************======")
# definimos una lista
my_list = [4, 3, 8, 9]
# añadimos el iterador a la lista
my_iter = iter(my_list)
# ahora podemos iterar con el commando next
print(next(my_iter ))
print(next(my_iter ))
print(next(my_iter ))
print(next(my_iter ))
print(next(my_iter ))