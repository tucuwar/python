

### accum("abcd")    # "A-Bb-Ccc-Dddd"
### accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
### accum("cwAt")    # "C-Ww-Aaa-Tttt"

def accum(cadena):
    print "Cadena ingresada: %s" %(cadena)
    cadena_up = cadena.upper()
    lista = []
    for i in cadena_up:
        lista.append(i)
    tam = len(lista)
    multiplic = 0
    lista1 = []
    for i in range(0,tam):
        a = lista[i] * multiplic
        l = a.lower()
        lista1.append(lista[i]+l)
        lista1.append("-")
        multiplic +=1
    lista2 = ""
    for i in lista1:
        lista2 += i
    lista3 = lista2.rstrip("-") #quito el ultimo caracter
    #raw_input("Pulsa una tecla para continuar...")  
    return lista3
    
cadena = raw_input("Ingrese cadena de caracteres: ")
lista3 = accum(cadena)
print lista3