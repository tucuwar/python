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

def validaPass(password):
    tam = len(password)
    check_tam = False
    check_space = False
    check_mayus = False
    check_minus = False
    check_num = False

    if not tam >= 8:
        print ("La contraseña debe tener un largo de 8 caracteres")
        #return
    else:
        check_tam = True
        print ("pass 8 - OK")
    print (" ")
    
    #check_space = password.isspace() # verifica que la pass no sea SOLO espacios en blanco
    #if check_space is not True:
    #    print ("La contraseña no puede ser solo espacios en blanco")
    #    return
    print (" ")
    print ("verifica que no existan espacios en blanco")
    for x in password: # verifica que no existan espacios en blanco
        z = x.isspace()
        
        if z is True:
            print ("La contraseña no puede contener espacios en blanco")
            check_space = True
            #return            
        else:
            print ("Contraseña SIN espacios en blanco - OK")
            
            
    
    print (" ")
    print ("verifica que exista al menos una letra mayuscula")        
    for x in password: # verifica que exista al menos una letra mayuscula
        z = x.isupper()
        print x
        if z is True:
            print ("Contraseña contiene una mayuscula al menos - OK")
            check_mayus = True
            #break # sale del CICLO del FOR
        else: 
            print ("La contraseña debe contener una letra mayuscula") 
            #check_mayus = False

    print (" ")
    print ("verifica que exista al menos una letra minuscula") 
    for x in password: # verifica que exista al menos una letra minuscula
        z = x.islower()
        print z
        if z is True:
            print ("Contraseña contiene una minuscula al menos - OK")
            check_minus = True
            #break # sale del CICLO del FOR
        else: 
            print ("La contraseña debe contener una letra minuscula") 
            #check_minus = False

    print (" ")
    print ("verifica que exista al menos un numero") 
    for x in password: # verifica que exista al menos un numero
        z = x.isdigit()
        print z
        if z is True:
            print ("Contraseña contiene un numero al menos - OK")
            check_num = True
            #break # sale del CICLO del FOR
        else: 
            print ("La contraseña debe contener al menos un numero") 
            #check_num = False
    
    #print ("antes", check_space)
    check_letras = bool(check_mayus) and bool(check_minus)
    check_num_space = bool(check_num) and bool(not check_space)
    #check_noalfanum_tam = bool(check_tam) == bool(check_noalfanum)

    check = (check_letras and check_num_space) and bool(check_tam)
    print (" ")
    print ("check_letras = check_mayus == check_minus")
    print check_letras, check_mayus, check_minus
    print (" ")
    print "check_num_space = check_num == check_space"
    print check_num_space, check_num, check_space
    print (" ")
    print "check = (check_letras == check_num_space) == (check_tam)"
    print check, check_letras, check_num_space, check_tam
    


    #print check_letras
    #print check_num_space
    #print check_tam
    #check = ( (bool(check_mayus) == bool(check_minus)) == (bool(check_num) == bool(not check_space)) ) == bool(check_tam)
    #print check
    if check is True:
        print ("La PASSWORD es segura") 
    else: print ("La PASSWORD elegida no es segura")


    
    print ("sigue por aqui")

    # abcAabc





### import re
# pattern = re.compile("\d+(\.{1}\d+){0-1}")
# cadena = "2342asdads1223"
# cadena_1 = 12312
# cadena_2 = 12.09

# pattern.match(cadena), devuelve un objeto None, pues la expresion regular dicta:

#  \d+ --> uno a mas digitios
#  (\.{1}\d+){0-1} --> {0-1} lo que esta entre parentesis puede aparecer solo una vez, si aparece dentro del paretesis:
#  (\.{1}\d+) un punto y 1 mas digitos.
#  por supuesto, las cadenas : cadena_1 y cadena_2, van a a matchear. Eso te ahorra el tedioso trabajo de iterar, si el numero es muy grande vas a consumir mucha mas memoria y tiempo. Esta solucion, tambien itera por supuesto, pero cuando python itera por nosotros lo hace mucho mas rapido.


print ("Ingrese usuario y contraseña")
print (""" Recuerde:
        La contraseña debe contener un mínimo de 8 caracteres.
        Debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
        La contraseña no puede contener espacios en blanco.
        """)

usuario = raw_input("Usuario: ")
password = raw_input("Contraseña: ")
validaPass(password)