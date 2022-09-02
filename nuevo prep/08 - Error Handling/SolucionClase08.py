######python .\SolucionClase08.py#######

## Manejo de errores

#1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. 
# Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de 
# dato?
from Tools08 import *
######var01 = tools08('hola mundo', True)
var011 = [3,2,2,3,4,5,2]
var01 = tools08(var011)
print('1. ', var01.masRepetido(True))

#2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, 
# informar cuáles son los valores esperados.

print('2. Errors values', var01.conversor('error', 'error'))
print('   ', var01.conversor('cel', 'far'))

#3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
#Creacion del objeto incorrecta<br>
#Creacion correcta del objeto<br>
#Metodo valor_modal()<br>

import unittest

class proofMyClass(unittest.TestCase):
    def testCreateSecObj(self):
        param = 'hola'
        self.assertRaises(ValueError, tools08, param)

    def testCreateFirtsObj(self):
        param = [3,2,2,3,4,5,2]
        var03 = tools08(param)
        self.assertEqual(var03.list07, param)

    def testMasRepetido(self) :
        param = [3,2,2,3,4,5,2]
        var03 = tools08(param)
        modal, repes = var03.masRepetido(True)
        modalDic = {}
        modalDic[modal] = repes
        resultado = {2: 3}
        self.assertEqual(modalDic, resultado)

#print(var01.list07)

#Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta 
# funcionalidad.

#4) Probar una creación incorrecta y visualizar la salida del "raise"

#####  SE HIZO EN EL PRIMER PUNTO #####

#6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una
#  lista de True o False en función de que el elemento en la posisicón sea o no primo

class secProofClass(unittest.TestCase):
    def testVerificaPrimos(self):
        param = [3,2,2,3,4,5,2]
        var06 = tools08(param)
        var06 = var06.verificaPrimo()
        respuesta = [(3, True), (2, True), (2, True), (3, True), (4, False), (5, True), (2, True)]
        self.assertEqual(var06, respuesta)

#7) Agregar casos de pruebas para el método conversion_grados()
    def testConversor(self):
        param = [3,2,2,3,4,5,2]
        var07 = tools08(param)
        var07 = var07.conversor('cel', 'far')
        respuesta = [(3, 37.4), (2, 35.6), (2, 35.6), (3, 37.4), (4, 39.2), (5, 41.0), (2, 35.6)]
        self.assertEqual(var07, respuesta)

#8) Agregar casos de pruebas para el método factorial()
    def testFactorial(self):
        param = [3,2,2,3,4,5,2]
        var08 = tools08(param)
        var08 = var08.factorial()
        respuesta = [(3, 6), (2, 2), (2, 2), (3, 6), (4, 24), (5, 120), (2, 2)]
        self.assertEqual(var08, respuesta)

unittest.main(argv=[''], verbosity=2, exit=False)


