print("Conversor Fahrenheit a Celsius con WHILE")
temp = int(input("Ingrese temperatura: "))
print("F     C")
while temp < 73:
  print(temp,"  ",int((temp-32)*5/9))
  #C=(F-32)*(5/9)
  temp=temp+1
