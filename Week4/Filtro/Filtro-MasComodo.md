# Filtro

Implemente un programa que aplique filtros a las BMP, según se indica a continuación.
```
$ ./filter -r IMAGE.bmp REFLECTED.bmp
```
donde ```IMAGE.bmp``` es el nombre de un archivo de imagen y ```REFLECTED.bmp``` es el nombre dado a un archivo de imagen de salida, ahora reflejado.

## Fondo
### Mapas de bits
Quizás la forma más sencilla de representar una imagen es con una cuadrícula de píxeles (es decir, puntos), cada uno de los cuales puede ser de un color diferente. Para las imágenes en blanco y negro, necesitamos 1 bit por píxel, ya que 0 podría representar el negro y 1 podría representar el blanco, como se muestra a continuación.

<img src="https://cs50.harvard.edu/x/2022/psets/4/filter/less/bitmap.png" width="600" height="300" />

En este sentido, entonces, una imagen es solo un mapa de bits. Para imágenes más coloridas, simplemente necesita más bits por píxel. Un formato de archivo (como [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG) o [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) que admita "24 bits de color" utiliza 24 bits por píxel. (BMP en realidad admite 1, 4, 8, 16, 24 y 32 bits de color).

Un BMP de 24 bits utiliza 8 bits para indicar la cantidad de rojo en el color de un píxel, 8 bits para indicar la cantidad de verde en el color de un píxel y 8 bits para indicar la cantidad de azul en el color de un píxel. Si alguna vez has oído hablar del color RGB, ahí lo tienes: rojo, verde, azul; por sus siglas en inglés (red, green, blue).

Si los valores R, G y B de algún píxel en un BMP son, por ejemplo, ```0xff```, ```0x00``` y ```0x00``` en hexadecimal, ese píxel es puramente rojo, ya que ```0xff``` (también conocido como ```255``` en decimal) implica "mucho rojo", mientras que ```0x00``` y ```0x00``` implica "sin verde" y "sin azul", respectivamente.

### Un mapa de bits más técnico
Recuerde que un archivo es solo una secuencia de bits, organizados de alguna manera. Un archivo BMP de 24 bits, entonces, es esencialmente solo una secuencia de bits, (casi) cada 24 de los cuales representan el color de algún píxel. Pero un archivo BMP también contiene algunos "metadatos", información como la altura y el ancho de una imagen. Esos metadatos se almacenan al comienzo del archivo en forma de dos estructuras de datos generalmente denominadas "encabezados", que no deben confundirse con los archivos de encabezado de C. (Dicho sea de paso, estos encabezados han evolucionado con el tiempo. Este problema usa la última versión del formato BMP de Microsoft, 4.0, que debutó con Windows 95).

El primero de estos encabezados, denominado ```BITMAPFILEHEADER```, tiene una longitud de 14 bytes. (Recuerde que 1 byte equivale a 8 bits). El segundo de estos encabezados, denominado ```BITMAPINFOHEADER```, tiene una longitud de 40 bytes. Inmediatamente después de estos encabezados se encuentra el mapa de bits real: una matriz de bytes, los triples de los cuales representan el color de un píxel. Sin embargo, BMP almacena estos triples al revés (es decir, como BGR), con 8 bits para azul, seguidos de 8 bits para verde, seguidos de 8 bits para rojo. (Algunos BMP también almacenan el mapa de bits completo al revés, con la fila superior de una imagen al final del archivo BMP. Pero hemos almacenado los BMP de este conjunto de problemas como se describe aquí, con la fila superior de cada mapa de bits primero y la fila inferior al final). En otras palabras, si tuviéramos que convertir el emoticón de 1 bit anterior en un emoticón de 24 bits, sustituyendo el rojo por el negro, un BMP de 24 bits almacenaría este mapa de bits de la siguiente manera, donde ```0000ff``` significa rojo y ```ffffff``` significa blanco; hemos resaltado en rojo todas las instancias de ```0000ff```.

<img src="https://cs50.harvard.edu/x/2022/psets/4/filter/less/red_smile.png" width="600" height="300" />

Debido a que hemos presentado estos bits de izquierda a derecha, de arriba a abajo, en 8 columnas, en realidad puedes ver el emoticón rojo si das un paso atrás.

Para que quede claro, recuerde que un dígito hexadecimal representa 4 bits. En consecuencia, ```ffffff``` en hexadecimal en realidad significa ```111111111111111111111111``` en binario.

Tenga en cuenta que podría representar un mapa de bits como una matriz bidimensional de píxeles: donde la imagen es una matriz de filas, cada fila es una matriz de píxeles. De hecho, así es como hemos elegido representar las imágenes de mapa de bits en este problema.

### Filtrado de imágenes
¿Qué significa filtrar una imagen? Puede pensar en filtrar una imagen como tomar los píxeles de una imagen original y modificar cada píxel de tal manera que un efecto particular sea evidente en la imagen resultante.

#### Escala de grises
Un filtro común es el filtro de "escala de grises", donde tomamos una imagen y queremos convertirla a blanco y negro. ¿Cómo funciona?

Recuerde que si los valores rojo, verde y azul están todos establecidos en ```0x00``` (hexadecimal para ```0```), entonces el píxel es negro. Y si todos los valores se establecen en ```0xff``` (hexadecimal para ```255```), entonces el píxel es blanco. Siempre que los valores de rojo, verde y azul sean todos iguales, el resultado será una variedad de tonos de gris a lo largo del espectro blanco y negro, donde los valores más altos significan tonos más claros (más cerca del blanco) y los valores más bajos significan tonos más oscuros (más cerca del negro).

Entonces, para convertir un píxel a escala de grises, solo debemos asegurarnos de que los valores rojo, verde y azul tengan el mismo valor. Pero, ¿cómo sabemos qué valor para hacerlos? Bueno, probablemente sea razonable esperar que si los valores originales de rojo, verde y azul eran bastante altos, entonces el nuevo valor también debería ser bastante alto. Y si los valores originales eran todos bajos, entonces el nuevo valor también debería ser bajo.

De hecho, para garantizar que cada píxel de la nueva imagen aún tenga el mismo brillo u oscuridad general que la imagen anterior, podemos tomar el promedio de los valores de rojo, verde y azul para determinar qué tono de gris crear el nuevo píxel.

Si aplica eso a cada píxel de la imagen, el resultado será una imagen convertida a escala de grises.

### Reflexión
Algunos filtros también pueden mover píxeles. Reflejar una imagen, por ejemplo, es un filtro donde la imagen resultante es la que obtendrías al colocar la imagen original frente a un espejo. Entonces, cualquier píxel en el lado izquierdo de la imagen debería terminar en el derecho, y viceversa.

Tenga en cuenta que todos los píxeles originales de la imagen original aún estarán presentes en la imagen reflejada, solo que esos píxeles pueden haberse reorganizado para estar en un lugar diferente en la imagen.

### Difuminar
Hay varias formas de crear el efecto de difuminar o suavizar una imagen. Para este problema, usaremos el "desenfoque de cuadro", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles vecinos.

Considere la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.

<img src="https://cs50.harvard.edu/x/2022/psets/4/filter/less/grid.png" width="300" height="300" />

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando un cuadro de 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (tenga en cuenta que el píxel 6 en sí está incluido en el promedio). Asimismo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel a lo largo del borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.


### Bordes
En los algoritmos de inteligencia artificial para el procesamiento de imágenes, suele ser útil detectar bordes en una imagen: líneas en la imagen que crean un límite entre un objeto y otro. Una forma de lograr este efecto es aplicando el [operador de Sobel ](https://es.wikipedia.org/wiki/Operador_Sobel#:~:text=El%20operador%20Sobel%20es%20utilizado,de%20intensidad%20de%20una%20imagen.) a la imagen.

Al igual que el desenfoque de la imagen, la detección de bordes también funciona tomando cada píxel y modificándolo en función de la cuadrícula de píxeles de 3x3 que rodea ese píxel. Pero en lugar de simplemente tomar el promedio de los nueve píxeles, el operador de Sobel calcula el nuevo valor de cada píxel tomando una suma ponderada de los valores de los píxeles circundantes. Y dado que los bordes entre los objetos pueden tener lugar tanto en dirección vertical como horizontal, en realidad calculará dos sumas ponderadas: una para detectar bordes en la dirección x y otra para detectar bordes en la dirección y. En particular, utilizará los siguientes dos "núcleos":

<img src=https://cs50.harvard.edu/x/2022/psets/4/filter/more/sobel.png width="600" height="300" />

¿Cómo interpretar estos núcleos? En resumen, para cada uno de los tres valores de color de cada píxel, calcularemos dos valores ```Gx``` y ```Gy```. Para calcular ```Gx``` para el valor del canal rojo de un píxel, por ejemplo, tomaremos los valores rojos originales de los nueve píxeles que forman un cuadro de 3x3 alrededor del píxel, los multiplicaremos por el valor correspondiente en el núcleo ```Gx``` y tomaremos la suma de los valores resultantes.

¿Por qué estos valores particulares para el núcleo? En la dirección ```Gx```, por ejemplo, multiplicamos los píxeles a la derecha del píxel de destino por un número positivo y multiplicamos los píxeles a la izquierda del píxel de destino por un número negativo. Cuando tomamos la suma, si los píxeles de la derecha son de un color similar a los píxeles de la izquierda, el resultado será cercano a 0 (los números se cancelan). Pero si los píxeles de la derecha son muy diferentes de los píxeles de la izquierda, el valor resultante será muy positivo o muy negativo, lo que indica un cambio de color que probablemente sea el resultado de un límite entre los objetos. Y un argumento similar es válido para calcular aristas en la dirección ```y```.

Con estos núcleos, podemos generar un valor ```Gx``` y ```Gy``` para cada uno de los canales rojo, verde y azul de un píxel. Pero cada canal solo puede tomar un valor, no dos: por lo que necesitamos alguna forma de combinar ```Gx``` y ```Gy``` en un solo valor. El algoritmo de filtro de Sobel combina ```Gx``` y ```Gy``` en un valor final al calcular la raíz cuadrada de ```Gx^2 + Gy^2```. Y dado que los valores del canal solo pueden tomar valores enteros de 0 a 255, ¡asegúrese de que el valor resultante se redondee al entero más cercano y se limite a 255!

¿Y qué pasa con el manejo de píxeles en el borde o en la esquina de la imagen? Hay muchas maneras de manejar los píxeles en el borde, pero para los propósitos de este problema, le pediremos que trate la imagen como si hubiera un borde negro sólido de 1 píxel alrededor del borde de la imagen: por lo tanto, intentar acceder un píxel más allá del borde de la imagen debe tratarse como un píxel negro sólido (valores de 0 para cada rojo, verde y azul). Esto ignorará efectivamente esos píxeles de nuestros cálculos de ```Gx``` y ```Gy```.

## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana de su terminal y ejecute ```cd```. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente:
```
$
```
A continuación ejecute
```
wget https://cdn.cs50.net/2021/fall/psets/4/filter-more.zip
```
para descargar un ZIP llamado ```filter-more.zip``` a su espacio de códigos.

Luego ejecute
```
unzip filter-more.zip
```
para crear una carpeta llamada ```filter-more```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm filter-more.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba
```
cd filter-more
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
filter-more/ $
```
Ejecute ```ls```, y debería ver algunos archivos: ```bmp.h```, ```filter.c```, ```helpers.h```, ```helpers.c``` y ```Makefile``` . También debería ver una carpeta llamada ```images``` con cuatro archivos BMP. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

## Comprensión
Ahora echemos un vistazo a algunos de los archivos que se le proporcionaron como código de distribución para comprender qué hay dentro de ellos.

### ```bmp.h```
Abra ```bmp.h``` (haciendo doble clic en él en el explorador de archivos) y eche un vistazo.

Verá definiciones de los encabezados que hemos mencionado (```BITMAPINFOHEADER``` y ```BITMAPFILEHEADER```). Además, ese archivo define los tipos de datos```BYTE```, ```DWORD```, ```LONG``` y ```WORD```, que normalmente se encuentran en el mundo de la programación. Observe cómo son solo alias para primitivos con los que (con suerte) ya está familiarizado. Parece que ```BITMAPFILEHEADER``` y ```BITMAPINFOHEADER``` hacen uso de estos tipos.

Quizás lo más importante para usted es que este archivo también define un ```struct``` llamado ```RGBTRIPLE``` que, simplemente, "encapsula" tres bytes: uno azul, uno verde y uno rojo (el orden, recuerde, en el que esperamos encontrar triples RGB en el disco).

¿Por qué son útiles estos ```struct```s? Bueno, recuerde que un archivo es solo una secuencia de bytes (o, en última instancia, bits) en el disco. Pero esos bytes generalmente se ordenan de tal manera que los primeros representan algo, los siguientes representan otra cosa, y así sucesivamente. Los "formatos de archivo" existen porque el mundo ha estandarizado qué bytes significan qué. Ahora, podríamos simplemente leer un archivo del disco a la RAM como una gran matriz de bytes. Y podríamos simplemente recordar que el byte en ```array[i]``` representa una cosa, mientras que el byte en ```array[j]``` representa otra. Pero, ¿por qué no dar nombres a algunos de esos bytes para que podamos recuperarlos de la memoria más fácilmente? Eso es precisamente lo que las estructuras en ```bmp.h``` nos permiten hacer. En lugar de pensar en un archivo como una secuencia larga de bytes, podemos pensar en él como una secuencia de ```struct```s.

### ```filter.c```
Ahora, abramos ```filter.c```. Este archivo ya se ha escrito para usted, pero hay un par de puntos importantes que vale la pena señalar aquí.

Primero, observe la definición de ```filtros``` en la línea 10. Esa cadena le dice al programa cuáles son los argumentos de línea de comando permitidos para el programa: ```b```, ```e```, ```g``` y ```r```. Cada uno de ellos especifica un filtro diferente que podemos aplicar a nuestras imágenes: desenfoque, detección de bordes, escala de grises y reflexión.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea un archivo BMP y leen toda la información de píxeles en una matriz 2D llamada ```imagen```.

Desplácese hacia abajo hasta la declaración de ```cambio``` que comienza en la línea 101. Observe que, según el ```filtro``` que hayamos elegido, se llama a una función diferente: si el usuario elige el filtro ```b```, el programa llama a la función de ```desenfoque```; si ```e```, entonces se llama ```bordes```; si ```g```, entonces se llama ```escala de grises```; y si ```r```, entonces se llama ```reflect```. Observe también que cada una de estas funciones toma como argumentos la altura de la imagen, el ancho de la imagen y la matriz 2D de píxeles.

Estas son las funciones que (¡pronto!) implementarás. Como puede imaginar, el objetivo es que cada una de estas funciones edite la matriz 2D de píxeles de tal manera que se aplique el filtro deseado a la imagen.

Las líneas restantes del programa toman la ```imagen``` resultante y las escriben en un nuevo archivo de imagen.

### ```helpers.h```
A continuación, eche un vistazo a ```helpers.h```. Este archivo es bastante corto y solo proporciona los prototipos de funciones para las funciones que vio anteriormente.

Aquí, tome nota del hecho de que cada función toma una matriz 2D llamada ```imagen``` como argumento, donde la ```imagen``` es una matriz de muchas filas de ```alto```, y cada fila es en sí misma otra matriz de muchos ```RGBTRIPLE``` de ```ancho```. Entonces, si la ```imagen``` representa la imagen completa, la ```imagen[0]``` representa la primera fila y la ```imagen[0][0]``` representa el píxel en la esquina superior izquierda de la imagen.

### ```helpers.c```
Ahora, abre ```helpers.c```. Aquí es donde pertenece la implementación de las funciones declaradas en ```helpers.h```. ¡Pero tenga en cuenta que, en este momento, faltan las implementaciones! Esta parte depende de ti.

### ```Makefile```
Finalmente, echemos un vistazo a ```Makefile```. Este archivo especifica lo que debería suceder cuando ejecutamos un comando de terminal como ```make filter```. Mientras que los programas que puede haber escrito antes estaban limitados a un solo archivo, el ```filtro``` parece usar varios archivos: ```filter.c```, ```bmp.h```, ```helpers.h``` y ```helpers.c```. Así que tendremos que decirle a ```make``` cómo compilar este archivo.

Intente compilar el ```filtro``` usted mismo yendo a su terminal y ejecutando
```
$ make filter
```
Luego, puede ejecutar el programa ejecutando:
```
$ ./filter -g images/yard.bmp out.bmp
```
que toma la imagen en ```images/yard.bmp``` y genera una nueva imagen llamada ```out.bmp``` después de ejecutar los píxeles a través de la función de ```escala de grises```. Sin embargo, la ```escala de grises``` aún no hace nada, por lo que la imagen de salida debería verse igual que el jardín original.

## Especificaciones
Implemente las funciones en ```helpers.c``` de modo que un usuario pueda aplicar filtros de detección de bordes, reflexión, desenfoque o escala de grises a sus imágenes.

- La función de ```escala de grises``` debe tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
- La función de ```reflexión``` debería tomar una imagen y reflejarla horizontalmente.
- La función de ```desenfoque``` debería tomar una imagen y convertirla en una versión borrosa de la misma imagen.
- La función de ```bordes``` debe tomar una imagen y resaltar los bordes entre los objetos, según el operador de Sobel.

No debe modificar ninguna de las firmas de función, ni debe modificar ningún otro archivo que no sea ```helpers.c```.

## Uso
Su programa debe comportarse según los ejemplos a continuación. ```INFILE.bmp``` es el nombre de la imagen de entrada y ```OUTFILE.bmp``` es el nombre de la imagen resultante después de aplicar un filtro.
```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -e INFILE.bmp OUTFILE.bmp
```

## Pistas
Los valores de los componentes ```rgbtRed```, ```rgbtGreen``` y ```rgbtBlue``` de un píxel son todos enteros, así que asegúrese de redondear los números de punto flotante al entero más cercano cuando los asigne a un valor de píxel.

## Pruebas
¡Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra provistos!

Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/filter/more
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 helpers.c
```

## Cómo enviar
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/problems/2022/x/filter/more
```
