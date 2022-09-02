#2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, 
# un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo 
# provisto "clase09_ej2.csv" una marca de tiempo y esa información.


import sys
import os

if len(sys.argv) == 2 :
    rainDay = sys.argv[1]
    temperature = input('Ingrese la temperatura en grados centigrados')
    humidity = input('Ingrese el porcentae de humedad: ')
    line = rainDay + ',' + temperature + ',' + humidity

    newLine = open('script02Clase09.csv', 'a') 
    newLine.write(line + '\n')
    newLine.close()
else:
    print('Error digite un elemento valido')
    print('Ejemplo, True o False') 