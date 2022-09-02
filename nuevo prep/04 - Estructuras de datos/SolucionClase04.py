## Estructuras de Datos

#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
var01 = ['Cali', 'Medellin', 'Bucaramanga', 'Pasto', 'Girardot', 'Pamplona', 'Yopal', 'San Jose']
print('1. ', var01)

#2) Imprimir por pantalla el segundo elemento de la lista
print('2. ', var01[1])

#3) Imprimir por pantalla del segundo al cuarto elemento
print('3. ', var01[1:4])

#4) Visualizar el tipo de dato de la lista
print('4. ', type(var01))

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print('5. ', var01[2:])

#6) Visualizar los primeros 4 elementos de la lista
print('6. ', var01[:4])

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
var01.append('Girardot')
var01.append('Neiva')
print('7. Sin Errores', var01)

#8) Agregar otra ciudad, pero en la cuarta posición
var01.insert(3, 'Villavicencio')
print('8. ', var01)

#9) Concatenar otra lista a la ya creada
var09 = ['Bogota', 'Cucuta', 'Manizales', 'Tunja', 'Mitu', 'Caqueta', 'Santa Marta']
var01.extend(var09)
print('9. ', var01)

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print('10. Particularidad: Retorna solo el primer indice: ', var01.index('Girardot'))

#11) ¿Qué pasa si se busca un elemento que no existe?
print('11. var01.index(*Riohacha*), Retorna: ValueError: *Riohacha* is not in list')

#12) Eliminar un elemento de la lista
var01.remove('Bogota')
print('12. ', var01)

#13) ¿Qué pasa si el elemento a eliminar no existe?
print('13. var01.remove(*Riohacha*), Retorna: ValueError: list.remove(x): x not in list')

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
var14 = var01.pop()
print('14. ', var14)

#15) Mostrar la lista multiplicada por 4
print('15. ', var01*4)

#16) Crear una tupla que contenga los números enteros del 1 al 20
var16 = []

for i in range(1, 21) : 
    var16.append(i)

var16 = tuple(var16)
print('16. ', var16)

#17) Imprimir desde el índice 10 al 15 de la tupla
print('17. ', var16[9:15])

#18) Evaluar si los números 20 y 30 están dentro de la tupla
print('18. 20 esta en la tupla: ', 20 in var16)
print('    30 no esta en la tupla: ', 30 in var16)

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print('19.', 'Paris' in var01)
var01.append('Paris')
var19 = var01
print(' ...Ahora Paris exist: ', var19)

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print('20. Count Girardot in List:', var19.count('Girardot'))
print('... Count 10 in tuple:', var16.count(10))

#21) Convertir la tupla en una lista
var21 = list(var16)
print('21. ', var21)

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
var22 = 'Salud', 'Dinero', 'Amor'
var221, var222, var223 = var22
print('22. ', '1ro:', var221, ', 2do:', var222, ', 3ro:', var223)

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
var23 = {}
var23['Ciudad'] = var01
var23['Pais'] = ['Mexico', 'Honduras', 'Nicaragua', 'Costa Rica', 'Puerto Rico', 'Panama', 'Cuba']
var23['Continente'] = ['America Central', 'America del Sur', 'Asia', 'Africa']

print('23. ', var23)

#24) Imprimir las claves del diccionario
print('24. ', var23.keys())

#25) Imprimir las ciudades a través de su clave
print('25. ', var23['Ciudad'])