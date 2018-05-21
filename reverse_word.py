# -*- coding: utf-8 -*-

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(cad):
    C = cad.split(' ')
    
    pivot = [] #guardo palabra al reves
    for i in C: # pasa primera palabra i
        tam = len(i)
        print tam
        word = []
        reverse = []
        for x in i:
            word.append(x)
        print word
        #cont = tam
        for l in range(0,tam,1):
            reverse.append(word[l]) #debe ir de mayor a menor
        print reverse
      
    pass



cad = raw_input("Ingrese cadena de texto: ")
reverse_words(cad)