# Legibilidad
Implemente un programa que calcule el nivel de grado aproximado necesario para comprender algún texto, según se indica a continuación.
```
$ Python readability.py
Texto: ¡Felicitaciones! Hoy es tu día. ¡Te vas a Grandes Lugares! ¡Estás fuera y lejos!
Grado 3
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente:
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-readability.zip
```
para descargar un ZIP llamado ```sentimental-readability.zip``` en su espacio de código.
Luego ejecuta
```
unzip sentimental-readability.zip
```
para crear una carpeta llamada ```sentimental-readability```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-readability.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.
Ahora escribe
```
cd sentimental-readability
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-readability/ $
```
Ejecute ```ls``` por sí mismo y debería ver ```readability.py```. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.
## Especificación
* Escriba, en un archivo llamado ```readability.py```, un programa que primero le pida al usuario que escriba un texto y luego muestre el nivel de calificación del texto, de acuerdo con la fórmula de Coleman-Liau, exactamente como lo hizo en el Conjunto de problemas 2, excepto que su programa esta vez debe estar escrito en Python.
    * Recuerde que el índice de Coleman-Liau se calcula como ```0.0588 * L - 0.296 * S - 15.8```, donde ```L``` es la cantidad promedio de letras por cada 100 palabras en el texto y ```S``` es la cantidad promedio de oraciones por cada 100 palabras en el texto.
* Utilice ```get_string``` de la Biblioteca CS50 para obtener la entrada del usuario e ```imprima``` para generar su respuesta.
* Su programa debe contar la cantidad de letras, palabras y oraciones en el texto. Puede suponer que una letra es cualquier carácter en minúscula de la ```a``` a la ```z``` o cualquier carácter en mayúscula de la ```A``` a la ```Z```, cualquier secuencia de caracteres separados por espacios debe contar como una palabra y que cualquier aparición de un punto, signo de exclamación o signo de interrogación indica el final de una oración.
* Su programa debe imprimir como salida ```"Grado X"```, donde ```X``` es el nivel de grado calculado por la fórmula de Coleman-Liau, redondeado al número entero más cercano.
* Si el número de índice resultante es 16 o superior (equivalente o mayor que un nivel de lectura de pregrado superior), su programa debe generar ```"Grado 16+"``` en lugar de dar el número de índice exacto. Si el número de índice es menor que 1, su programa debería generar ```"Antes del grado 1"```.
## Uso
Su programa debe comportarse según el siguiente ejemplo.
```
$ Python readability.py
Texto: ¡Felicitaciones! Hoy es tu día. ¡Te vas a Grandes Lugares! ¡Estás fuera y lejos!
Grado 3
```
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```Un pescado. Dos pescados. Pescado rojo. pescado azul``` y presione enter. Su programa debe generar ```antes del grado 1```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escribe ```¿Te gustaría que estuvieran aquí o allá? No me gustaría que estuvieran aquí o allí. No los quisiera en ningún lado.``` y presione enter. Su programa debe generar el ```Grado 2```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```¡Felicidades! Hoy es tu día. ¡Te vas a Grandes Lugares! ¡Estás fuera y lejos!``` y presiona enter. Su programa debe generar el ```Grado 3```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```Harry Potter era un niño muy inusual en muchos sentidos. Por un lado, odiaba las vacaciones de verano más que cualquier otra época del año. Por otro lado, realmente quería hacer su tarea, pero se vio obligado a hacerlo en secreto, en la oscuridad de la noche. Y también resultó ser un mago.``` y presione enter. Su programa debe generar el ```Grado 5```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```En mis años más jóvenes y vulnerables, mi padre me dio un consejo que he estado dando vueltas en mi mente desde entonces.``` y presione enter. Su programa debe generar el ```Grado 7```.
* Ejecute su programa como ```python readability.py``` y espere un mensaje de entrada. Escriba ```Alice estaba empezando a cansarse de estar sentada junto a su hermana en el banco y de no tener nada que hacer: una o dos veces se había asomado al libro que su hermana estaba leyendo, pero no tenía imágenes ni conversaciones, "¿y de qué sirve un libro", pensó Alicia, "sin imágenes ni conversaciones?"``` y presione enter. Su programa debe generar el ```Grado 8```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```Cuando tenía casi trece años, mi hermano Jem se rompió gravemente el brazo a la altura del codo. Cuando se curó y se disiparon los temores de Jem de no poder jugar nunca al fútbol, rara vez se sentía cohibido por su lesión. Su brazo izquierdo era algo más corto que el derecho; cuando estaba de pie o caminaba, el dorso de su mano estaba en ángulo recto con su cuerpo, su pulgar paralelo a su muslo.``` y presione enter. Su programa debe generar el ```Grado 8```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```Hay más cosas en el Cielo y en la Tierra, Horatio, de las que sueña en su filosofía.``` y presione enter. Su programa debe generar el ``` Grado 9```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```Era un día brillante y frío de abril, y los relojes daban las trece. Winston Smith, con la barbilla apoyada en el pecho en un esfuerzo por escapar del vil viento, se deslizó rápidamente a través de las puertas de vidrio de Victory Mansions, aunque no lo suficientemente rápido como para evitar que un remolino de polvo arenoso entrara con él.``` y presione enter. Su programa debe generar ```Grado 10```.
* Ejecute su programa como ```python readability.py``` y espere a que se le solicite la entrada. Escriba ```una gran clase de problemas computacionales que involucran la determinación de propiedades de gráficos, dígrafos, números enteros, arreglos de números enteros, familias finitas de conjuntos finitos, fórmulas booleanas y elementos de otros dominios contables.``` y presione enter. Su programa debe generar ```Grado 16+```.

Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/sentimental/readability
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 readability.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/readability
```