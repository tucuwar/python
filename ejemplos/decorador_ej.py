# -*- coding: utf-8 -*-

def decorador(funcion):
    def funcionDecorada(*args, **kwargs):
        print('Funcion ejecutada')
        funcion(*args,**kwargs) 
    return funcionDecorada 
def resta(n,m):
    print (n-m)
     
decorador(resta)(5,2) 