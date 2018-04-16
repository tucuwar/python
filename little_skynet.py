
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

#Primera interacciÃ³n. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interacciÃ³n. Solicitamos el ingreso del aÃ±o, y utilizamos este
#dato para estimar la edad de la persona. Â¿Por quÃ© decimos que solo estamos "estimando" su edad?
#Â¿QuÃ© ocurre si eliminamos la conversiÃ³n a tipo de dato 'int' de la siguiente lÃ­nea?
agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2017-agno-1
print()

#Tercera interacciÃ³n. Solicitamos la estatura, medida en metros.
#Utilizamos la conversiÃ³n a 'int', y una expresiÃ³n para convertir esto
#a una medida en metros y centÃ­metros
estatura = float(input("Cuentame más de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacciÃ³n. Consultamos cuÃ¡ntos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()
print("Completar los siguientes datos adicionales")
sexo = input("Escribe tu sexo: ")
tel = input("Cual es tu número de teléfono: ")
ciudad = input("En que ciudad vives: ")
print()
print("Datos complementarios de " + nombre)
print("sexo: "+sexo)
print("Tel: "+tel)
print("Ciudad: "+ciudad)


#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

def menu1():
    print("")
    print("================================")
    print("Menu de Opciones")
    print("1 - Modificar Nombre")
    print("2 - Escribir un mensaje nuevo")
    print("S -  Salir")
    print("================================")


while continuar:
    menu1()
    opt_menu=input("Opcion: ")

    if opt_menu == "1":
        nombre=input("Ingrese nuevo nombre: ")
        print("")
        print("Su nuevo nombre es "+ nombre)

    elif opt_menu == "2":
        mensaje = input("Vamos a publicar un nuevo mensaje. ¿Que piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    elif opt_menu == "S" or opt_menu == "s":
        continuar = False
        #Mensaje de salida, una vez que el ciclo ha terminado.
        print("Gracias por usar Mi Red. ¡Hasta pronto!")

