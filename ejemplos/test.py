
import os, sys, subprocess, socket, string

#listar como "dir"
#print os.listdir('.')

print("HOLA")
#ip = "10.10.1.3"
ip = "10.10.253.209"
#ip = str(input("Escriba ip para hacer un ping: "))
print(ip)
#print(type(ip))
#param = "-n 2"
cuak = ('psexec \\\\'+ip+' cmd')
print (cuak)
#os.system('cuak')
# print("ping "+param+" "+ip)
#PARA PING os.system('ping -c 2'+' '+ip)
print ("Ejecutando psexec a: "+ip)
os.system(cuak)



#def suma(N):
#N=input("Ingrese valor: ")
#s=0
#for i in range(N):
# s+=i
# print("Valor i: ", i)
# print("Valor s: ", s)
# print("")

#print("Valores finales")
#print("Valor i: ", i)
#print("Valor s: ", s)
  #return s


#def funcion_misteriosa(x):
#x=input("Ingrese valor: ")
#for i in range(2,x):
# if x%i==0:
#   print("IF - FALSE")
#print("FOR - TRUE")
#print("Valor de x: ", x)

#def funcion_misteriosa(x):
#x = input("Ingrese valor: ")
#c=0
#while x!=0:
# c+=1
# x = x//10
# print(c)


#x = 48
#y = 8
#n = 0
#while x > 0:
#    x = x - y
#    n = n + 1
#    print ("Valor de x: ", x)
#    print ("Vuelta N: ", n)
#    print ("")
#print ("Valor final de x ", x)
#print ("Valor final de n ", n)

#a = 5
#b = 8
#r = 0
#while a > 0:
#    r = r + b
#    a = a - 1
#print(r)





#a = 4
#b = 3
#r = b
#while a > 1:
#    a = a - 1
#    b2 = b
#    r2 = 0
#    while b2 > 0:
#        r2 = r2 + r
#        b2 = b2 - 1
#    r = r2
#print(r)


#a = 3
#for i in range(2, 3):
#    a = a * i
#print(a)


#a = 2
#for i in range(1,4):
#    a = i ** a
#print(a)

#for i in range(10):
#    print('hola mundo', i)

#a = 0
#for i in range(3):
#    a = a + i
#print(a)

#numero = 1
#while numero <= 5:
#  print(numero, numero**2)

#for i in range(1,101):
#  for j in range(1,101):
#    print(i,j)