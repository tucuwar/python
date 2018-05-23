# -*- coding: utf-8 -*-

#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    tam=len(s)
    P=[]
    I=[]
    ii = 0
    f = 2
    if (tam % 2 == 0):
        #print "PAR"
        for i in range(len(s)/2): #range(0,tam/2,1):
            i = s[ii:f:1]
            P.append(i)
            ii += 2
            f += 2
        print P
    else:
        #print "IMPAR"
        for i in range(len(s)/2+1): #range(0,tam/2+1,1):
            i = s[ii:f:1]
            I.append(i)
            ii += 2 
            f += 2
        #print I[-1] #ultimo elemento de una lista 
        I[-1] = I[-1]+"_"
        print I
        

s = solution(raw_input("Ingresa string: "))
