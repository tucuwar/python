# -*- coding: utf-8 -*-
def mensaje_publico():
    mensaje = raw_input("Ahora vamos a publicar un mensaje. ¿Que piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")

def mensaje_privado():
    mensaje = raw_input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Que quieres decirles? ")
    print()
    for i in range(num_amigos):
        nombre_amigo = raw_input("Ingresa el nombre de tu amigo o amiga: ")
        print("--------------------------------------------------")
        print(nombre, "dice:", "@" + nombre_amigo, mensaje)
        print("--------------------------------------------------")

def obtener_nombre():
    nombre = raw_input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    # Calculo de edad
    agno = int(raw_input("Para preparar tu perfil, dime en que anio naciste. "))
    edad = 2017-agno-1
    return edad

def obtener_genero():
    genero = raw_input("Indicar sexo (Masc. o Fem.) ")
    return genero

def obtener_pais():
    pais = raw_input("¿En que pais vives?. ")
    return pais

def obtener_estatura():
    # Calculo de estatura
    estatura = float(raw_input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    return estatura_m, estatura_cm

def obtener_amigos():
    # Cantidad de amigos
    num_amigos = int(raw_input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return num_amigos


#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
def mostrar_perfil(nombre, edad, genero, pais, estatura_m, estatura_cm, num_amigos):
    print("")
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "anios")
    print("Genero:  ", genero)
    print("Nacionalidad:  ", pais)
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
    print("")

def menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje publico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(raw_input("Ingresa una opcion: "))
    #while opcion < 0 or opcion > 4:
     #   print("No conozco la opcion que has ingresado. Intentalo otra vez.")
      #  opcion = int(raw_input("Ingresa una opcion: "))
    return opcion

def bienvenida():
    print("Bienvenido a ... ")
    print("""

     _______  _                 _        _______ _________
    (  ____ \| \    /\|\     /|( (    /|(  ____ \\__   __/
    | (    \/|  \  / /( \   / )|  \  ( || (    \/   ) (
    | (_____ |  (_/ /  \ (_) / |   \ | || (__       | |
    (_____  )|   _ (    \   /  | (\ \) ||  __)      | |
          ) ||  ( \ \    ) (   | | \   || (         | |
    /\____) ||  /  \ \   | |   | )  \  || (____/\   | |
    \_______)|_/    \/   \_/   |/    )_)(_______/   )_(

    """)


nombre = obtener_nombre()
bienvenida()


#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    opcion = menu()

    #Codigo para la opcion 1. Publicar un mensaje.
    if opcion == 1:
        mensaje_publico()

    #Codigo para la opcion 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje_privado()

    #Codigo para la opcion 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, genero, pais, estatura_m, estatura_cm, num_amigos)

    #Codigo para la opcion 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        genero = obtener_genero()
        pais = obtener_pais()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_amigos()
        mostrar_perfil(nombre, edad, genero, pais, estatura_m, estatura_cm, num_amigos)

    #Codigo para la opcion 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")
        break

    #Codigo para la opcion que no coincida con ninguna anterior.
    else:
        print("No conozco la opcion que has ingresado. Intentalo otra vez.")

print("")
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print("")
