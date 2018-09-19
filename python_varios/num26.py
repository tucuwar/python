### Crear  funcion que reciba una cadena y muestre que caracteres
# estan repetidos.
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(cadena):
    repite = 0
    string = [] #cadena original
    string_compara = [] #cadena sin pivot para comparar
    string_resultado = [] #guarda los elementos repetidos
    
    for i in cadena:
        string.append(i) #guardo elementos en una lista
    tam = len(string)
    string_compara = string

    for i in range(0, tam, 1):
        #print string_compara, "string completo"
        pivot = string_compara[i]
        print pivot, "Pivot"
        string_compara.pop(i)
        #print string_compara, "string compara"
        print "==="

        for item in range(0, tam-1, 1):
            #print string_compara[item], pivot
            if string_compara[item] == pivot:
                #print pivot, "=", string_compara[item], "<-- OK"
                #repite = repite + 1
                string_resultado.append(pivot)
            #else:
                #print pivot, "!=", string_compara[item]
          
        print string_resultado, "RESULTADO PARCIAL"
        print "---------"
        string_compara.insert(i, pivot)

    print " "
    print "---------------------------------------" 
    print string_resultado, "RESULTADO"
    print repite 
    return (repite)

cadena = raw_input("Ingrese cadena: ")
duplicate_count(cadena)

