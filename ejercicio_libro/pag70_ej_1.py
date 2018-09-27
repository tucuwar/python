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
    tam = len(usuario)
    alfanum = usuario.isalnum()
    
    if tam >= 6: 
        print ("tam mayor igual que 6 - OK")
        if tam <= 12:
            print ("tam menor igual que 12 - OK")
            check1 = True
        else: 
            print ("El nombre de usuario no puede contener más de 12 caracteres")
            check1 = False
            #return
    else: 
        print ("El nombre de usuario debe contener al menos 6 caracteres")
        return
        
    if alfanum is True:
        print ("Cadena alfanumerica")
        check2 = True
    else: 
        print ("El nombre de usuario puede contener solo letras y números")
        check2= False
        #return

    valida = bool(check1) == bool(check2)
    print valida
    raw_input("Pulsa una tecla para continuar...sale")     
        
                

print ("Ingrese usuario y contraseña")
print (""" Recuerde:
        El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
        El nombre de usuario puede ser alfanumérico
        """)

usuario = raw_input("Usuario: ")
password = raw_input("Contraseña: ")
validaUsr(usuario)