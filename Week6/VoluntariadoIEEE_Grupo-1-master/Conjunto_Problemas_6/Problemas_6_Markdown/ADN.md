# ADN
Implemente un programa que identifique a una persona en función de su ADN, según se indica a continuación.
```
$ python dna.py bases de datos/secuencias large.csv/5.txt
Lavanda
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/dna.zip
```
para descargar un ZIP llamado ```dna.zip``` en su espacio de código.
Luego ejecuta
```
unzip dna.zip
```
para crear una carpeta llamada ```dna```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm dna.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.
Ahora escribe
```
cd dna
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
dna/ $
```
Ejecute ```ls``` por sí mismo, y debería ver algunos archivos y carpetas:
```
databases/ dna.py sequences/
```
Si se encuentra con algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde salió mal.
## Antecedentes
El ADN, el portador de la información genética en los seres vivos, se ha utilizado en la justicia penal durante décadas. Pero, ¿cómo funciona exactamente el perfil de ADN? Dada una secuencia de ADN, ¿cómo pueden los investigadores forenses identificar a quién pertenece?

Bueno, el ADN es realmente solo una secuencia de moléculas llamadas nucleótidos, dispuestas en una forma particular (una doble hélice). Cada célula humana tiene miles de millones de nucleótidos ordenados en secuencia. Cada nucleótido de ADN contiene una de cuatro bases diferentes: adenina (A), citosina (C), guanina (G) o timina (T). Algunas partes de esta secuencia (es decir, el genoma) son iguales, o al menos muy similares, en casi todos los humanos, pero otras partes de la secuencia tienen una mayor diversidad genética y, por lo tanto, varían más entre la población.

Un lugar donde el ADN tiende a tener una alta diversidad genética es en las repeticiones cortas en tándem (STR). Un STR es una secuencia corta de bases de ADN que tiende a repetirse consecutivamente numerosas veces en ubicaciones específicas dentro del ADN de una persona. La cantidad de veces que se repite un STR en particular varía mucho entre los individuos. En las muestras de ADN a continuación, por ejemplo, Alice tiene el STR AGAT repetido cuatro veces en su ADN, mientras que Bob tiene el mismo STR repetido cinco veces.
![](/Conjunto_Problemas_6/Problemas_6_Markdown/ADN.png)
El uso de varios STR, en lugar de uno solo, puede mejorar la precisión de los perfiles de ADN. Si la probabilidad de que dos personas tengan el mismo número de repeticiones para un solo STR es del 5 % y el analista observa 10 STR diferentes, entonces la probabilidad de que dos muestras de ADN coincidan por pura casualidad es de aproximadamente 1 en 1 cuatrillón (suponiendo que todos los STR son independientes entre sí). Entonces, si dos muestras de ADN coinciden en el número de repeticiones para cada uno de los STR, el analista puede estar bastante seguro de que provienen de la misma persona. CODIS, [la base de datos de
ADN](https://www.fbi.gov/how-we-can-help-you/dna-fingerprint-act-of-2005-expungement-policy/codis-and-ndis-fact-sheet) del FBI, utiliza 20 STR diferentes como parte de su proceso de perfilado de ADN.

¿Cómo sería una base de datos de ADN de este tipo? Bueno, en su forma más simple, podría imaginar formatear una base de datos de ADN como un archivo CSV, en el que cada fila corresponde a un individuo y cada columna corresponde a un STR en particular.
```
nombre,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```
Los datos del archivo anterior sugerirían que Alice tiene la secuencia ```AGAT``` repetida 28 veces consecutivas en algún lugar de su ADN, la secuencia ```AATG``` repetida 42 veces y ```TATC``` repetida 14 veces. Mientras tanto, Bob tiene esos mismos tres STR repetidos 17, 22 y 19 veces, respectivamente. Y Charlie tiene esos mismos tres STR repetidos 36, 18 y 25 veces, respectivamente.

Entonces, dada una secuencia de ADN, ¿cómo podrías identificar a quién pertenece? Bueno, imagina que buscas en la secuencia de ADN la secuencia consecutiva más larga de ```AGAT``` repetidos y encuentras que la secuencia más larga tiene 17 repeticiones. Si luego descubriera que la secuencia más larga de ```AATG``` tiene 22 repeticiones y la secuencia más larga de ```TATC``` tiene 19 repeticiones, eso proporcionaría una evidencia bastante buena de que el ADN era de Bob. Por supuesto, también es posible que una vez que haga el conteo de cada uno de los STR, no coincida con nadie en su base de datos de ADN, en cuyo caso no tendrá ninguna coincidencia.

En la práctica, dado que los analistas saben en qué cromosoma y en qué ubicación del ADN se encontrará un STR, pueden localizar su búsqueda en una sección estrecha del ADN. Pero ignoraremos ese detalle para este problema.

Su tarea es escribir un programa que tome una secuencia de ADN y un archivo CSV que contenga recuentos de STR para una lista de individuos y luego indique a quién pertenece el ADN (más probable).
## Especificación
En un archivo llamado dna.py, implemente un programa que identifique a quién pertenece una secuencia de ADN.

* El programa debe requerir como primer argumento de la línea de comandos el nombre de un archivo CSV que contenga los recuentos de STR para una lista de individuos y debe requerir como segundo argumento de la línea de comandos el nombre de un archivo de texto que contenga la secuencia de ADN para identificar.
    * Si su programa se ejecuta con el número incorrecto de argumentos de la línea de comandos, su programa debería imprimir un mensaje de error de su elección (con impresión). Si se proporciona la cantidad correcta de argumentos, puede suponer que el primer argumento es, de hecho, el nombre de archivo de un archivo CSV válido y que el segundo argumento es el nombre de archivo de un archivo de texto válido.
* Su programa debería abrir el archivo CSV y leer su contenido en la memoria.
    * Puede asumir que la primera fila del archivo CSV serán los nombres de columna. La primera columna será el ```nombre``` de la palabra y las columnas restantes serán las secuencias STR en sí mismas.
* Su programa debería abrir la secuencia de ADN y leer su contenido en la memoria.
* Para cada uno de los STR (desde la primera línea del archivo CSV), su programa debe calcular la serie más larga de repeticiones consecutivas del STR en la secuencia de ADN para identificar. Tenga en cuenta que hemos definido una función de ayuda para usted,``` longest_match```, ¡que hará exactamente eso!
* Si los recuentos de STR coinciden exactamente con cualquiera de las personas en el archivo CSV, su programa debe imprimir el nombre de la persona coincidente.
    * Puede asumir que los recuentos de STR no coincidirán con más de un individuo.
    * Si los recuentos de STR no coinciden exactamente con ninguna de las personas en el archivo CSV, su programa debe imprimir ``` No coincide``` .
 
## Uso
Su programa debe comportarse según el ejemplo a continuación:
```
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```
```
$ python dna.py
Uso: python dna.py data.csv sequence.txt
```
```
$ python dna.py data.csv
Uso: python dna.py data.csv sequence.txt
```
## Sugerencias
* Puede encontrar útil el módulo csv de Python para leer archivos ```CSV``` en la memoria. Es posible que desee aprovechar las ventajas de ```csv.reader``` o ```csv.DictReader```.
* Las funciones de ```open``` y ```read``` pueden ser útiles para leer archivos de texto en la memoria.
* Considere qué estructuras de datos podrían ser útiles para mantener el seguimiento de la información en su programa. Una ```lista``` o un ```dictado``` pueden resultar útiles.
* Recuerde que hemos definido una función (```longest_match```) que, dada una secuencia de ADN y un STR como entradas, devuelve el número máximo de veces que se repite el STR. ¡Entonces puede usar esa función en otras partes de su programa!
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python dna.py databases/small.csv sequences/1.txt```. Su programa debe generar ```Bob```.
* Ejecute su programa como ```python dna.py databases/small.csv sequences/2.txt```. Su programa debe generar ```No hay coincidencia```.
* Ejecute su programa como ```python dna.py databases/small.csv sequences/3.txt```. Su programa debe generar ```No hay coincidencia```.
* Ejecute su programa como ```python dna.py databases/small.csv sequences/4.txt```. Su programa debe generar ```Alice```.
* Ejecute su programa como ```python dna.py databases/large.csv sequences/5.txt```. Su programa debe generar ```Lavanda```. 
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/6.txt```. Su programa debe generar ```Luna```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/7.txt```. Su programa debe generar ```Ron```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/8.txt```. Su programa debe generar ```Ginny```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/9.txt```. Su programa debe generar ```Draco```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/10.txt```. Su programa debe generar ```Albus```. 
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/11.txt```. Su programa debe generar ```Hermione```. 
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/12.txt```. Su programa debe generar ```Lily```. 
* Ejecute su programa como ```python dna.py databases/large.csv sequences/13.txt```. Su programa debe generar ```No hay coincidencia```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/14.txt```. Su programa debe generar ```Severus```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/15.txt```. Su programa debe generar ```Sirius```.
* Ejecute su programa como ```python dna.py databases/large.csv sequences/16.txt```. Su programa debe generar ```No hay coincidencia```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/17.txt```. Su programa debe generar ```Harry```.
* Ejecute su programa como ```python dna.py databases/large.csv sequences/18.txt```. Su programa debe generar ```No hay coincidencia```.
*  Ejecute su programa como ```python dna.py databases/large.csv sequences/19.txt```. Su programa debe generar ```Fred```.
* Ejecute su programa como ```python dna.py databases/large.csv sequences/20.txt```. Su programa debe generar ```No hay coincidencia```.
Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/dna
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 dna.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/dna
```