c = float(input("Ingrese temperatura del agua: "))
if c<=0:
  print("Su agua esta congelada")
elif c>=0 and c<100:
  print("Su agua esta liquida") 
elif c>=101:
  print("Su agua esta hirviendo") 
