print("Ingrese tiempo en segundos")
ts=input()

th=(ts/60)/60

print("Tiempo ingresado en segundos " + str(ts))
print("Equivale en horas a: " + str(th))
print("==========================")
print("Ingrese distancia en kilometros")
dk=input()

dm=dk*1000
print("Distancia ingresada en kilometros " + str(dk))
print("Equivale en metros a: " + str(dm))
print("========================")

#formula velocidad=distancia/tiempo

vkh=dk/th
vms=dm/ts

print("La velocidad es " + str(vkh) + " km/h o " + str(vms) + " m/s")
