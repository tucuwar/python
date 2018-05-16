# -*- coding: utf-8 -*-

#Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
#You need to return the highest scoring word as a string.
#If two words score the same, return the word that appears earliest in the original string.
#All letters will be lowercase and all inputs will be valid.

#equals(high('man i need a taxi up to ubud'), 'taxi')
#test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
#test.assert_equals(high('take me to semynak'), 'semynak')

def cadena(cad):
    #cadena a lista
    L=[]
    L = cad.split(' ')
    print L    
    P = L #guardo L por las dudas

    #for recorre cada item con su valor y
    #mantiene el de mayor valor
    pivot = 0
    for i in P:
        #def valor_palabra de cada item de la lista
        valor_word = valor_palabra(i)
        if valor_word > pivot:
            valor_palabra = valor_word
            max_palabra = i
            pivot = valor_palabra
        else:
            pass
        
    
    pass



def valor_palabra(i):
    abc = [a, b, c, d, e, f, g, h, i, j, k, l, ll, m, n, o, p, q, r, rr, s, t, u, v, w, x, y, z]
    val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    for l in i:
        if l in abc:
            pos = abc.index(l)
        else:
            pass
        valor_word += val[pos]
    return valor_word



        #find(l [, posicion_inicio, posicion_fin])
        #print abc.find(l)
        


cad = raw_input("Ingresar cadena: ")
cadena(cad)





