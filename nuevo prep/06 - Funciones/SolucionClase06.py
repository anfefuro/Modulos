## Funciones

#1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es


from random import randint, randrange
import re

def verificaPrimo(var01):
    esPrimo = True
    for i in range(2, var01):
        if var01 % i == 0 :
            esPrimo = False
    return(esPrimo)

#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo 
# aquellos que son primos en otra lista

def listPrimos(var02) :
    var021 = [i for i in var02 if verificaPrimo(int(i)) == True]
    return(var021)

var022 = list(range(2, 21))
print('2.', listPrimos(var022))

#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay 
# más de un "más repetido", que devuelva cualquiera
import random

def masRepetido(var03, var04) :
    var031 = {}
    var033 = {}
    if len(var03) == 0 : return None
    for i in sorted(var03) : 
        if i not in var031 :
            var031[i]=1
        else:
            var031[i] += 1
    for k, v in var031.items() :
        var033[v] = k
    if var04 == True :
        return(var033[max(var033)], max(var033))
    else: 
        return(var033[min(var033)], min(var033))

var032 = [random.randint(0, 5) for i in range(20)]

moda, repite = masRepetido(var032, True)
print('4. ', 'Modal:', moda, 'Repeticiones:', repite)

#4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
#Fórmula 1	: (°C × 9/5) + 32 = °F<br>
#Fórmula 2	: °C + 273.15 = °K<br>
#Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conversor(valor, origen, destino) :
    if origen == 'cel' and destino == 'far' :
        retorno = ((valor * 9)/5) + 32
    elif origen == 'cel' and destino == 'kel' :
        retorno = valor + 273.15
    elif origen == 'cel' and destino == 'cel':
        retorno = valor
    elif origen == 'far' and destino == 'cel' :
        retorno = ((valor - 32) * 5) / 9
    elif origen == 'far' and destino == 'kel' :
        retorno = (((valor - 32) * 5) / 9) + 273.15
    elif origen == 'far' and destino == 'far':
        retorno = valor
    elif origen == 'kel' and destino == 'cel' :
        retorno = (valor - 273.15)
    elif origen == 'kel' and destino == 'far' :
        retorno= (((valor - 273.15) * 9)/5) + 32
    elif origen == 'kel' and destino == 'kel':
        retorno = valor
    else:
        print('Valor invalido')
    return(retorno)

print('5. 30° Celcius a Fahrenheit: ', conversor(30, 'cel', 'far'))

#6) Iterando una lista con los tres valores posibles de temperatura que recibe la función 
# del punto 5, hacer un print para cada combinación de los mismos:
var06 = ['cel', 'far', 'kel']
var061 = {}

for i in range(0,3):
    for j in range(0,3):
        var061['30°', var06[i], 'a', var06[j]] = round((conversor(30, var06[i], var06[j])), 2)
print('6. ', var061)

#7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(var07):
    if type(var07) != int :
        return('Debe ser entero')
    elif var07 < 0 :
        return('Debe ser positivo') 
    elif var07 > 1 :
        var07 *= factorial(var07 - 1)
    elif var07 == 0 :
            return(None)
    return(var07)

var071 = 0
print('7. Factorial de', var071, ':', factorial(var071))