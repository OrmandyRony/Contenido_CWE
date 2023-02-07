## Píxeles
- La semana pasada echamos un vistazo a la memoria y cómo podíamos usar arreglos para almacenar datos.
- Podríamos acercarnos más y más en una imagen, pero muy pronto veremos píxeles individuales, como los del ojo de esta marioneta:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/eyes.png" width="500" height="300" />
  
  - Dado que esta imagen se almacena con un número finito de bytes, cada uno de los cuales puede representar un valor rojo, verde o azul para cada píxel, a su vez hay un número finito de píxeles que podemos ver.
- Una imagen más simple de una cara sonriente podría representarse con un solo bit por píxel:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/smiley.png" width="600" height="300" />
- Podemos visitar [cs50.ly/art](cs50.ly/art) con una cuenta de Google para hacer una copia de una hoja de cálculo, que luego podemos llenar con colores para crear nuestro propio [pixel art](https://es.wikipedia.org/wiki/Pixel_art).
- [Adobe Photoshop](https://es.wikipedia.org/wiki/Adobe_Photoshop), un popular software de edición de imágenes, incluye un selector de color que se ve así:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/color_picker.png" width="450" height="300" />
  
  - Aquí se selecciona el color negro y vemos que los valores para R, G y B, o rojo, verde y azul respectivamente, son todos 0. Además, vemos otro valor, #000000 que parece representar los tres valores para el color negro.
- Echemos un vistazo a algunos colores más:
  - blanco, con R: 255, G: 255 y B: 255, y #FFFFFF
  - rojo, con R: 255, G: 0 y B: 0, y #FF0000
  - verde, con R: 0, G: 255 y B: 0 y #00FF00
  - azul, con R: 0, G: 0 y B: 255 y #0000FF

## Hexadecimal
- Podríamos notar un patrón para la nueva notación, donde parece que cada valor de rojo, verde y azul se representa con dos caracteres. Resulta que hay otro sistema base, hexadecimal o base-16, donde hay 16 dígitos:
  ```
  0 1 2 3 4 5 6 7 8 9 A B C D E F
  ```
  - Los dígitos comienzan con 0 hasta 9, y continúan con A hasta F como equivalentes a los valores decimales de 10 a 15.
- Consideremos un número hexadecimal de dos dígitos:
    ```
    16^1 16^0
       0    0
    ```
    - Aquí, el ```0``` en el lugar de las unidades (ya que $16^0=1$) tiene un valor decimal de 0. Contaremos hacia arriba y después de ```09``` usaremos ```0A``` para representar 10 en decimal.
    - Podemos seguir contando hasta ```0F```, que equivale a 15 en decimal.
- Después de ```0F```, tenemos que llevar el uno, ya que iríamos del 9 al 10 en decimal:
  ```
  16^1 16^0
     1    0
  ```
  - Aquí, el ```1``` tiene un valor de $16^1\times1=16$, entonces ```10``` en hexadecimal es 16 en decimal.
- Con dos dígitos, podemos tener un valor máximo de ```FF```, o $16^1\times15+16^0\times15=16\times15+1\times15=240+15=255$.
  - Los valores en la memoria de una computadora todavía se almacenan como binarios, pero esta forma de representación nos ayuda a los humanos a representar valores numéricos más grandes con menos dígitos necesarios.
  - Con 8 bits en binario, el valor más alto que podemos contar también es 255, con ```11111111```. Entonces, dos dígitos en hexadecimal pueden representar convenientemente el valor de un byte en binario. (Cada dígito en hexadecimal, con 16 valores, se asigna a cuatro bits en binario).

## Direcciones, punteros
- Para la memoria de nuestra computadora, también veremos que se usa el hexadecimal para describir cada dirección o ubicación:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/addresses.png" width="600" height="350" />
  
  - Al escribir ```0x``` delante de un valor hexadecimal, podemos distinguirlos de los valores decimales.
- Podríamos crear un valor ```n``` e imprimirlo:
  ```C
  #include <stdio.h>

  int main(void)
  {
      int n = 50;
      printf("%i\n", n);
  }
  ```
- En la memoria de nuestra computadora, ahora hay 4 bytes en algún lugar que tienen el valor binario de 50, con algún valor para su dirección, como ```0x123```:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/50.png" width="600" height="350" />
- Un **puntero** es una variable que almacena una dirección en la memoria, donde se podría almacenar alguna otra variable.
- El operador **```&```** se puede usar para obtener la dirección de alguna variable, como con ```&n```. Y el operador ```*``` declara una variable como puntero, como con ```int *p```, indicando que tenemos una variable llamada ```p``` que *apunta a* un ```int```. Entonces, para almacenar la dirección de una variable ```n``` en un puntero ```p```, escribiríamos:
  ```C
  int *p = &n;
  ```
- En C podemos ver la dirección con el operador ```&```, lo que significa "obtener la dirección de esta variable":
  ```C
  #include <stdio.h>
  
  int main(void)
  {
      int n = 50;
      int *p = &n;
      printf("%p\n", p);
  }
  ```
  
  ```
  $ make address
  $ ./address
  0x7ffcb4578e5c
  ```
  - ```%p``` es el código de formato para imprimir una dirección con ```printf```. Y solo necesitamos usar el nombre de la variable ```p```, después de haberla declarado.
  - En nuestra instancia de VS Code, vemos una dirección con un valor grande como ```0x7ffcb4578e5c```. El valor de la dirección en sí mismo no es significativo, ya que es solo una ubicación en la memoria en la que se almacena la variable; en cambio, la idea importante es que podemos *usar* esta dirección más adelante.
  - Podemos ejecutar este programa varias veces y ver que la dirección ```n``` en la memoria cambia, ya que diferentes direcciones en la memoria estarán disponibles en diferentes momentos.
- Con C también podemos ir a direcciones específicas en la memoria, lo que podría causar **fallas de segmentación**, donde hemos tratado de leer o escribir en la memoria para lo que no tenemos permiso.
- El operador ```*``` también es el operador de desreferencia, que va a una dirección para obtener el valor almacenado allí. Por ejemplo, podemos decir:
  ```C
  #include <stdio.h>

  int main(void)
  {
      int n = 50;
      int *p = &n;
      printf("%p\n", p);
      printf("%i\n", *p);
  }
  ```
  
  ```
  $ ./address
  0x7ffda0a4767c
  50
  ```
  - Ahora, vemos el valor del puntero en sí (una dirección), y luego el valor en la dirección con ```*p```, que es ```50```.
  - Dado que declaramos ```p``` para ser un ```int *```, el compilador sabe que ```*p``` es un ```int```, por lo que se lee el número correcto de bytes.
- En la memoria, podríamos tener una variable, ```p```, con el valor de alguna dirección, como ```0x123```, almacenada, y otra variable, un número entero con el valor ```50```, en esas direcciones:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/p.png" width="600" height="350" />
  - Tenga en cuenta que ```p``` ocupa 8 bytes, ya que en los sistemas informáticos modernos se utilizan 64 bits para gestionar los miles de millones de bytes de memoria disponibles. Con 32 bits, solo podemos contar hasta unos 4 mil millones de bytes, o unos 4 GB de memoria.
- Podemos abstraer el valor real de las direcciones, ya que serán diferentes a medida que declaremos variables en nuestros programas. Simplemente podemos pensar en ```p``` como puntero a algún valor en la memoria:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/pointing.png" width="600" height="250" />
- En el mundo real, podríamos tener un buzón con la etiqueta "p", entre muchos buzones con direcciones. Dentro de nuestro buzón, podemos poner un valor como ```0x123```, que es la dirección de algún otro buzón que tiene la etiqueta "n".

## Cadenas
- Podemos declarar una cadena con ```string s = "HI!";```, que se almacenará un carácter a la vez en la memoria. Y podemos acceder a cada carácter con ```s[0]```, ```s[1]```, ```s[2]``` y ```s[3]```:
  
  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_array.png" width="200" height="50" />
- Pero resulta que cada carácter, dado que está almacenado en la memoria, *también* tiene una dirección única, y ```s``` en realidad es solo un puntero con la dirección del primer carácter:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_pointer.png" width="400" height="150" />
  - ```s``` es una variable de tipo ```string```, que es un puntero a un carácter.
  - Recuerde que podemos leer la cadena completa comenzando en la dirección en ```s```, y continuar leyendo un carácter a la vez desde la memoria hasta llegar a ```\0```.
- Resulta que ```string s = "HI!"``` es lo mismo que ```char *s = "HI!";```. Y podemos usar cadenas en C exactamente de la misma manera sin la Biblioteca CS50, usando ```char *```.
- Imprimamos una cadena:
  ```C
  #include <cs50.h>
  #include <stdio.h>
  
  int main(void)
  {
      string s = "HI!";
      printf("%s\n", s);
  }
  ```
  
  ```
  $ make address
  $ ./address
  HI!
  ```
- Ahora, podemos eliminar la biblioteca CS50 y decir:
  ```C
  #include <stdio.h>
  
  int main(void)
  {
      string s = "HI!";
      printf("%s\n", s);
  }
  ```
  
  ```
  $ make address
  $ ./address
  HI!
  ```
  
- Podemos experimentar y ver la dirección de los carácteres:
  ```C
  #include <cs50.h>
  #include <stdio.h>

  int main(void)
  {
     string s = "HI!";
     char c = s[0];
     char *p = &c;
     printf("%p\n", s);
     printf("%p\n", p);
  }
  ```
  
  ```
  $ make address
  $ ./address
  0x402004
  0x7ffd4227fdd7
  ```
  - Almacenamos el primer carácter de ```s``` en ```c```, e imprimimos su dirección con ```p```. También imprimimos ```s``` como una dirección con ```%p```, y vemos que los valores son diferentes ya que hicimos una copia del primer carácter con ```char c = s[0];```.
- Ahora, imprimiremos la dirección del primer carácter en ```s```:
  ```C
  #include <cs50.h>
  #include <stdio.h>

  int main(void)
  {
     string s = "HI!";
     char *p = &s[0];
     printf("%p\n", p);
     printf("%p\n", s);
  }
  ```
  
  ```
  $ make address
  $ ./address
  0x402004
  0x402004
  ```
  - Con ```char *p = &s[0];```, almacenamos la dirección del primer carácter de ```s``` en un puntero llamado ```p```. Y ahora, cuando imprimimos ```p``` y ```s``` como direcciones, vemos el mismo valor.
- Podemos ver la dirección de cada carácter en ```s```:
  ```C
  #include <stdio.h>

  int main(void)
  {
      char *s = "HI!";
      printf("%p\n", s);
      printf("%p\n", &s[0]);
      printf("%p\n", &s[1]);
      printf("%p\n", &s[2]);
      printf("%p\n", &s[3]);
  }
  ```
  
  ```
  $ make address
  $ ./address
  0x402004
  0x402004
  0x402005
  0x402006
  0x402007
  ```
  - De nuevo, la dirección del primer carácter, ```&s[0]```, es el mismo que el valor de ```s```. Y cada carácter siguiente tiene una dirección que es un byte superior.
- En la biblioteca CS50, una cadena se define con solo ```typedef char *string;```. Con ```typedef```, estamos creando un tipo de datos personalizado para la palabra ```string```, haciéndolo equivalente a ```char *```.

## Aritmética de punteros
- Podemos imprimir cada carácter en una cadena:
  ```C
  #include <cs50.h>
  #include <stdio.h>

  int main(void)
  {
      string s = "HI!";
      printf("%c\n", s[0]);
      printf("%c\n", s[1]);
      printf("%c\n", s[2]);
      printf("%c\n", s[3]);
  }
  ```
  
  ```
  $ make address
  $ ./address
  H
  I
  !
  
  $
  ```
  - Cuando declaramos un ```string``` con comillas dobles ```"```, el compilador determina dónde colocar esos caracteres en la memoria como una matriz.
- Simplifiquemos nuestro código para usar ```char *``` y mostrar solo los caracteres imprimibles:
  ```C
  #include <stdio.h>

  int main(void)
  {
      char *s = "HI!";
      printf("%c\n", s[0]);
      printf("%c\n", s[1]);
      printf("%c\n", s[2]);
  }
  ```
  
  ```
  $ make address
  $ ./address
  H
  I
  !
  ```
- Pero podemos ir directamente a las direcciones:
  ```C
  #include <stdio.h>

  int main(void)
  {
      char *s = "HI!";
      printf("%c\n", *s);
      printf("%c\n", *(s + 1));
      printf("%c\n", *(s + 2));
  }
  ```
  - ```*s``` va a la dirección almacenada en ```s``` y ```*(s + 1)``` va a la ubicación en la memoria con el siguiente carácter, una dirección que está un byte más arriba.
  - ```s[1]``` es **azúcar sintáctico**, como una abstracción de ```*(s + 1)```, equivalente en función pero más amigable para leer y escribir.
- La **aritmética de punteros** es el proceso de aplicar operaciones matemáticas a los punteros, usándolos como números (que lo son).
- Podemos declarar una matriz de números y acceder a ellos con aritmética de punteros:
  ```C
  #include <stdio.h>

  int main(void)
  {
      int numbers[] = {4, 6, 8, 2, 7, 5, 0};
  
      printf("%i\n", *numbers);
      printf("%i\n", *(numbers + 1));
      printf("%i\n", *(numbers + 2));
      printf("%i\n", *(numbers + 3));
      printf("%i\n", *(numbers + 4));
      printf("%i\n", *(numbers + 5));
      printf("%i\n", *(numbers + 6));
  }
  ```
  
  ```
  $ make address
  $ ./address
  4
  6
  8
  2
  7
  5
  0
  ```
  - Resulta que solo necesitamos agregar ```1``` a la dirección de ```numbers```, en lugar de ```4``` (aunque los ```int```s tienen un tamaño de 4 bytes), ya que el compilador ya sabe que el tipo de cada valor en ```numbers``` es de 4 bytes. Con ```+ 1```, le estamos diciendo al compilador que se mueva al siguiente valor en la matriz, no al siguiente byte.
  - Y observe que ```numbers``` es una matriz, pero podemos usarla como un puntero con ```*numbers```.

## Comparar y copiar
- Intentemos comparar dos enteros del usuario:
  ```C
  #include <cs50.h>
  #include <stdio.h>
  
  int main(void)
  {
      int i = get_int("i: ");
      int j = get_int("j: ");
  
      if (i == j)
      {
          printf("Igual\n");
      }
      else
      {
          printf("Diferente\n");
      }
  }
  ```
  
  ```
  $ make compare
  $ ./compare
  i: 50
  j: 50
  Igual
  $ ./compare
  i: 50
  j: 42
  Diferente
  ```
  - Compilamos y ejecutamos nuestro programa, y funciona como esperábamos, con los mismos valores de los dos enteros dándonos "Igual" y diferentes valores "Diferente".
- Cuando tratamos de comparar dos cadenas, vemos que las mismas entradas hacen que nuestro programa imprima "Diferente":
  ```C
  #include <cs50.h>
  #include <stdio.h>

  int main(void)
  {
      char *s = get_string("s: ");
      char *t = get_string("t: ");

      if (s == t)
      {
          printf("Igual\n");
      }
      else
      {
          printf("Diferente\n");
      }
  }
  ```
  
  ```
  $ make compare
  $ ./compare
  s: HI!
  t: BYE!
  Diferente
  $ ./compare
  s: HI!
  t: HI!
  Diferente
  ```
  - Incluso cuando nuestras entradas son las mismas, vemos impreso "Diferente".
  - Cada "cadena" es un puntero, ```char *```, a una ubicación diferente en la memoria, donde se almacena el primer carácter de cada cadena. Entonces, incluso si los caracteres en la cadena son los mismos, esto siempre imprimirá "Diferente".
- Y ```get_string```, todo este tiempo, ha estado devolviendo solo un ```char *```, o un puntero al primer carácter de una cadena del usuario. Como llamamos ```get_string``` dos veces, obtuvimos dos punteros diferentes.
- Podemos arreglar nuestro programa con:
  ```C
  #include <cs50.h>
  #include <stdio.h>
  #include <string.h>

  int main(void)
  {
      char *s = get_string("s: ");
      char *t = get_string("t: ");

      if (strcmp(s, t) == 0)
      {
          printf("Igual\n");
      }
      else
      {
          printf("Diferente\n");
      }
  }
  ```
  
  ```
  $ make compare
  $ ./compare
  s: HI!
  t: HI!
  Igual
  ```
- Echaremos un vistazo a los valores de ```s``` y ```t``` como punteros:
  ```C
  #include <cs50.h>
  #include <stdio.h>

  int main(void)
  {
      char *s = get_string("s: ");
      char *t = get_string("t: ");

      printf("%p\n", s);
      printf("%p\n", t);
  }
  ```
  
  ```
  $ make compare
  $ ./compare
  s: HI!
  t: HI!
  0x19e06b0
  0x19e06f0
  ```
  - Vemos que las direcciones de nuestras dos cadenas son de hecho diferentes.
- Visualicemos cómo se vería esto en la memoria de nuestra computadora. Nuestra primera cadena podría estar en la dirección 0x123, la segunda podría estar en 0x456 y ```s``` tendrá el valor de ```0x123```, apuntando a esa ubicación, y ```t``` tendrá el valor de ```0x456```, apuntando a otra ubicación:
  
  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_t.png" width="600" height="350" />
  
  - Dado que nuestra computadora coloca cada cadena en algún lugar de la memoria para nosotros, necesitamos ```s``` y ```t``` apuntar a cada una de ellas. Y ahora vemos por qué comparar ```s``` y ```t``` directamente siempre imprimirá "Diferente". ```strcmp```, en cambio, irá a cada cadena y las comparará carácter por carácter.
- En C, también podemos obtener la dirección de ```s``` o ```t```, y almacenarlos en una variable del tipo ```char **```, un puntero a un puntero.
- Intentemos copiar una cadena:
  ```C
  #include <cs50.h>
  #include <ctype.h>
  #include <stdio.h>
  #include <string.h>

  int main(void)
  {
      string s = get_string("s: ");

      string t = s;
  
      t[0] = toupper(t[0]);
  
      printf("s: %s\n", s);
      printf("t: %s\n", t);
  }
  ```
  
  ```
  $ make copy
  $ ./copy
  s: hi!
  s: Hi!
  t: Hi!
  ```
  - Obtenemos una cadena ```s``` y copiamos el valor de ```s``` en ```t```. Luego, ponemos en mayúscula la primera letra de ```t```.
  - Pero cuando ejecutamos nuestro programa, vemos que ambos ```s``` y ```t``` ahora están en mayúscula.
- Dado que configuramos ```s``` y ```t``` con el mismo valor, o la misma dirección, ambos apuntan al mismo carácter, por lo que escribimos en mayúscula el mismo carácter en la memoria:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_t_copy.png" width="600" height="350" />
  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_t_pointing.png" width="600" height="300" />
  
## Asignación de memoria
- Para hacer realmente una copia de una cadena, tenemos que hacer un poco más de trabajo y copiar cada carácter en salgún otro lugar de la memoria.
- Tendremos que usar una nueva función, **```malloc```**, para *asignar* una cierta cantidad de bytes en la memoria. Y usaremos **```free```** para marcar la memoria como usable cuando hayamos terminado con ella, para que el sistema operativo pueda hacer algo más con ella.
  - Nuestras computadoras pueden ralentizarse si un programa que estamos ejecutando tiene un error en el que asigna más y más memoria pero nunca la libera. El sistema operativo tardará cada vez más en encontrar suficiente memoria disponible para nuestro programa.
- Copiemos una cadena ahora:
  ```C
  #include <cs50.h>
  #include <ctype.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main(void)
  {
      char *s = get_string("s: ");
  
      char *t = malloc(strlen(s) + 1);
  
      for (int i = 0, n = strlen(s) + 1; i < n; i++)
      {
          t[i] = s[i];
      }
  
      t[0] = toupper(t[0]);
  
      printf("s: %s\n", s);
      printf("t: %s\n", t);
  }
  ```
  - Creamos una nueva variable para apuntar a una nueva cadena con ```char *t```. El argumento ```malloc``` es el número de bytes que nos gustaría usar. Ya sabemos la longitud de ```s```, pero necesitamos agregar 1 para el carácter nulo de terminación.
  - Luego, copiamos cada carácter, uno a la vez, con un bucle ```for```. Usamos ```strlen(s) + 1``` ya que queremos copiar el carácter nulo también para finalizar la cadena. En el bucle, configuramos ```t[i] = s[i]```, copiando los caracteres.
- También podríamos usar una función de biblioteca ```strcpy```:
  ```C
  #include <cs50.h>
  #include <ctype.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main(void)
  {
      char *s = get_string("s: ");
  
      char *t = malloc(strlen(s) + 1);
  
      strcpy(t, s);
  
      t[0] = toupper(t[0]);
  
      printf("s: %s\n", s);
      printf("t: %s\n", t);
  
      free(t);
  }
  ```
  
  ```
  $ make copy
  $ ./copy
  s: hi!
  s: hi!
  t: Hi!
  ```
  - Ahora, podemos poner en mayúscula la primera letra de ```t```.
  - Recordaremos llamar ```free``` a ```t```, ya que lo asignamos nosotros mismos.
- Podemos agregar algunas comprobaciones de errores a nuestro programa:
  ```C
  #include <cs50.h>
  #include <ctype.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main(void)
  {
      char *s = get_string("s: ");
  
      char *t = malloc(strlen(s) + 1);
      if (t == NULL)
      {
          return 1;
      }
  
      strcpy(t, s);
  
      if (strlen(t) > 0)
      {
          t[0] = toupper(t[0]);
      }
  
      printf("s: %s\n", s);
      printf("t: %s\n", t);
  
      free(t);
  }
  ```
  - Si nuestra computadora no tiene memoria, ```malloc``` devolverá ```NULL```, el puntero nulo o un valor especial de todos los ```0``` bits que indica que no hay una dirección a la que apuntar. Entonces deberíamos verificar ese caso y salir si ```t``` es ```NULL```.
  - También deberíamos comprobar que ```t``` tiene una longitud, antes de intentar poner en mayúscula el primer carácter.
- Podemos visualizar cómo se ve esto en la memoria de nuestra computadora:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/s_t_malloc.png" width="600" height="300" />
  
  - Hemos asignado memoria en ```0x456``` y configurado ```t``` para apuntar a ella. Luego, usábamos ```strcpy``` para copiar el valor de cada carácter, comenzando desde la dirección a la que apunta ```s```, hasta la dirección a la que apunta ```t```.
