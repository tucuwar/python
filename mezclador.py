# -*- coding: utf-8 -*-
#FuNCIoNES

def menu():
    print("Acciones disponibles:")
    print("  1. Mezclador de palabra")
    print("  2. Intercalar palabra")
    print("  3. Binaria")
    print("  4. Remover n")
    print("  5. Reemplazo de caracter en mayuscula")
    print("  6. Reemplazo de caracter en mayuscula - v1")
    print("  0. Salir")
    opcion = input("Ingresa una opcion: ")
    #opcion = input("Ingresa una opcion: ")
    #while opcion < 0 or opcion > 4:
     #   print("No conozco la opcion que has ingresado. Intentalo otra vez.")
      #  opcion = int(raw_input("Ingresa una opcion: "))
    return opcion

def mezclador():
    string1 = str(raw_input("Ingrese primer palabra: "))
    print("")
    string2 = str(raw_input("Ingrese segunda palabra: "))
    string11 = string1[0:2]
    print(string11)
    n2 = len(string2)
    string22 = string2[n2-2:n2]
    print(string22)
    mezcla = string11+string22
    print(mezcla)
    return mezcla

def intercalar():
    string1 = str(raw_input("Ingrese primer palabra: "))
    print("")
    string2 = str(raw_input("Ingrese segunda palabra: "))
    tam=len(string1)
    palabra1 = ""
    for c in range(0, tam):
        palabra=string1[c]+string2
        print("Contenido de palabra")
        print(palabra)
        print("")
        print("Agrupando")
        palabra1=palabra1+palabra
        print(palabra1)
        print("")
    return palabra1

def binaria():
    string = raw_input("Ingrese string binario: ")
    print("")
    tam = len(string)
    unos = 0
    ceros = 0

    for i in range(0, tam):
        print(string[i])
    print("**************")

    for i in range(0, tam):
        if string[i] == str("1"):
            unos += 1
        else:
            ceros += 1
    result = int(unos) - int(ceros)
    print(unos,"menos",ceros,"=",result)
    return result

def remover_enesimo():
    s = raw_input("Ingrese palabra: ")
    n = int(raw_input("Ingrese posicion de caracter a suprimir: "))
    print("")
    tam = len(s)
    part1 = s[0:n]
    part2 = s[n+1:tam]
    result = part1+part2
    print(result)
    return result

def reemplazo():
    cadena = raw_input("Ingrese palabra: ")
    print("")
    tam = len(cadena)
    cadena1 = ""
    for i in range(0,tam):
        if chr(32) == cadena[i]:
            cadena1 += cadena[i]
        elif cadena[i] == cadena[i].upper():
            #print("reemplazo")
            cadena1 += str("$")
        elif cadena[i] == cadena[i].lower():
            cadena1 += cadena[i]
    print(cadena1)
    return cadena1


def reemplazo_v1():
    cadena = raw_input("Ingrese palabra: ")
    print("")
    tam = len(cadena)
    cadena1 = ""
    for i in range(0,tam):
        if ((chr(32) == cadena[i]) or (cadena[i] == cadena[i].lower())):
            cadena1 += cadena[i]
        elif cadena[i] == cadena[i].upper():
            #print("reemplazo")
            cadena1 += str("$")

        #elif cadena[i] == cadena[i].lower():
         #   cadena1 += cadena[i]
    print(cadena1)
    return cadena1



opcion = 1
while opcion != 0:
    print ("")
    print ("")
    opcion = menu()
    print(opcion)
    print("===================")
    if opcion == 1:
        print("Por ejemplo, si los strings son familia y abrigarse, entonces tu función debe retornar --> fase <--")
        print("")
        mezclador()

    if opcion == 2:
        print("Por ejemplo si los strings son paz y so, entonces tu función debe retornar --> psoasozso <--")
        print("")
        intercalar()

    if opcion == 3:
        print("Por ejemplo, si el string es 11000110101, entonces tu función debe retornar 1 -ya que hay 6 unos y 5 ceros- ")
        print("")
        binaria()

    if opcion == 4:
        print("Por ejemplo, si s es >>Hasta luego<< y n es 3, entonces tu función debe retornar >>Hasa luego<<.")
        print("")
        remover_enesimo()
    
    if opcion == 5:
        print("Por ejemplo si el string es >>Viva la Vida<<, entonces tu función debe retornar >> $iva la $ida <<")
        print("")
        reemplazo()

    if opcion == 6:
            print("Por ejemplo si el string es >>Viva la Vida<<, entonces tu función debe retornar >> $iva la $ida <<")
            print("")
            reemplazo_v1()

else:
    print("No conozco la opcion que has ingresado. Intentalo otra vez.")

print("Chauuuuu")

