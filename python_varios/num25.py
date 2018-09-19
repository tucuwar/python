# -*- coding: utf-8 -*-
###Programa que imprima los 25 primeros numeros naturales
#for num in range(1,26):
#   print num
#print(" ")

###Imprimir los numeros impares desde el 1 al 25, ambos inclusive
#for num in range(1,26,2):
#    print num
#print(" ")

###Imprimir los numeros pares desde el 40 hasta el 60, ambos inclusive
#for num in range(40,62,2):
#    print num
#print(" ")

###Imprimir los numeros 48, 52, 56, ..., 120
#for num in range(48,124,4):
#   print num
#print(" ")


###Calcular e imprimir la suma 1+2+3+4+5+...+50
#num = 0
#num1 = 0
#for num in range(1,51):
#    num1 = num + num1  
#    print ("Pos.",num," Suma >>",num1)
#print(" ")

###Calcular e imprimir el producto de 1*2*3*4*5*...*50
#num = 0
#num1 = 1
#for num in range(1,51):
#    num1 = num * num1  
#    print ("Pos.",num," Suma >>",num1)
#print(" ")


###Calcular e imprimir la suma 50+48+46+44+...+20
#num1 = 0
#for num in range(50,19,-1):
#    num1 = num + num1
#    print ("Pos.",num," Suma >>",num1)
#print(" ")

###Programa que imprima los nuumeros impares desde el 100 hasta la unidad y calcule su suma
#num1 = 0
#for num in range(99,0,-2):  
#    if (num % 2) == 1:
#        num1 = num + num1
#        print ("Pos Impar.",num," Suma >>",num1)
#print(" ")

### Introducir un nuumero por teclado y decir si es par o impar
#num = 0
#num = int(input("Ingrese un numero: "))
#if (num%2) == 1:
#    print("Numero ingresado es IMPAR")
#else:
#    print("Numero ingresado es PAR")
#print(" ")

##Imprimir los numeros del 1 al 100 y calcular la suma de todos los nuumeros 
###pares por un lado, y por otro, la de los impares
#np = 0
#ni = 0
#for n in range(1,101,1):
#    if (n%2)==1:
#        ni = n + ni
#    else:
#        np = n + np
#print("Los numeros pares suman ", np)
#print("Los numeros impares suman ", ni)


##Introducir dos numeros por teclado. Imprimir los numeros que hay entre ellos 
###comenzando por el mas pequeno. Contar cuantos hay y cuantos de ellos son 
###pares. Calcular la suma de los pares

#n1 = int(input("Ingrese num1: "))
#n2 = int(input("Ingrese num2: "))
#a = 0; b = 0; np = 0

#if n1 > n2:
#    a = int(n2); print "Num. mas chico ",a
#    b = int(n1); print "Num. mas grande ",b
#else:
#    a = int(n1); print "Num. mas chico ",a
#    b = int(n2); print "Num. mas grande ",b
    
#for n in range(a,b,1):
#    print "Numeros intermedios: ", n
#    if (n%2)==0: #saber si es par
#        np = n + np

#c = b-a; print "==================="
#print "Cantidad de numeros intermedios: ",c
#print "Suma de numeros pares intermedios: ", np 

### Imprimir y contar los numeros multiplos de 3 que hay entre 1 y 100.
#print "Multiplos de 3, entre 1 y 100"
#cont = 0
#for n in range(1,101,1):
#    if (n%3) == 0: #multiplo de 3
#        print n
#        cont += 1
#print "Cantidad de multiplos de 3: ", cont


### Imprimir, sumar y contar los numeros que son a la vez multiplos de 2 y 
###de 3, que hay entre la unidad y un determinado numero introducido por el 
###teclado.
#a = int(input("Ingrese numero: "))
#sum1 = sum2 = sum3 = 0 #inicializar multiples variables
#for n in range(1,a,1):
#    if (n%2)==0:
#        print "Multiplo de 2: ",n
#        sum2 = n + sum2
#    elif (n%3)==0:
#        print "Multiplo de 3: ",n
#        sum3 = n + sum3
#sum1 = sum2 + sum3
#print "Sumatoria de multiplos de 2 y 3 entre 1 y",a
#print "es igual a: ",sum1


##Introducir dos valores A y B:
###Si A>=B, calcular e imprimir la suma 10+14+18+...+50 
###Si A/B<=30, calcular e imprimir el valor de (A**2+B**2)
#A = int(input("Ingrese 1er valor: ")) 
#B = int(input("Ingrese 2do valor: "))
#sum_AB = exp = 0

#if A >= B:
#    for n in range(10,51,1):
#        sum_AB = n + sum_AB
#    print "Sumatoria: ",sum_AB
#elif (A/B) <= 30:
#    exp = (A**2+B**2) 
#    print "Si es menor o igual a 30: ", exp



### Mete los valores del 1 al 100 en una lista.
#l = []
#for i in range(1,101):
#    l.append(i) #encierra en []
#print l
#print "=============="
#c = []
#c.append(range(1,101)) #encierra en dos [[ ]]
#print c



### Crea una tupla con los meses del anio, pide numeros al usuario, 
## si el numero esta entre 1 y la longitud maxima de la tupla, 
## muestra el contenido de esa posicion sino muestra un mensaje de error.
## El programa termina cuando el usuario introduce un cero.

#n = 0
#anio = ("salir","ene","feb","mar","abr","may","jun","jul","ago","sep","octb","nov","dic") # esto es una TUPLA

#n = int(input("Ingrese num de mes: "))

#if n > 0 and n < 13:
#    print anio[n] #para ver el valor de un elemento en la tupla se utiliza el []
#elif n == 0 or n >= 13:
#    print "Salir"




### Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo, si pide el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

#a = int(input("Ingrese num.: "))
#l = [] # crea lista vacia
#for n in range(1,11):
#    l.append(a*n)
#t = tuple(l)  #utiliza "tuple" para convertir a tupla y se utiliza "list" para converir a lista
#print t



###Pide nnmeros y metelos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por ultimo, muestra los numeros ordenados de menor a mayor.
#n = 1
#l = []
#print "Ingrese num. a la lista, para dejar de ingresar presione cero"
#while n != 0:
#    n = int(input("Ingrese num.: "))  
#    if n != 0:
#        l.append(n)
#l.sort()  # ordeno al finalizar la carga
#print l


### Crea una tupla con numeros, pide un numero por teclado e indica cuantas veces se repite.
#t = (2,3,8,7,4,65,5,9,8,12,32) # SE REPITE 8
#print "Tupla --> ", t
#c = int(input("Ingresar numero para verificar si esta repetido: "))
#if c in t: #valor esta en la tupla?
#    if t.count(c) >= 2:
#        print("El valor es repetido "+str(t.count(c))+" veces")
#    else:
#        print "No esta repetido"
#else:
#    print "El numero no esta en la lista"


### Crea una tupla con numeros e indica el numero con mayor valor y el que menor tenga.
#t = (2,3,8,7,4,65,5,9,8,12,32)
#print "tupla -->", t
#t = list(t) #convierto tupla a lista
#t.sort()
#print t
#print "el mayor numero es: ", t[len(t)-1]
#print "el menor numero es: ", t[0]


###Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono 
# (no es necesario validar). 
# Tendras que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas.
# No se podran meter nombres repetidos.

#def fcontacto():
#    name = str(raw_input("  Ingrese nom: "))
#    return name
#def fcel():
#    cel = str(raw_input("  Ingrese cel: "))
#    return cel 
#def check_repetido(name):
#    if d.get(name) == None:
#        d[name] = [cel] #guardo nombre y cel en DICCIONARIO
#    else:    
#        print "El nombre de contacto: >> "+name+" << ya esta en uso"
#d={} #creo diccionario vacio
#while (str(raw_input("Ingresar nuevo contacto (y/n): ")) == 'y'):
#    print "Contacto: "
#    name = fcontacto() #solicito nombre
#    cel = fcel() #solicito cel
#    check_repetido(name)
#print "DICCIONARIO -->", d


###Escribir un algoritmo que, para cualquier numero de segundos inferior a un millon, 
#calcule su equivalente en dias, horas, minutos y segundos.
# 1 minuto = 60 segundos.
# 1 hora = 60 minutos = 3600 segundos.
# 1 dia = 24 horas = 1440 minutos = 86400 segundos.
#{0:.2f}".format(n)
#s = int(input("Ingrese numero inferior a 1 millon: "))
#if s > 1000000: print "El numero es mayor a 1Millon"
#else:
#    m = int(s/60)
#    h = int(m/60)
#    d = int(h/24)
#    print "        Dias::Horas:Min:Seg"
#    print "Tiempo: "+str(d)+"::"+str(h)+":"+str(m)+":"+str(s)


###Escribir un algoritmo que imprima el minimo, el maximo y la media de tres numeros.
#print "Ingrese 3 numeros"
#l = [] #creo lista
#for i in range(0,3,1):
#    i = int(input("Ingrese numero: "))
#    l.append(i)
#l.sort()
#print "Numeros igresados ",l
#m = round ((l[0]+l[1]+l[2])/float(3),2)
#print "MAX | MEDIA | MIN ", str(l[2])+" | "+str(m)+" | "+str(l[0])

###Escribir un algoritmo que, dado el infinitivo de un verbo regular de la primera conjugacion, 
# obtenga la conjugacion en singular y plural de presente de indicativo. 
# Por ejemplo, para el verbo cantar el resultado es yo canto, tu cantas, el canta, 
# nosotros cantamos, vosotros cantais, ellos cantan.

#pronombre = ['yo','tu','el','nosotros','vosotros','ellos']
#terminaciones = ['o','as','a','amos','ais','an']
#p = str(raw_input("Ingrese verbo regular de la 1era Conjugacion: "))
#tam = len(p)
#p1 = p[0:(tam-2)] #quitando al verbo la conjugacion ar, er, ir 
#v = []
#t=0
#for i in pronombre:
#    v.append(i+": "+p1+terminaciones[t])
#    t += 1
#print v


###Escribir un algoritmo que, para un numero binario de 4 cifras, imprima su valor en base 10. 
#Se estudiaran dos formas del problema segun la representacion de los datos:
#    -forma 1: los datos son cuatro enteros (0 o 1). Por ejemplo: 1,1,0,1.
#    -forma 2: el dato es un entero cuya representacion decimal con cuatro
#              cifras no contenga mas que 0 o 1: Por ejemplo: 1101.

#import sys #utilizado para sys.exit()
#print "Ingrese binario de 4 cifras"
#b = [] #binario
#o = [] #operaciones
#d = 0 #decimal
#p = [2**3,2**2,2**1,2**0] #potencia2
#a = int(input("numero binario: "))
#print "El numero ingresado: ",a
#c = str(a)
#for i in range(0,4,1): #ingresa numero a una lista
#    e = int(c[i])
#    b.append(e)
#print (b), "Binario"
#print (p), "Potencia de 2"
#for i in range(0,4,1): #Operaciones
#    if b[i] == 0:
#        o.append(0)
#    elif b[i] == 1:
#        o.append(p[i])
#    else:
#        print "El numero "+ str(a) +" no es binario"
#        sys.exit()
#print (o), "Operaciones"
#for i in range(0,4,1): #decimal
#    d = d + o[i]
#print (d), "Numero Decimal"



###Escribir un algoritmo que decodifique fechas del siglo XXI.
#El dato es un entero comprendido entre 10100 y 311299. 
#El resultado es una secuencia de caracteres: 
#número del día dentro del mes, del mes dentro del año y
# del año dentro del siglo. 
# Por ejemplo, para el dato 30485, 
# el resultado es el texto 3-4-2085.

#import sys #utilizado para sys.exit()
#print "Ingrese numero comprendido entre 10100 y 311299"
#n = int(input("Ingrese:"))
#if (n >= 10100) and (n <= 311299):
#    print "Numero aceptado"
#else:
#    print "El numero no esta en el rango solicitado"
#    sys.exit()
#sn = str(n) #numero a string
#l = len(sn) #largo de palbra
#if l >= 6: # dd mm aa
#     d = sn[0:2]
#     m = sn[2:4]
#     a = 2000 + int(sn[4:6])
#else: # d mm aa
#    d = sn[0]
#    m = sn[1:3]
#    a = 2000 + int(sn[3:5])
#print "La fecha es {0}-{1}-{2}".format(d,m,a)


### Escribir un algoritmo que, para una suma de dinero dada, 
# indique cómo descomponerla en billetes y monedas corrientes.
# Se desea utilizar el mínimo de billetes y monedas. 
# No hay ninguna limitación respecto al número de billetes 
# y monedas disponibles.

#   B       M              A B C    D
#   500           ej:      3 2 5 . 50 
#A  200
#   100
#------------------
#   50
#B  20
#   10
#-----------------
#   5
#C  2
#   1
#-----------------
#           0,50
#           0,25
#D          0,10
#           0,05
#           0,01 
# ----------------

plata = raw_input("Ingrese valor (use punto decimal): ")
tam = len(plata)
billetera = [500, 200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]




if "." in plata:
    #print "Tiene punto decimal"
    plata_decimal = plata[tam-2:tam]
    plata_decimal = float("0."+plata_decimal) #str a float
    plata_entero = int(float(plata)) #paso de str a float a entero int
    #print plata_entero, plata_decimal
else:
    #print "No tiene punto decimal"
    plata_decimal = 0
    plata_entero = int(float(plata)) #paso de str a float a entero int
    #print plata_entero

print "---------"
print "Entero {0} y decimal {1}".format(plata_entero, plata_decimal)
print "Entero %s y decimal %s" % (plata_entero, plata_decimal)


#Para entero solo (else)
if plata_entero >= 501 and plata_entero <= 1000:
    print "Entre 501 y 1000"
elif plata_entero >= 200 and plata_entero <= 500:
    print "Entre 500 y 200"
elif plata_entero >= 100 and plata_entero <= 200:
    print "Entre 200 y 100"
elif plata_entero >= 50 and plata_entero <= 100:
    print "Entre 100 y 50"
elif plata_entero >= 20 and plata_entero <= 50:
    print "Entre 50 y 20"
elif plata_entero >= 10 and plata_entero <= 20:
    print "Entre 20 y 10"
elif plata_entero >= 5 and plata_entero <= 10:
    print "Entre 10 y 5"
elif plata_entero >= 1 and plata_entero <= 5:
    print "Entre 5 y 1"    
   
