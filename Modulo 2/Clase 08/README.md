![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# Tests Estadísticos

Por lo general, en la práctica, se tienen que tomar decisiones sobre poblaciones, partiendo de la información muestral de las mismas. Tales decisiones se llaman, decisiones estadísticas.<br>
Para tomar decisiones conviene hacer determinados supuestos y tales supuestos son formulados respecto del valor de algún parámetro, que pueden ser o no ciertos. A estos los denominamos Hipótesis Estadísticas y, en general, lo son sobre las distribuciones de probabilidad de las poblaciones.<br>
En el procedimiento de test estadísticos, se utilizan las denominadas pruebas de hipótesis y en ellas se usan datos de una muestra para probar dos afirmaciones contrarias indicadas por H0 (hipótesis nula) y Ha (la hipótesis alternativa).<br>
Suponga que las notas promedios de un Henry Challenge es de 78, Henry determina que a través de métodos innovadores puede aumentar esa media. En este caso, se establece un grupo de investigación que busca evidencias para concluir que el nuevo sistema aumenta la media del rendimiento. La hipótesis de investigación es, entonces, que el nuevo sistema proporciona un rendimiento medio mayor; es decir, μ > 78. Como lineamiento general, una hipótesis de investigación se debe plantear como hipótesis alternativa. Por tanto, en este estudio las hipótesis nula y alternativa adecuadas son "H0: μ<= 78" y "H1: μ> 78".<br>
Si los resultados obtenidos con la muestra indican que no se puede rechazar H0, el grupo no concluirán que el nuevo sistema sea mejor. Quizá será necesario continuar investigando y realizar nuevas pruebas. Pero si los resultados muestrales indican que se
puede rechazar H0, inferirán que Ha: μ > 78 es verdadera. Esta conclusión proporciona el apoyo estadístico necesario para afirmar que el nuevo sistema aumenta el rendimiento. Se considerará la implementación del nuevo sistema.<br>
En estudios de investigación como éste, las hipótesis nula y alternativa deben formularse de manera que al rechazar H0 se apoye la conclusión de la investigación. La hipótesis de la investigación, entonces, debe expresarse como hipótesis alternativa.<br>
Cuando lo que realizamos es una afirmación, en este caso sería que quienes rinden un HC obtienen por lo menos 78 puntos en promedio, la "H0: μ>= 78" y "H1: μ< 78". Es decir que en toda situación en la que se desee probar la validez de una afirmación, la hipótesis nula se suele basar en la suposición de que la afirmación sea verdadera. Entonces, la hipótesis alternativa se formula de manera que rechazar H0 proporcione la evidencia estadística de que la suposición establecida es incorrecta.<br>

Existen además otras formas de realizar el planteo de H0 y H1, como cuando se debe tomar una decisión. Como por ejemplo controlar la calidad de un determinado respuesto en donde debe medir obligatoriamente 10 cm. "H0: μ= 10" y "H1: μ!= 10". Lo que determina solo dos alternativas.

![test](/_src/assets/hipotesis.PNG)

METODOLOGÍA DE LA PRUEBA DE HIPÓTESIS: DEFINICIÓN DE ETAPAS

1. Formular la hipótesis nula.<br>
2. Formular la hipótesis alternativa.<br>
3. Especificar el nivel de significación.<br>
4. Determinar el tamaño de la muestra.<br>
5. Determinar el estadístico de prueba.<br>
6. Establecer los valores críticos que dividen las zonas de rechazo y de no rechazo.<br>
7. Obtener los datos y calcular los estadísticos.<br>
8. Determinar el estadístico de prueba ha caído en la región de rechazo o en la de no rechazo.<br>
9. Determinar la decisión estadística.<br>
10. Expresar la decisión estadística en términos del problema.<br>

### Especificar el nivel de significación

La distribución muestral del estadístico analizado, suele seguir una distribución estadística conocida, como la distribución normal estandarizada, la distribución t o la distribución chi cuadrado, éstas se utilizan como ayuda para determinar si la hipótesis nula es cierta.

Existen dos tipos de errores: <br>
- Error de tipo I: Es la probabilidad de que se rechace la hipótesis nula cuando es verdadera. Se conoce como nivel de significancia. <br>
- Error de tipo II: Es la probabilidad de aceptar la hipótesis nula cuando es falsa. Se conoce como la potencia de la prueba.

El error de tipo I que se llama también nivel de significación, determina el nivel de riesgo que se está dispuesto a tolerar en términos de rechazo de una hipótesis verdadera (imagina rechazar algo que en realidad era cierto,¡que problema!). La selección del nivel de Error I particular de riesgo, depende de la importancia (significación) del problema. En otras palabras, si se encuentra que los resultados observados en una muestra al azar difieren mar cadamente de aquellos que cabría esperar con la hipótesis y la variación propia del muestreo, se diría que las diferencias observadas son significativas y se estaría en condiciones de rechazar la hipótesis. Habitualmente se trabaja con niveles de significación del 1% y del 5%.

![conlusion](/_src/assets/significa.PNG)

### Determinar el tamaño de la muestra.<br>
El tamaño de la muestra se determina al tomar en cuenta la importancia de Error I y Error II y al considerar las restricciones presupuestarias al efectuar el estudio. Generalmente las muestras grandes, permiten detectar incluso diferencias pequeñas entre los valores hipotéticos los parámetros poblacionales. Para un nivel de Error I dado, aumentar el tamaño de la muestra reducirá Error II y así se incrementará el poder de la prueba para detectar que la hipótesis nula es falsa. Sin embargo, esto implica un aumento de los costos del estudio, por lo que las restricciones presupuestarias afectarán el tamaño de la muestra que se tomará.<br>
La fórmula para determinar el tamaño de muestra mínimo requerido para una prueba de
hipótesis de la media, usando la distribución normal es:

El valor z0 es el valor crítico de z que surge del nivel de significación especificado (Error I), mientras que z1 es el valor respecto de la probabilidad del error de tipo II asignada. El valor de la varianza debe conocerse o utilizar su estimador. Esta fórmula puede emplearse lo mismo para pruebas unilaterales que bilaterales. El único valor que difiere en estos dos tipos de pruebas es el valor de z0 utilizado.

### Determinar el estadístico de prueba.<br>
Una vez definidas las hipótesis nula y alternativa, y el tamaño de la muestra se puede establecer la distribución a utilizar: normal, t- student ó chi cuadrado.

### Establecer los valores críticos que dividen las zonas de rechazo y de no rechazo.<br>
Para poder establecer un método objetivo, que permita comparar los resultados muestrales con la hipótesis nula, el “nivel de significación”, se representa como un área (como toda probabilidad en una función de densidad), que se ubica a la derecha, a la izquierda o a ambos lados (en este caso, con la mitad de  en cada lado) según como se haya definido la Hipótesis alternativa. Esta probabilidad permite encontrar, en la tabla correspondiente (normal, t de Student o chi cuadrado), un valor de la variable (z, t ó ) denominado “valor crítico” simbolizado con zc (o eventualmente tc ó c), que divide al eje de las abscisas en dos zonas: la “zona de rechazo”, que se extiende por debajo de , y la “zona de no rechazo”, que se extiende a lo largo del resto del eje.

### Obtener los datos y calcular los estadísticos.<br>
Este paso está reservado a la efectiva realización de la investigación muestral. Es decir que en este momento es cuando se realiza el estudio tendiente a obtener los valores muestrales y calcular los estadísticos.

### Determinar el estadístico de prueba ha caído en la región de rechazo o en la de no rechazo.<br>
Se debe determinar la técnica a utilizar para determinar si el estadístico muestral ha caído en la región de rechazo o en la de no rechazo, es decir, el modo en que el estadístico de la muestra se va a comparar con el parámetro hipotético. El estadístico de prueba puede ser el estadístico muestral (el estimador insesgado del parámetro que se prueba) o una versión transformada de ese estadístico muestral.<br>
La forma de verificar la validez del supuesto formulado, consiste en comparar el parámetro poblacional con el estadístico muestral:

![resumen](/_src/assets/estadistico.PNG)

El procedimiento para efectuar esta comparación, consiste en construir una variable estandarizada zi cuando n > 30, porque al estar trabajando con una muestra grande las estadísticas tienen Distribución Normal, en cuyo numerador aparece, precisamente, la diferencia entre media poblacional y media muestra , o entre varianza poblacional  y varianza muestral es decir:

![resumen](/_src/assets/z.PNG)

o en su defecto la variable t de Student ó chi cuadrado (si se tratara de n ≤ 30 y no conocemos el desvío estandar poblacional), haciendo:

![resumen](/_src/assets/t.PNG)

El valor del estadístico de prueba. se compara con el valor crítico en la distribución apropiada, para determinar si cae en la zona de rechazo o en la de no rechazo.

### Determinar la decisión estadística.<br>

Se determina la decisión de la prueba de hipótesis

- si z1 > zc entonces z1 cae en la “zona de rechazo” y se considera que las diferencias entre z1 y zc son significativas entonces Rechazo la Hipótesis nula.

- si z1 ≤ zc entonces z1 cae en la “zona de no rechazo” y se considera que las diferencias entre z1 y zc no son significativas entonces No Rechazo la Hipótesis nula.

### Expresar la decisión estadística en términos del problema.<br>
Una vez tomada la decisión, se deben expresar sus consecuencias en términos del problema particular.


![resumen](/_src/assets/prueba2.PNG)


![test](/_src/assets/pruebahip.PNG)


## Pruebas de hipótesis para la media poblacional.<br>

En el cálculo de las prubas de hipótesis, debemos estandarizar las variables a fin de poder estimar la zona en la cual se encuentra la prueba, esto se determina mediante la busqueda de los valores de z para el nivel de siginificancia en las tablas correspondientes (normal, t, chi cuadrado). Para un nivel del sigifincancia de 0.05 y una prueba de dos colas. el valor de z 

Cuando nos encontramos frente a una prueba de hipótesis del tipo: "H0: μ<= x" y "H1: μ> x" o "H0: μ>= x" y "H1: μ< x" , la denominamos prueba de una cola.

![prueba2](/_src/assets/unacola.jpg)

Cuando nos encontramos frente a una prueba de hipótesis del tipo: "H0: μ= x" y "H1: μ!= 1x", la denominamos prueba de dos colas.

![prueba2](/_src/assets/doscolas.png)

## Homework

1. Un fabricante de neumáticos informa que el promedio de km que se puede recorrer con ellos es de 50.000km la desviación estandar es de 4.000 km. Usted decide comprar 80 neumáticos y decide corroborar la afirmación del fabricante. Si su medición da una media de 49.600km.<br>
- Determine la hipótesis nula y alternativa.<br>
- ¿Consedería correcto lo expresado por el fabricante para un nivel de significancia del 0.05?.<br>
- ¿A partir de que valor de media muestral se ecuentra la zona de rechazo?
- ¿Consedería correcto lo expresado por el fabricante para un nivel del 0.01?. <br>
- ¿A partir de que valor de media muestral se ecuentra la zona de rechazo?

2. Los alumnos de Henry, obtienen en promedio una puntuación de 78 en un HC con una desviación estándar de 15 puntos. Henry determina que a través de métodos innovadores puede aumentar esa media. Considerando la hipótesis de investigación de que el nuevo sistema proporciona un rendimiento medio mayor; es decir, μ > 78. El grupo de investigación tomo una muestra de 45 alumnos y obtiene notas promedio de 80 puntos.
- Determine la hipótesis nula y alternativa.<br>
- ¿Determine si el nuevo sistema realmente mejoro el rendimiento para un nivel de significancia del 0.05?.<br>
- ¿A partir de que valor de media muestral se ecuentra la zona de rechazo?
- ¿Determine si el nuevo sistema realmente mejoro el rendimiento para un nivel de significancia del 0.01?.<br>
- ¿A partir de que valor de media muestral se ecuentra la zona de rechazo?

<table class="hide" width="100%" style='table-layout:fixed;'>
  <tr>
    <td>
      <a href="https://airtable.com/shrSzEYT4idEFGB8d?prefill_clase=00-PrimerosPasos">
        <img src="https://static.thenounproject.com/png/204643-200.png" width="100"/>
        <br>
        Hacé click acá para dejar tu feedback sobre esta clase.
      </a>
    </td>
  </tr>
</table>
