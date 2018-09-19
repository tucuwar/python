

# A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.
# For example, take 153 (3 digits):
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


def narcissistic(numero):
    tam = len(numero)
    #print tam
    pivot = numero[tam-1]
    #print pivot
    string = str(numero)
    potencia = 0
    for i in string:
        potencia = pow(int(i),int(pivot)) + potencia
        #print potencia
    #raw_input("Pulsa una tecla para continuar...")
    numero = int(string)
    if (numero==potencia):
        print "El numero %d ES narcisista" %(numero)
    else:
        print "El numero %d NO ES narcisista" %(numero)

    #raw_input("Pulsa una tecla para continuar...")



numero = raw_input("Ingrese numero: ")
narcissistic(numero)
    