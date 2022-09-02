#1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente 
# esa cantidad, y muestre como salida los parámetros recibidos

import sys

if len(sys.argv) == 4 :
    print('El primer parametro es:', sys.argv[1])
    print('El segundo parametro es:', sys.argv[2])
    print('El tercer argumento es:', sys.argv[3])
else:
    print('Error, digite tres argumentos')
    print('Ejemplo, 1 2 3')