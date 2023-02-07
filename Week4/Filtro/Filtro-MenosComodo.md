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

#### Sepia
La mayoría de los programas de edición de imágenes admiten un filtro "sepia", que le da a las imágenes una sensación de antaño al hacer que toda la imagen se vea un poco marrón rojiza.

Una imagen se puede convertir a sepia tomando cada píxel y calculando nuevos valores de rojo, verde y azul en función de los valores originales de los tres.

Hay una serie de algoritmos para convertir una imagen a sepia, pero para este problema, le pediremos que utilice el siguiente algoritmo. Para cada píxel, los valores de color sepia deben calcularse en función de los valores de color originales según se indica a continuación; donde Red es rojo, Green es verde y Blue es Azul.
```
  sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
  sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
  sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
```
Por supuesto, el resultado de cada una de estas fórmulas puede no ser un número entero, pero cada valor se puede redondear al número entero más cercano. También es posible que el resultado de la fórmula sea un número superior a 255, el valor máximo para un valor de color de 8 bits. En ese caso, los valores de rojo, verde y azul deben tener un tope de 255. Como resultado, podemos garantizar que los valores resultantes de rojo, verde y azul serán números enteros entre 0 y 255, inclusive.

#### Reflexión
Algunos filtros también pueden mover píxeles. Reflejar una imagen, por ejemplo, es un filtro donde la imagen resultante es la que obtendría al colocar la imagen original frente a un espejo. Entonces, cualquier píxel en el lado izquierdo de la imagen debería terminar en el derecho, y viceversa.

Tenga en cuenta que todos los píxeles de la imagen original aún estarán presentes en la imagen reflejada, solo que esos píxeles pueden haberse reorganizado para estar en un lugar diferente en la imagen.

#### Difuminar
Hay varias formas de crear el efecto de difuminar o suavizar una imagen. Para este problema, usaremos el "desenfoque de cuadro", que funciona tomando cada píxel y, para cada valor de color, dándole un nuevo valor promediando los valores de color de los píxeles vecinos.

Considere la siguiente cuadrícula de píxeles, donde hemos numerado cada píxel.

<img src="https://cs50.harvard.edu/x/2022/psets/4/filter/less/grid.png" width="300" height="300" />

El nuevo valor de cada píxel sería el promedio de los valores de todos los píxeles que están dentro de 1 fila y columna del píxel original (formando un cuadro de 3x3). Por ejemplo, cada uno de los valores de color para el píxel 6 se obtendría promediando los valores de color originales de los píxeles 1, 2, 3, 5, 6, 7, 9, 10 y 11 (tenga en cuenta que el píxel 6 en sí está incluido en el promedio). Asimismo, los valores de color para el píxel 11 se obtendrían promediando los valores de color de los píxeles 6, 7, 8, 10, 11, 12, 14, 15 y 16.

Para un píxel a lo largo del borde o la esquina, como el píxel 15, aún buscaríamos todos los píxeles dentro de 1 fila y columna: en este caso, los píxeles 10, 11, 12, 14, 15 y 16.

## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io/), haga clic en la ventana de su terminal y ejecute ```cd```. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente:
```
$
```
A continuación ejecute
```
wget https://cdn.cs50.net/2021/fall/psets/4/filter-less.zip
```
para descargar un ZIP llamado ```filter-less.zip``` a su espacio de códigos.

Luego ejecute
```
unzip filter-less.zip
```
para crear una carpeta llamada ```filter-less```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm filter-less.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba
```
cd filter-less
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
filter-less/ $
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

Primero, observe la definición de ```filters``` en la línea 10. Esa cadena le dice al programa cuáles son los argumentos de línea de comandos permitidos para el programa: ```b```, ```g```, ```r``` y ```s```. Cada uno de ellos especifica un filtro diferente que podemos aplicar a nuestras imágenes: desenfoque, escala de grises, reflejo y sepia.

Las siguientes líneas abren un archivo de imagen, se aseguran de que sea un archivo BMP y leen toda la información de píxeles en una matriz 2D llamada ```image```.

Desplácese hacia abajo hasta la declaración ```switch``` que comienza en la línea 101. Observe que, dependiendo del ```filter``` que hayamos elegido, se llama a una función diferente: si el usuario elige el filtro ```b```, el programa llama a la función ```blur``` (desenfoque); si es ```g```, entonces se llama a ```grayscale``` (escala de grises); si es ```r```, entonces se llama a ```reflect``` (reflejo); y si es ```s```, entonces se llama a ```sepia```. Observe también que cada una de estas funciones toma como argumentos la altura de la imagen, el ancho de la imagen y la matriz 2D de píxeles.

Estas son las funciones que (¡pronto!) implementará. Como puede imaginar, el objetivo es que cada una de estas funciones edite la matriz 2D de píxeles de tal manera que se aplique el filtro deseado a la imagen.

Las líneas restantes del programa toman el resultado ```image``` y las escriben en un nuevo archivo de imagen.

### ```helpers.h```
A continuación, eche un vistazo a ```helpers.h```. Este archivo es bastante corto y solo proporciona los prototipos de funciones para las funciones que vio anteriormente.

Aquí, tome nota del hecho de que cada función toma una matriz 2D llamada ```image``` como argumento, donde ```image``` es una matriz de ```height``` muchas filas, y cada fila es en sí misma otra matriz de ```width``` muchas ```RGBTRIPLE```s. Si ```image``` representa la imagen completa, entonces ```image[0]``` representa la primera fila e ```image[0][0]``` representa el píxel en la esquina superior izquierda de la imagen.

### ```helpers.c```
Ahora, abra ```helpers.c```. Aquí es donde pertenece la implementación de las funciones declaradas en ```helpers.h```. ¡Pero tenga en cuenta que, en este momento, faltan las implementaciones! Esta parte depende de ti.

### ```Makefile```
Finalmente, veamos ```Makefile```. Este archivo especifica lo que debería suceder cuando ejecutamos un comando de terminal como ```make filter```. Mientras que los programas que puede haber escrito antes estaban limitados a un solo archivo, ```filter``` parece que usa varios archivos: ```filter.c```, ```bmp.h```, ```helpers.h``` y ```helpers.c```. Así que necesitaremos decir ```make``` cómo compilar este archivo.

Intente compilar ```filter``` usted mismo yendo a su terminal y ejecutando
```
$ make filter
```
Luego, puede ejecutar el programa ejecutando:
```
$ ./filter -g images/yard.bmp out.bmp
```
que toma la imagen en ```images/yard.bmp``` y genera una nueva imagen llamada ```out.bmp``` después de ejecutar los píxeles a través de la función ```grayscale```. Sin embargo, todavía no hace nada, por lo que la imagen de salida debería tener el mismo aspecto que la original.

## Especificación
Implemente las funciones de ```helpers.c``` de manera que un usuario pueda aplicar filtros de escala de grises, sepia, reflejo o desenfoque a sus imágenes.
- La función ```grayscale``` debería tomar una imagen y convertirla en una versión en blanco y negro de la misma imagen.
- La función ```sepia``` debería tomar una imagen y convertirla en una versión sepia de la misma imagen.
- La función ```reflect``` debe tomar una imagen y reflejarla horizontalmente.
- Finalmente, la función ```blur``` debería tomar una imagen y convertirla en una versión borrosa de la misma imagen.
No debe modificar ninguna de las firmas de función, ni debe modificar ningún otro archivo que no sea ```helpers.c```.

## Tutorial
**Tenga en cuenta que hay 5 videos en esta lista de reproducción.**

## Uso
Su programa debe comportarse según los ejemplos a continuación. ```INFILE.bmp``` es el nombre de la imagen de entrada y ```OUTFILE.bmp``` es el nombre de la imagen resultante después de aplicar un filtro.
```
$ ./filter -g INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -s INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -r INFILE.bmp OUTFILE.bmp
```
```
$ ./filter -b INFILE.bmp OUTFILE.bmp
```

## Sugerencias
- Los valores de los componentes ```rgbtRed```, ```rgbtGreen``` y ```rgbtBlue``` son todos enteros, así que asegúrese de redondear cualquier número de punto flotante al entero más cercano cuando los asigne a un valor de píxel.
- Al implementar la función ```grayscale```, deberá promediar los valores de 3 enteros. ¿Por qué querría dividir la suma de estos enteros por 3.0 y no por 3?
- En la función ```reflect```, deberá intercambiar los valores de los píxeles en los lados opuestos de una fila. Recuerde de la lección cómo implementamos el intercambio de dos valores con una variable temporal. ¡No es necesario usar una función separada para intercambiar a menos que lo desee!
- ¿Cómo podría ser útil una función que devuelve el menor de dos enteros al implementar ```sepia```, particularmente cuando necesita asegurarse de que el valor de un color no sea superior a 255?
- Al implementar la función ```blur```, es posible que el desenfoque un píxel termine afectando el desenfoque de otro píxel. ¿Quizás cree una copia de ```image``` (el tercer argumento de la función) declarando una nueva matriz (bidimensional) con código similar a ```RGBTRIPLE copy[height][width]```;y copiándola ```image``` en ```copy```, píxel por píxel, con bucles ```for``` anidados? Y luego lea los colores de los píxeles de ```copy``` pero escriba (es decir, cambie) los colores de los píxeles en ```image```?

## Pruebas
¡Asegúrese de probar todos sus filtros en los archivos de mapa de bits de muestra provistos!

Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/filter/less
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 helpers.c
```
## Cómo enviar
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/problems/2022/x/filter/less
```
