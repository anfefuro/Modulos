from cmath import pi
## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
var1 = 77
print('First point: ', var1);

# 2) Imprimir el tipo de dato de la constante 8.5
print('Second point: ',type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print('Third point: ', type(var1))

# 4) Crear una variable que contenga tu nombre
var4 = 'Felipe Fuentes' 

# 5) Crear una variable que contenga un número complejo
var5 = 10 + 20j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print('Sixth point: ', type(var5))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
print('Seventh point: ', round(pi, 4))

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
fakeBool = 'True'
realBool = True
print('Eighth point: No se trata del mismo tipo de variable, la primera es del tipo ', type(fakeBool), ' y la segunda es de tipo ', type(realBool))

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print('Nineth point: fakeBool, ', type(fakeBool), 'realBool, ', type(realBool))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
var10 = 10 + 10.01
print('Tenth point: ', var10)

# 11) Realizar una operación de suma de números complejos
var11 = 5j + 3j
print('Eleventh point: ', var11)

# 12) Realizar una operación de suma de un número real y otro complejo
var12 = var11 * 10
print('Twelfth point: ', var12)

# 13) Realizar una operación de multiplicación
var13 = 77 * 7
print('Thirdteenth point: ', var13)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
var14 = 2**8
print('Fourteenth point: ', var14)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
var15 = 27/4
print('Fifteen point: ', var15)

# 16) De la división anterior solamente mostrar la parte entera
var16 = 27 // 4
print('Sixteenth point: ', var16)

# 17) De la división de 27 entre 4 mostrar solamente el resto
var17 = 27 % 4
print('Seventeenth point: ', var17)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
var18 = (4 * var16) + var17
print('Eighteenth point: ', var18)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var19 = 'Is ' + 'This ' + 'It'
print('Nineteenth point: ', var19)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
var20 = '2'
var201 = 2
print('Twentieth point: ', var20 == var201)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print('Twentieoneth point: ', int(var20) == var201)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print('Twentietwoth point: 3,8 se concidera una tupla, en lugar de un flotante')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var23 = 3
var23 -= 2
print('Twentiethreeth point: ', var23)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print('Twentiefourth point: ', 1 << 2, 'Es un desplazamiento a la izquierda bit a bit, 1 es igual a 1 en binario, si se agregan dos ceros desplazando todo a a la izquierda se obtiene 100 o 4 en lenguaje natural, el sistema de numeracion binario es el refleo de valores en el lenguaje de la maquina')

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print('Twentiefiveth point: No esta permitido, en la mayoria de los casos, la suma de elementos de difente tipo. Si ambos elemntos son strings se realiza una concatenacion, si son enteros una suma ordinaria')

# 26) Realizar una operación válida entre valores de tipo entero y string
print('Twentiesixth point: ', 'ja' * 3)