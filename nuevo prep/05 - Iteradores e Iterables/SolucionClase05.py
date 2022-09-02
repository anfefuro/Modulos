## Iteradores e iterables

#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
from os import remove


var01 = []
var011 = -15

while (var011 < 0) :
    var01.append(var011)
    var011 += 1 
print('1. ', var01)

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
var02 = -15
var021 = []

while (var02 < 0) :
    if var02% -2 == 0 : var021.append(var02)
    var02 += 1
print('2. ', var021)

#3) Resolver el punto anterior sin utilizar un ciclo while

var031 = {i for i in var01 if i%2 == 0}    
print('3. ', var031)

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

var042 = {i for i in var01[:3]}
print('4. ', var042)

#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

var052 = {}
for k, v in enumerate(var01): var052[k] = v
print('5. ', var052)

#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: 
lista = [1,2,5,7,8,10,13,14,15,17,20]

for i in range(1, 20) :
    if i not in lista : lista.append(i)
lista.sort()
print('6. ', lista)

#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n0 = 0
#n1 = 1
#ni = ni-1 + ni-2
#Crear una lista con los primeros treinta números de la sucesión.<br>
var07 = 1
var071 = [0, 1]

while (len(var071) < 30) :
    var071.append(var071[var07] + var071[var07 - 1])
    var07 += 1
print('7. ', var071)

#8) Realizar la suma de todos elementos de la lista del punto anterior
print('8. ', sum(var071))

#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. 
# Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos<br>
#ni-1 / ni
#ni-2 / ni-1
#ni-3 / ni-2
#ni-4 / ni-3
#ni-5 / ni-4

var09 = 25 
var091 = []

while var09 < 30 :
    var091.append(round((var071[var09] / var071[var09 - 1]), 4))
    var09 += 1
print('9. ', var091)

#10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

var101 = {k for k,v in enumerate(cadena) if v == 'n'}
print('10. ', var101)

#11) Crear un diccionario e imprimir sus claves utilizando un iterador
var11 = {'Lunes' : 'Monday', 'Martes' : 'Tuesday', 'Miercoles' : 'Wednesday', 'Jueves' : 'Thursday', 'Viernes' : 'Fryday', 'Sabado' : 'Saturday', 'Domingo' : 'Sunday'}

var112 = {i for i in var11}
print('11. ', var112)

#12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

var122 = [i for i in list(cadena) if i != ' ' and i != '.']
print('12. ', var122)

#13) Crear dos listas y unirlas en una tupla utilizando la función zip
var13 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
var131 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Fryday', 'Saturday', 'Sunday']

var132 = list(zip(var13, var131))
print('13. ', var132)

#14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lis14 = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

var141 = [i for i in lis14 if i%7 == 0]
print('14. ', var141)

#15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que 
# un elemento de la lista podría ser otra lista:<br>
lis15 = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
var15 = []

for i in lis15 :
    if type(i) == list:
        for y in i :
            var15.append(y)
    else:
        var15.append(i)
print('15. ', len(var15))


#16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
var16 = []

for i in lis15 : 
    i = list(i)
    var16.append(i)
print('16. ', var16)

