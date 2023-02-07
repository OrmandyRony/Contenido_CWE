# Mario
## Empezando

Abra el código VS.

Comience haciendo clic dentro de la ventana de su terminal, luego ejecutecd  por sí mismo. Debería encontrar que su "indicador" se parece al siguiente.

```
$
```

Haga clic dentro de esa ventana de terminal y luego ejecute

```
wget https://cdn.cs50.net/2021/fall/psets/1/mario-less.zip 
```

Seguido de Enter para descargar un ZIP llamado mario-less.zip en su espacio de código. ¡Tenga cuidado de no pasar por alto el espacio entre wget y la siguiente URL, o cualquier otro carácter para el caso!

Ahora ejecuta

```
descomprimir mario-less.zip
```

Para crear una carpeta llamada mario-less. Ya no necesita el archivo ZIP, por lo que puede ejecutar

```
rm mario-less.zip
```

y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba

```
cd mario-less
```

Seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.

```
mario-less/ $
```

Si todo fue exitoso, debe ejecutar

```
ls
```

y ver un archivo llamado `mario.c` . Ejecutar el código mario.c debería abrir el archivo donde escribirá su código para este conjunto de problemas. De lo contrario, vuelva sobre sus pasos y vea si puede determinar dónde se equivocó.

# World 1-1
Hacia el final del Mundo 1-1 en Super Mario Brothers de Nintendo, Mario debe ascender una pirámide de bloques alineados a la derecha, como se muestra a continuación.

![mario](mario.png)

Recreemos esa pirámide en C, aunque en texto, usando hash (#) para los ladrillos, como se muestra a continuación. Cada hash es un poco más alto que ancho, por lo que la pirámide en sí también será más alta que ancha.

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

El programa que escribiremos se llamará mario. Y permitamos que el usuario decida qué tan alta debe ser la pirámide solicitándole primero un número entero positivo entre, digamos, 1 y 8, inclusive.

Así es como podría funcionar el programa si el usuario ingresa 8 cuando se le solicite:

```
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```
Así es como podría funcionar el programa si el usuario ingresa 4 cuando se le solicite:

```
$ ./mario
Height: 4
   #
  ##
 ###
####
```

Así es como podría funcionar el programa si el usuario ingresa 2 cuando se le solicite:

```
$ ./mario
Height: 2
 #
##
```

Y así es como podría funcionar el programa si el usuario ingresa 1 cuando se le solicite:

```
$ ./mario
Height: 1
#
```
Si el usuario, de hecho, no ingresa un número entero positivo entre 1 y 8, inclusive, cuando se le solicite, el programa debería volver a preguntarle al usuario hasta que coopere:

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```
¿Cómo empezar? Abordemos este problema paso a paso.

# Tutorial

[![Alt text](https://img.youtube.com/vi/dF7wNjsRBjI/0.jpg)](https://www.youtube.com/watch?v=NAs4FIWkJ4s)

# Pseudocódigo
Primero, ejecuta

```
cd
```
para asegurarse de que está en el directorio predeterminado de su espacio de códigos.

Luego, ejecuta

```
cd mario-less
```
para cambiar a su directorio `mario-less`.

Luego, ejecuta

```
code pseudocode.txt
```
Para abrir el archivo llamado `pseudocode.txt` dentro de ese directorio.

Escriba en `pseudocode.txt` algún pseudocódigo que implemente este programa, incluso si no (¡todavía!) está seguro de cómo escribirlo en código. No existe una forma correcta de escribir pseudocódigo, pero basta con oraciones breves en inglés. Recuerde cómo escribimos un pseudocódigo para encontrar a alguien en una guía telefónica. Lo más probable es que su pseudocódigo use (¡o implique usar!) una o más funciones, condicionales, expresiones booleanas, bucles y/o variables.

### __Spoiler__

Hay más de una manera de hacer esto, ¡así que aquí hay solo una!

1. Solicitar al usuario la altura

2. Si la altura es menor que 1 o mayor que 8 (o no es un número entero), retroceda un paso

3. Iterar desde 1 hasta la altura:
    1. En la iteración i, imprima i hashes y luego una nueva línea

Está bien editar el suyo después de ver este pseudocódigo aquí, ¡pero no copie/pegue el nuestro en el suyo!

## Solicitud de entrada

Cualquiera que sea su pseudocódigo, primero escribamos solo el código C que solicita (y vuelve a solicitar, según sea necesario) al usuario para que ingrese. Abra el archivo llamado `mario.c` dentro de su directorio de `mario`. (¿Recuerdas cómo?)

Ahora, modifique `mario.c` de tal manera que solicite al usuario la altura de la pirámide, almacenando su entrada en una variable, volviendo a preguntar al usuario una y otra vez según sea necesario si su entrada no es un número entero positivo entre 1 y 8, inclusivo. Luego, simplemente imprima el valor de esa variable, confirmando así (usted mismo) que efectivamente almacenó la entrada del usuario con éxito, como se muestra a continuación.
```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
Stored: 4
```
### __Sugerencias__

- Recuerda que puedes compilar tu programa con make.
- Recuerde que puede imprimir un int con printf usando %i.
- Recuerde que puede obtener un número entero del usuario con get_int.
- Recuerde que get_int se declara en cs50.h.
- Recuerde que solicitamos al usuario un número entero positivo en la clase usando un ciclo do while en `mario.c`.

# Construyendo lo contrario

Ahora que su programa está (¡con suerte!) aceptando entradas según lo prescrito, es hora de dar otro paso.

Resulta que es un poco más fácil construir una pirámide alineada a la izquierda que a la derecha, como se muestra a continuación.

```
#
##
###
####
#####
######
#######
########
```
Así que primero construyamos una pirámide alineada a la izquierda y luego, una vez que funcione, ¡alinéala a la derecha!

Modifique `mario.c` a la derecha para que ya no imprima simplemente la entrada del usuario, sino que imprima una pirámide alineada a la izquierda de esa altura.

### __Sugerencias__

- Tenga en cuenta que un hash es solo un carácter como cualquier otro, por lo que puede imprimirlo con `printf`.
- Así como Scratch tiene un bloque de repetición, C tiene un bucle for, a través del cual puede iterar varias veces. ¿Quizás en cada iteración, podría imprimir tantos hashes?
- De hecho, puede "anidar" bucles, iterando con una variable (p. ej., i) en el bucle "externo" y otra (p. ej., j) en el bucle "interno". Por ejemplo, así es como puede imprimir un cuadrado de alto y ancho n, a continuación. ¡Por supuesto, no es un cuadrado lo que quieres imprimir!

```
  for (int i = 0; i < n; i++)
  {
      for (int j = 0; j < n; j++)
      {
          printf("#");
      }
      printf("\n");
  }
```

# Alinear a la derecha con puntos

Ahora alineemos a la derecha esa pirámide empujando sus hashes hacia la derecha prefijándolos con puntos (es decir, puntos), como se muestra a continuación.

¡Modifique `mario.c` de tal manera que haga exactamente eso!
```
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

## Cómo probar su código
¿Funciona su código según lo prescrito cuando ingresa

- `-1` (u otros números negativos)?
- `-0`?
- `1` del al `8`?
- `9` u otros números positivos?
- letras o palabras?
- ninguna entrada en absoluto, cuando solo presiona Enter?

## Quitar los puntos

¡Todo lo que queda ahora es una floritura final! ¡Modifique mario.c de tal manera que imprima espacios en lugar de esos puntos!

## Cómo probar su código

Ejecute lo siguiente para evaluar la corrección de su código usando check50. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

```
check50 cs50/problems/2022/x/mario/less
```

Ejecute lo siguiente para evaluar el estilo de su código usando style50.
```
style50 mario.c
```
### __Insinuación__
¡Un espacio es solo presionar la barra espaciadora, al igual que un punto es solo presionar su tecla! ¡Solo recuerde que printf requiere que rodee ambos con comillas dobles!


## Cómo enviar
En su terminal, ejecute lo siguiente para enviar su trabajo.

```
submit50 cs50/problems/2022/x/mario/less
```



<!--```t```-->


