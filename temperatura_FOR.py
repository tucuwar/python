print("Conversor Fahrenheit a Celsius con FOR")
temp = int(input("Ingrese temperatura: "))
print("F     C")
for temp in range(temp,73,10):
  print(temp,"  ",int((temp-32)*5/9))

#in range (inicio, final-1, aumenta variable en)
#