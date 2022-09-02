#3) Crear un archivo a partir de los datos presentes en el diccionario provisto. El cual debe contener en la primera fila 
# el nombre de las claves y luego cada línea los elementos i-ésimos de las listas de valores contiguos y separados por 
# coma ','. Este archivo debe llamarse clase09_ej3.csv
import os

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

mFile = open('script03.csv', 'w')

##Para agregar los titulos##
for k in montañas.keys():
    if k == 'altura':
        mFile.write(k + '\n')
    else:
        mFile.write(k + ',')

i = 0
while (i < 10):
    mFile.write(montañas['nombre'][i] + ',')
    mFile.write(str(montañas['orden'][i]) + ',')
    mFile.write(montañas['cordillera'][i] + ',')
    mFile.write(montañas['pais'][i] + ',')
    mFile.write(str(montañas['altura'][i]) + '\n')
    i += 1 

mFile.close()

#4) Mostrar el tamaño en MB del archivo generado en el punto 3

print('Tamaño', (os.path.getsize('script03.csv')/1024))