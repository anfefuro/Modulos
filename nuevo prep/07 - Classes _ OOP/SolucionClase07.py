## Clases y Programación Orientada a Objetos

from random import randint, randrange
import random
import re

 
#1) Crear la clase vehículo que contenga los atributos:<br>
#Color<br>
#Si es moto, auto, camioneta ó camión<br>
#Cilindrada del motor
class vehículo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.grados = 0
#2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
#Acelerar<br>
#Frenar<br>
#Doblar<br>
    def acelerar(self, vel):
        self.velocidad += vel
    def frenar(self, vel):
        self.velocidad -= vel
    def doblar(self, grd):
        self.grados += grd
#4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. 
# Y otro método que muestre color, tipo y cilindrada
    def estado(self):
        eDict = {}
        eDict['Velocidad'] = self.velocidad
        eDict['Dirección'] = self.grados
        return(eDict)
    def estilo(self):
        esDict = {}
        esDict['Color'] = self.color
        esDict['Tipo'] = self.tipo
        esDict['Cilindraje'] = self.cilindraje
        return(esDict)

#3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

obj1 = vehículo('Negro', 'Motocicleta', 180)
obj2 = vehículo('Plateado', 'Carro', 2000)
obj3 = vehículo('Rojo', 'Camion', 120)

obj1.acelerar(100)
obj2.acelerar(140)
obj3.acelerar(70)
obj1.frenar(-20)
obj2.frenar(-40)
obj3.frenar(-30)
obj1.doblar(40)
obj2.doblar(10)
obj3.doblar(50)
print('4.  Vehículo 1. ', obj1.estilo(), obj1.estado())
print('    Vehículo 2. ', obj2.estilo(), obj2.estado())
print('    Vehículo 3. ', obj3.estilo(), obj3.estado())

#4.  Vehículo 1.  {'Color': 'Negro', 
#                  'Tipo': 'Motocicleta',
#                  'Cilindraje': 180} 
#                 {'Velocidad': 120, 
#                  'Dirección': 40}
#    Vehículo 2.  {'Color': 'Plateado',
#                  'Tipo': 'Carro', 
#                  'Cilindraje': 2000}
#                 {'Velocidad': 180, 
#                  'Dirección': 10}
#    Vehículo 3.  {'Color': 'Rojo', 
#                  'Tipo': 'Camion', 
#                  'Cilindraje': 120} 
#                 {'Velocidad': 100, 
#                  'Dirección': 50}


#5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>

class tools:
    def __init__(self) -> None :
        pass
#Verificar Primo<br>
    def verificaPrimo(self, var01):
        esPrimo = True
        for i in range(2, var01):
            if var01 % i == 0 :
                esPrimo = False
        return(esPrimo)
#Valor modal<br>
    def masRepetido(self, listVer, var04) :
        var031 = {}
        var033 = {}
        var034 = {}
        if len(listVer) == 0 : return None
        for i in sorted(listVer) : 
            if i not in var031 :
                var031[i]=1
            else:
                var031[i] += 1
        for k, v in var031.items() :
            var033[v] = k
        if var04 == True :
            var034['Valor Modal'] = var033[max(var033)]
            var034['Repeticiones'] = max(var033)
            return(var034)
        else:
            var034['Valor Anti-Modal'] = var033[min(var033)]
            var034['Repeticiones'] = min(var033) 
            return(var034)
#Conversión grados<br>
    def conversor(self, valor, origen, destino) :
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
#Factorial<br>
    def factorial(self, var07):
        if type(var07) != int :
            return('Debe ser entero')
        elif var07 < 0 :
            return('Debe ser positivo') 
        elif var07 > 1 :
            var07 *= self.factorial(var07 - 1)
        elif var07 == 0 :
            return(None)
        return(var07)        

#6) Probar las funciones incorporadas en la clase del punto 5
var05 = tools()
var051 = [random.randint(1, 5) for i in range(10)]
val = 7
org = 'cel'
dst = 'far'
print('6. ', val, 'es primo:', var05.verificaPrimo(val))
print('   ', var05.masRepetido(var051, True))
print('   ', val, '°', org, 'a', dst, ':', var05.conversor(val, org, dst))
print('    Factorial de', val, ':', var05.factorial(val))

#7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
class tools07:
    def __init__(self, list07) :
        self.list07 = list07
    def __verificaPrimo__(self):
        list071 = [self.verificaPrimo(i) for i in self.list07]
        return(list(zip(self.list07, list071)))
    def __conversor__(self, origen, destino):
        list072 = [round((self.conversor(i, origen, destino)), 2) for i in self.list07]
        return(list(zip(self.list07, list072)))
    def __factorial__(self):
        list073 = [self.factorial(i) for i in self.list07]
        return(list(zip(self.list07, list073)))
#Verificar Primo<br>
    def verificaPrimo(self, var01):
        esPrimo = True
        for i in range(2, var01):
            if var01 % i == 0 :
                esPrimo = False
        return(esPrimo)
#Valor modal<br>
    def masRepetido(self, var04) :
        var031 = {}
        var033 = {}
        var034 = {}
        listVer = self.list07
        for i in sorted(listVer) : 
            if i not in var031 :
                var031[i]=1
            else:
                var031[i] += 1
        for k, v in var031.items() :
            var033[v] = k
        if var04 == True :
            var034['Valor Modal'] = var033[max(var033)]
            var034['Repeticiones'] = max(var033)
            return(var034)
        else:
            var034['Valor Anti-Modal'] = var033[min(var033)]
            var034['Repeticiones'] = min(var033) 
            return(var034)
#Conversión grados<br>
    def conversor(self, valor, origen, destino) :
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
#Factorial<br>
    def factorial(self, var07):
        if type(var07) != int :
            return('Debe ser entero')
        elif var07 < 0 :
            return('Debe ser positivo') 
        elif var07 > 1 :
            var07 *= self.factorial(var07 - 1)
        elif var07 == 0 :
            return(None)
        return(var07)

var071 = tools07(var051) 
print('7.  Verifica primos:', var071.__verificaPrimo__())
print('   ', var071.masRepetido(True), var051)
print('    De grados Celsius a Fahrenheit:', var071.__conversor__('cel', 'far'))
print('    Factoriales:', var071.__factorial__())

#8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del 
# módulo y probar alguna de sus funciones

from ToolsClase07 import *

var081 = [random.randint(1, 5) for i in range(10)]
var08 = tools08(var081)

print('8.  Verifica primos:', var08.__verificaPrimo__())
print('   ', var08.masRepetido(True), var081)
print('    De grados Fahrenheit a Kelvin:', var08.__conversor__('far', 'kel'))
print('    Factoriales:', var08.__factorial__())