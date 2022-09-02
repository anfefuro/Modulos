## Flujos de Control

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from random import randint
from re import I

var01 = randint(1, 10)
if var01 > 0: print('1. La constante es mayor a cero') 
else: print('1. La constante es menor a cero')

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
var02 = randint(1, 10)
var021 = randint(1, 10)
if type(var02) == type(var021) : print('2. Las variables son del mismo tipo de dato')
else : print('2. Las variables no son del mismo tipo de dato')

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
var03 = []
var031 = []
for i in range(1, 20) :
    if i%2 == 0 : var03.append(i)
    else : var031.append(i)
print('3. Pares: ', var03)
print('   Inpares: ', var031)

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
var04 = []
for i in range(5) : var04.append(i**3)
print('4. Valores del 0 al 5 elevados a la tercera potencia: ', var04)

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var05 = randint(1, 10)
var051 = []
for i in range(var05) : var051.append(i)
print('5. ', var051)

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
var06 = randint(1, 10)
print('6. Factorial de ', var06, ':')
fact = 1
while (var06 > 0) : 
    fact *= var06
    var06 -= 1
print('  ', fact)

#7) Crear un ciclo for dentro de un ciclo while (Mientras sea verdad, implica una modificacion del valor hasta no cumplir la condicion)
var07 = randint(1, 10)
print('7. Valores en un rango del 0 al', var07 - 1, 'multiplicados por 2')
var071 = []
while (var07 > 0) :
    for i in range(var07) : i *= 2
    var07 -= 1
    var071.append(i)
print('  ', var071)

#8) Crear un ciclo while dentro de un ciclo for
var08 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var081 = []

for i in var08 : 
    while True :
        i < 1
        break
        i -= 1
    var081.append(i)
print('8. El bucle while interactua con la iteracion generada por el bucle for, generando una operacion en la cual el ciclo se rompe cuando el elemento iterado se menor a 1: ', var081)

#9) Imprimir los números primos existentes entre 0 y 30
var09 = []

for i in range(30) : 
    if i%2 != 0 : var09.append(i)
print('9. ', var09)

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
var10 = range(30)
var101 = []

for i in var10 :
    if i%2 == 0 : continue
    var101.append(i)
print('10. ', var101)    

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
var11 = []
count = 0
for i in range(30) : 
    count += 1
    if i%2 != 0 : var11.append(i)
print('11. Sin continue', count, var11)

var111 = range(30)
var112 = []
count2 = 0
for i in var111 :
    count2 += 1
    if i%2 == 0 : continue
    var112.append(i)
print('11. Con continue', count2, var112)  

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
var12 = range(100)
var121 = []
count2 = 0
for i in var12 :
    count2 += 1
    if i%2 == 0 : continue
    var121.append(i)
print('12. Con cien elementos iterados', count2, var121)  

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
var13 = 99
var131 = []

while (var13 < 300) : 
    var13 += 1
    if var13%12 != 0 :
        continue
    var131.append(var13)
print('13. ', var131)

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

var14 = range(100)
var141 = []
var142 = 0

for i in var14 :
    if i%2 != 0 : var141.append(i)

for line in var141 : 
    inputVar = input('Siguiente primo *y* más enter, salir, cualquier otro más enter: ')
    if inputVar == 'y' : print(var141[var142])
    else : break
    var142 += 1

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
var15 = 99


while (var15 <= 300) :
    if var15%3 == 0 and var15%6 == 0 : 
        print('15. ', var15)
        break
    var15 += 1
