
numero = input("Ingrese un numero: ")

# eval = numero % 2 == 0
if (numero % 2) == 0:
  print("Numero ingresado es par", numero)
  resultado = numero ** 3
  print("Elevado al cubo es: ", resultado)
else:
  print("Numero ingresado es impar", numero)
  resultado = numero ** 2
  print("Elevado al cuadrado es: ", resultado)


