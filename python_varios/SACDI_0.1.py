# -*- coding: utf-8 -*-

# Sistema Avanzado de Calculo de Interes :)

###web Referencia:
# https://igdigital.com/2017/09/tasa-de-interes-la-formula-para-calcularla-en-2017/

# Interés simple = Prestamo x Tasa de interés x Períodos a pagar
# Interés simple = 500 pesos x 0,03 x 6 meses = 90

#La fórmula para calcular el interés simple será así:
#El interés (I) que produce el capital es proporcional al capital inicial (C ), 
# al tiempo (t) y a la tasa de interés (i)
# I = C x i x t    #tasa de interes (i) = 3/100 = 0.03
# I = 90 x 0,03 x 6 


### Historial de cambios
### Opcion 3 COMPARA resultados de los dos calculos de intereses (por mes y por dia) no funciona
###

def menu():
    print("")
    print("================================")
    print("Menu de Opciones - Calculo de Interes")
    print("1 - Interes Simple por mes")
    print("2 - Interes Simple por dias")
    print("9 - Comparar Intereses")
    print("0 -  Salir")
    print("================================")

def Capital_input():
    CI = int(input("Capital Inicial: "))
    return CI
def Interes_input():
    ti = int(input("Tasa de interes % "))
    return ti
def Periodo_m_input():
    P = int(input("Periodos a pagar por mes: "))
    return P
def Periodo_d_input():
    d = int(input("Periodos a pagar por dias: "))
    return d

def Interes_simple_mes(CI, ti, P):
    print "Calculo de Interes Simple - por mes"
    print "IS = Capital Inicial (CI) x Tasa de interes (TI) x Períodos a pagar (P)"
    cim = CI #capital inicial por mes
    tii = round((ti%100),2)
    TI = tii/100
    ISm =cim*TI*P #Interes Simple por mes
    CAm =cim+ISm # Capital Actual por mes
    print "Calculo de Interes Simple - por mes"
    print " "
    print "Interes Simple por mes: ",round(ISm,2)
    print "Capital Actual por mes: ",round(CAm,2)
    return ISm,CAm


def Interes_simple_dia(CI,ti, d):
    print "Calculo de Interes Simple - por dia"
    print "IS = Capital Inicial (CI) x Tasa de interes (TI) x dias a pagar (P)"
    cid = CI #capital inicial por dia
    tii = round((ti%100),2)
    TI = tii/100
    p= round((d%365),2)
    D= p/365
    ISd =cid*TI*D #Interes Simple
    CAd =cid+ISd # Capital Actual
    print "Calculo de Interes Simple - por dia"
    print " "
    print "Interes Simple por dia: ",round(ISd,2)
    print "Capital Actual por dia: ",round(CAd,2)
    return ISd,CAd

def compara(ISm, CAm, ISd, CAd):
    print "======================================="
    print "Interes Simple por mes: ",round(ISm,2)
    print "Capital Actual por mes: ",round(CAm,2)
    print "======================================="
    print "Interes Simple por dia: ",round(ISd,2)
    print "Capital Actual por dia: ",round(CAd,2)
    return ISm, CAm, ISd, CAd


continuar = True
while continuar:
    menu()
    opt_menu=raw_input("Opcion: ")
    if opt_menu == "1":
        CI = Capital_input()
        ti = Interes_input()
        P = Periodo_m_input()
        ISm, CAm = Interes_simple_mes(CI, ti, P)
        print("")
    elif opt_menu == "2":
        CI = Capital_input()
        ti = Interes_input()
        d = Periodo_d_input()
        ISd, CAd = Interes_simple_dia(CI, ti, d)
        print("")
    elif opt_menu == "9":
        compara(ISm,CAm,ISd,CAd)
    elif opt_menu == "0":
        continuar = False
        #Mensaje de salida, una vez que el ciclo ha terminado.
        print("Programa terminado - Exit")