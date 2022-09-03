def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''

    listaBin = []
    divResto = 0
    divEntero = 0 
    while numero > 0:
        divResto = numero % 2
        numero = numero // 2
        listaBin.append(divResto)
    
    numBin = ''
    for i in listaBin:
        numBin = str(i) + numBin

    return(numBin)
    
def numeroBinarioFraccionario(numero):
    parteEntera = 0
    listaBinarioDec = []
    limitePeriodico = 20
    i = 0
    while numero > 0 and (i < limitePeriodico):
        listaBinarioDec.append(int(numero * 2))
        numero = numero * 2 - (int(numero * 2))
        i += 1
    numeroBinario = '0.'
    for e in listaBinarioDec:
        numeroBinario = numeroBinario + str(e)
    return(numeroBinario)

for j in range(2, 10):
    print('Fraccion 1/', j, ': ', str(1/j), 'y en binario: ', numeroBinarioFraccionario(1/j)) 
