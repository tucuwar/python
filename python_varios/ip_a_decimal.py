
# -*- coding: utf-8 -*-
### http://www.hackplayers.com/2018/01/dotless-ip-otra-forma-mas-de-llamar-un-host.html
### calculadora --> http://www.vermiip.es/convertir-ip-decimal/
## un ejemplo sencillo para que quede claro convirtiendo la IP más 
# famosa del mundo: 127.0.0.1.
#Teniendo en cuenta que son octetos debemos tener en cuenta 8 bits 
# por cada número, 
#así que siendo los valores 127=1111111, 0=0 y 1=1 rellenamos con 
# ceros el resto del octeto para completarlo, 
#quedando así: 01111111.00000000.00000000.00000001 
#Ya no nos queda casi nada. Eliminamos los puntos, juntamos 
# todo en una cadena larga y lo convertimos a decimal. 
# 01111111000000000000000000000001 = 2130706433
# test ping 2130706433

### http://elclubdelautodidacta.es/wp/2013/01/python-un-programa-para-la-conversion-de-decimal-a-binario/


def binarizar(ip):
    octetos = ip.split(".") #convierte ip en lista de 4 elementos. separador "."
    print octetos
    print "----"
    ip_binaria = []
    ip_binaria_full = []
    binario = ""
    binario_1 = ""
    binario_2 = ""
    binario_3 = ""
    #cont = 1 #borrar dsp
    for i in octetos:
        ### Separa en 4 partes los valores decimales convertidos a binario
        ### Los guarda en una lista ip_binaria[] 
        #print "octeto %d: " %(cont), i
        a = int(i)
        binario_1 = "" #inicializa vacio por cada ietracion para no arrastrar valores
        while a // 2 != 0:
            binario = str(a % 2) + binario
            a = a // 2
        #print "a: ",a
        #print "binario: ",binario
        binario_1 += str(a) + binario
        binario = "" #para que no arrastre valor
        #cont += 1 #borrar dsp
        ip_binaria.append(binario_1)
    #print "PARTE DOS"
    for i in ip_binaria:
        ### Rellena con "0" a la izquierda para completar el numero binario
        ### Guarda cada elemento en una lista ip_binaria_full[]
        #print i  #borrar
        tam = len(i)
        #print "tam: ",tam   # borrar
        while tam < 8:
            binario_2 += "0" 
            #print binario_2   # borrar
            tam = len(binario_2)+len(i)
            #print ip_binaria[i]
            #print "tam incremental: ",tam
        binario_3 = binario_2+i
        ip_binaria_full.append(binario_3)
        binario_2 = "" # en blanco para no arrastrar valores a la prox.iteracion
    print ip_binaria_full
    return ip_binaria_full
      

def bin_full_a_decimal(ip_binaria_full):
    ### Toma la lista ip_binaria_full[] que contiene 4 elementos con los
    #numeros binarios que constan de 8 caracteres cada uno
    #Concatena todos los elementos en una variable binario_full
    #aplica a la variable una funcion de python int(str(binario_full), 2)
    binario_full = ""
    for i in ip_binaria_full:
        binario_full += i
    print "FULL BINARIO: ",binario_full
    decimal_full = int(str(binario_full), 2)
    print "FULL DECIMAL: ",decimal_full
    #raw_input("Pulsa una tecla para continuar...")

    #return str(decimal) + binario

#def binarizar(decimal):
#    binario = ''
#    while decimal // 2 != 0:
#        binario = str(decimal % 2) + binario
#        decimal = decimal // 2
#    return str(decimal) + binario    

### FUNCIONES DE PYTHON
#De binario a decimal.
#b = 11001
#Convertimos el entero en una cadena y despeas lo pasamos a binario.
#Base 2.
#print int(str(b), 2)
#>>> 25

#De decimal a binario.
#Convertimos el entero 25 a binario
#bin(25)
#Nos devuelve una cadena.
#>>> '0b11001'
#Para convertir el numero en un entero.
#int(bin(25)[2:])


ip = raw_input('Introduce ip: ')
ip_binaria_full = binarizar(ip)
bin_full_a_decimal(ip_binaria_full)
