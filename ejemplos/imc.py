imc = 0
print("Ingrese masa")
masa = input()

print("Ingrese altura")
altura = input()

imc = masa / (altura**2)
a=round(imc,2)
print "Su IMC es "+str(a)
