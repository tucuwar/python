print("Ingrese cargo de: Ejecutivo, Jefe o Externo ")
cargo = str(input("Su cargo es: "))
print (type(cargo))
print ("===========")
dinero = 0
if cargo is Ejecutivo:
  dinero = 90
elif cargo == "2":
    dinero = 100
else:
    dinero = 50

print("Su sueldo como : "+ str(cargo)+" es de $"+str(dinero))