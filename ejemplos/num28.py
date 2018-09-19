
# -*- coding: utf-8 -*-

#We want to generate a function that computes the series starting 
# from 0 and ending until the given number following the sequence:
# 0 1 3 6 10 15 21 28 36 45 55 ....
# 0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4, 0+1+2+3+4+5, 0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7 etc..

# Input: 6
# Output: 0+1+2+3+4+5+6 = 21

# Input: -15
# Output: -15<0

# Input: 0
# Output: 0=0

def serie(n):
    #n = fin
    v = 0
    i = 0
    r=[] 

    for i in range(n):
        v = i + (v+1)
        r.append(str(v)+"+")
        #print "v: ",v
        print v, #para resultado horizontal
    print ""
    print "Output"
    print ""
    print r
    resultado(r)

def resultado(r):
    #temp = len(r)
    print "Resultado"
    print r
    

n = int(raw_input("Ingrese valor final de la serie: "))
serie(n)

