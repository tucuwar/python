# -*- coding: utf-8 -*-
#Curso Python para Principiantes - Eugenia Bahit

# pagina 70
# ejercicio 2
# Crear un módulo para validación de contraseñas. Dicho módulo, deberá cumplir con
#  los siguientes criterios de aceptación:
# La contraseña debe contener un mínimo de 8 caracteres
# Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos
#  1 carácter no alfanumérico
# La contraseña no puede contener espacios en blanco
# Contraseña válida, retorna True
# Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”

import re

def validaPass(password):
    tam = len(password)
    check_tam = False
    check_space = False
    check_mayus = False
    check_minus = False
    check_num = False
    check_noalfanum = False
    noalfanum = re.compile(r'[\W.%+-]') # valido caracteres especiales no alfanumericos
    pwd = noalfanum.search(password)    # pwd guardo resultado en variable
   
    if not tam >= 8:
        print ("La contraseña debe tener un largo de 8 caracteres")
    else:
        check_tam = True
        print ("pass 8 - OK")
    
    #print ("verifica que no existan espacios en blanco")
    for x in password: # verifica que no existan espacios en blanco
        z = x.isspace()
        
        if z is True:
            print ("La contraseña no puede contener espacios en blanco")
            check_space = True
        else: print ("Contraseña SIN espacios en blanco - OK")
                
    #print ("verifica que exista al menos una letra mayuscula")        
    for x in password: # verifica que exista al menos una letra mayuscula
        z = x.isupper()
        print x
        if z is True:
            print ("Contraseña contiene una mayuscula al menos - OK")
            check_mayus = True
        else: print ("La contraseña debe contener una letra mayuscula") 

    #print ("verifica que exista al menos una letra minuscula") 
    for x in password: # verifica que exista al menos una letra minuscula
        z = x.islower()
        print z
        if z is True:
            #print ("Contraseña contiene una minuscula al menos - OK")
            check_minus = True
        else: print ("La contraseña debe contener una letra minuscula") 

    #print ("verifica que exista al menos un numero") 
    for x in password: # verifica que exista al menos un numero
        z = x.isdigit()
        print z
        if z is True:
            #print ("Contraseña contiene un numero al menos - OK")
            check_num = True
        else: print ("La contraseña debe contener al menos un numero") 
    
    if pwd is None:
        print ("Faltan caracteres especiales")
    else:
        check_noalfanum = True
    
    check_letras = bool(check_mayus) and bool(check_minus)
    check_num_space = bool(check_num) and bool(not check_space)
    check_noalfanum_tam = bool(check_tam) and bool(check_noalfanum)
    check = (bool(check_letras) and bool(check_num_space)) and bool(check_noalfanum_tam)

    #print (" ")
    #print ("check_letras = check_mayus == check_minus")
    #print check_letras, check_mayus, check_minus
    #print (" ")
    #print "check_num_space = check_num == check_space"
    #print check_num_space, check_num, check_space
    #print (" ")
    #print "check_noalfanum_tam = check_tam == check_noalfanum"
    #print check_noalfanum_tam, check_tam, check_noalfanum
    #print ("RESULTADO")
    #print "check = (check_letras == check_num_space) == (check_tam)"
    #print check, check_letras, check_num_space, check_noalfanum_tam
    
    if check is True:
        print ("La PASSWORD es segura") 
    else: print ("La PASSWORD elegida no es segura")
    
    return check
    
    
print ("Ingrese usuario y contraseña")
print (""" Recuerde:
        La contraseña debe contener un mínimo de 8 caracteres.
        Debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
        La contraseña no puede contener espacios en blanco.
        """)

usuario = raw_input("Usuario: ")
password = raw_input("Contraseña: ")
validaPass(password)