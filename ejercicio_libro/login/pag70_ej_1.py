# -*- coding: utf-8 -*-
#Curso Python para Principiantes - Eugenia Bahit

# pagina 70
# ejercicio 1
# Crear un módulo para validación de nombres de usuarios. 
# Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:

# El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
# El nombre de usuario debe ser alfanumérico
# Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de
#  usuario debe contener al menos 6 caracteres”
# Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de
#  usuario no puede contener más de 12 caracteres”
# Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
# “El nombre de usuario puede contener solo letras y números”
# Nombre de usuario válido, retorna True


def validaUsr(usuario):
    check1 = False
    check11 = False
    check2 = False

    tam = len(usuario)
    alfanum = usuario.isalnum() # isalnum() verifica cadena alfanumerica
    
    if tam >= 6: 
        #print ("tam mayor igual que 6 - OK")
        check1 = True
        if tam <= 12:
            #print ("tam menor igual que 12 - OK")
            check11 = True
        else: 
            #print ("El nombre de usuario no puede contener más de 12 caracteres")
            check11 = False
    else: 
        #print ("El nombre de usuario debe contener al menos 6 caracteres")
        check1 = False

    if alfanum is True:
        #print ("Cadena alfanumerica")
        check2 = True
    #else: 
        #print ("El nombre de usuario puede contener solo letras y números")
    
    check_usr = (bool(check1) and bool(check11)) and bool(check2)
    
    #if check_usr is True:
    #    print ("Nombre de usuario - OK")
    #else: print ("Nombre usuario mal formado")
    
    return check_usr
    #raw_input("Pulsa una tecla para continuar...sale")     

#print ("Ingrese usuario y contraseña")
#print (""" Recuerde:
#        El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
#        El nombre de usuario puede ser alfanumérico
#        """)

#usuario = raw_input("Usuario: ")
#password = raw_input("Contraseña: ")
#validaUsr(usuario)
