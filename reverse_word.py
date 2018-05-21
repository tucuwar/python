# -*- coding: utf-8 -*-

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(cad):
    vere = [] 
    s = cad.split(" ") #string a lista. Separo por espacio en blanco
    for i in s:
        a = i[::-1] #al reves cada palabra
        vere.append(a) #voy guardando en lista
    b = " ".join(vere) #lista a string
    return b
    print b
       
cad = raw_input("Ingrese cadena de texto: ")
b = reverse_words(cad)
print b