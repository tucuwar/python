numero=int(input("Ingrese un numero: "))
a=0

for i in range(1,numero+1):
 if(numero % i==0):
  a=a+1

print("Valores para entrar al IF a!=0")
print(a)
print(i)
print("")
if(a!=2):
 print("No es primo")
 primo = False
else:
 print("si es primo")
 primo = True

