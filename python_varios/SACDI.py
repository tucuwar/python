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




def menu():
    print("")
    print("================================")
    print("Menu de Opciones - Calculo de Interes")
    print("1 - Interes Simple por mes")
    print("2 - Interes Simple por dias")
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
    tii = round((ti%100),2)
    TI = tii/100
    IS =CI*TI*P #Interes Simple
    CA =CI+IS # Capital Actual
    print "Calculo de Interes Simple - por mes"
    print " "
    print "Interes Simple: ",round(IS,2)
    print "Capital Actual: ",round(CA,2)
    return IS,CA


def Interes_simple_dia(CI,ti, d):
    print "Calculo de Interes Simple - por dia"
    print "IS = Capital Inicial (CI) x Tasa de interes (TI) x dias a pagar (P)"
    tii = round((ti%100),2)
    TI = tii/100
    p= round((d%365),2)
    D= p/365
    IS =CI*TI*D #Interes Simple
    CA =CI+IS # Capital Actual
    print "Calculo de Interes Simple - por dia"
    print " "
    print "Interes Simple: ",round(IS,2)
    print "Capital Actual: ",round(CA,2)
    return IS,CA


continuar = True
while continuar:
    menu()
    opt_menu=raw_input("Opcion: ")
    if opt_menu == "1":
        CI = Capital_input()
        ti = Interes_input()
        P = Periodo_m_input()
        Interes_simple_mes(CI, ti, P)
        print("")
    elif opt_menu == "2":
        CI = Capital_input()
        ti = Interes_input()
        d = Periodo_d_input()
        Interes_simple_dia(CI, ti, d)
        print("")
    elif opt_menu == "9":
        compara()
    elif opt_menu == "0":
        continuar = False
        #Mensaje de salida, una vez que el ciclo ha terminado.
        print("Programa terminado - Exit")