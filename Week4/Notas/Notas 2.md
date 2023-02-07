## Valgrind
- Asignemos memoria para algunos enteros:

  ```C
  #include <stdio.h>
  #include <stdlib.h>

  int main(void)
  {
      int *x = malloc(3 * sizeof(int));
      x[1] = 72;
      x[2] = 73;
      x[3] = 33;
  }
  ```
  ```
  $ make memory
  $ ./memory
  $
  ```

  - Usaremos ```malloc``` para obtener suficiente memoria para 3 veces el tamaño de un ```int```, que podemos averiguar con ```sizeof```.
  - Deliberadamente cometimos un error en el que olvidamos que las matrices están indexadas en 0 y comenzamos en ```x[1]``` en su lugar. Luego, con ```x[3]```, estamos   tratando de acceder a la memoria más allá de los límites a los que tenemos acceso.
  - Tampoco liberamos la memoria que hemos asignado.
  - Cuando compilamos y ejecutamos nuestro programa, sin embargo, parece que no pasa nada. Resulta que nuestro error no fue lo suficientemente grave como para causar     una falla de segmentación esta vez, aunque podría ocurrir la próxima vez.
- ```valgrind``` es una herramienta de línea de comandos que podemos usar para ejecutar nuestro programa y ver si tiene algún problema relacionado con la memoria.
- Ejecutaremos ```valgrind ./memory``` después de compilar y veremos muchos resultados:

  ```
  $ valgrind ./memory
  ==5902== Memcheck, a memory error detector
  ==5902== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
  ==5902== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
  ==5902== Command: ./memory
  ==5902== 
  ==5902== Invalid write of size 4
  ==5902==    at 0x401162: main (memory.c:9)
  ==5902==  Address 0x4bd604c is 0 bytes after a block of size 12 alloc'd
  ==5902==    at 0x483B7F3: malloc (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
  ==5902==    by 0x401141: main (memory.c:6)
  ==5902== 
  ==5902== 
  ==5902== HEAP SUMMARY:
  ==5902==     in use at exit: 12 bytes in 1 blocks
  ==5902==   total heap usage: 1 allocs, 0 frees, 12 bytes allocated
  ==5902== 
  ==5902== 12 bytes in 1 blocks are definitely lost in loss record 1 of 1
  ==5902==    at 0x483B7F3: malloc (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
  ==5902==    by 0x401141: main (memory.c:6)
  ==5902== 
  ==5902== LEAK SUMMARY:
  ==5902==    definitely lost: 12 bytes in 1 blocks
  ==5902==    indirectly lost: 0 bytes in 0 blocks
  ==5902==      possibly lost: 0 bytes in 0 blocks
  ==5902==    still reachable: 0 bytes in 0 blocks
  ==5902==         suppressed: 0 bytes in 0 blocks
  ==5902== 
  ==5902== For lists of detected and suppressed errors, rerun with: -s
  ==5902== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
  ```
   - Veremos algunos fragmentos como ```Invalid write of size 4 at ... memory.c:9```, que nos da una pista para mirar la línea 9, donde estamos usando ```x[3]```.
 - Arreglaremos ese error:

    ```C
    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        int *x = malloc(3 * sizeof(int));
        x[0] = 72;
        x[1] = 73;
        x[2] = 33;
    }
    ```
    ```
    $ make memory
    $ ./memory
    $ valgrind ./memory
    ==6435== Memcheck, a memory error detector
    ==6435== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==6435== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
    ==6435== Command: ./memory
    ==6435== 
    ==6435== 
    ==6435== HEAP SUMMARY:
    ==6435==     in use at exit: 12 bytes in 1 blocks
    ==6435==   total heap usage: 1 allocs, 0 frees, 12 bytes allocated
    ==6435== 
    ==6435== 12 bytes in 1 blocks are definitely lost in loss record 1 of 1
    ==6435==    at 0x483B7F3: malloc (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
    ==6435==    by 0x401141: main (memory.c:6)
    ==6435== 
    ==6435== LEAK SUMMARY:
    ==6435==    definitely lost: 12 bytes in 1 blocks
    ==6435==    indirectly lost: 0 bytes in 0 blocks
    ==6435==      possibly lost: 0 bytes in 0 blocks
    ==6435==    still reachable: 0 bytes in 0 blocks
    ==6435==         suppressed: 0 bytes in 0 blocks
    ==6435== 
    ==6435== For lists of detected and suppressed errors, rerun with: -s
    ==6435== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
    ```

   - Ahora, vemos menos salida, con solo un error que nos dice que  ```12 bytes... están definitivamente perdidos ```, ya que los hemos asignado, pero no los hemos liberado.
- Una vez que liberemos nuestra memoria, no veremos errores:

    ```C
    #include <stdio.h>
    #include <stdlib.h>

    int main(void)
    {
        int *x = malloc(3 * sizeof(int));
        x[0] = 72;
        x[1] = 73;
        x[2] = 33;
        free(x);
    }
    ```
    ```
    $ make memory
    $ ./memory
    $ valgrind ./memory
    ==6812== Memcheck, a memory error detector
    ==6812== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==6812== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
    ==6812== Command: ./memory
    ==6812== 
    ==6812== 
    ==6812== HEAP SUMMARY:
    ==6812==     in use at exit: 0 bytes in 0 blocks
    ==6812==   total heap usage: 1 allocs, 1 frees, 12 bytes allocated
    ==6812== 
    ==6812== All heap blocks were freed -- no leaks are possible
    ==6812== 
    ==6812== For lists of detected and suppressed errors, rerun with: -s
    ==6812== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
    ```
    
## Garbage Values
- Echemos un vistazo a este programa:

  ```C
  #include <stdio.h>
  #include <stdlib.h>
  
  int main(void)
  {
      int scores[3];
      for (int i = 0; i < 3; i++)
      {
          printf("%i\n", scores[i]);
      }
  }
  ```
  ```
  $ make garbage
  $ ./garbage
  68476128
  32765
  0
  ```
    - Declaramos una matriz, ```puntuaciones```, pero no la inicializamos con ningún valor.
    - Los valores en la matriz son **valores basura**, o cualquier valor desconocido que estuviera en la memoria, de           cualquier programa que se estuviera ejecutando en nuestra computadora antes.
- Si no tenemos cuidado con la forma en que nuestros programas acceden a la memoria, los usuarios podrían terminar viendo   datos de programas anteriores, como contraseñas. Y si tratamos de ir a una dirección que es un valor basura, es probable que nuestro programa se bloquee debido a una falla de segmentación.
- Vemos [Pointer Fun with Binky](https://www.youtube.com/watch?v=3uLKjb973HU&ab_channel=CS50), un video animado que muestra punteros, malloc y desreferenciación.
El código del video podría verse así en un programa:

  ```C
  int main(void)
  {   
      int *x;  
      int *y; 

      x = malloc(sizeof(int));                    

      *x = 42;
      *y = 13;    

      y = x;        
  
      *y = 13;   
  }
  ```
  - En las dos primeras líneas, declaramos dos punteros. Luego, asignamos memoria para ```x```, pero no para ```y```, por     lo que podemos asignar un valor a la memoria a la que apunta ```x``` con ```*x = 42;```. Pero ```*y = 13;``` es             problemático, ya que no hemos asignado ninguna memoria para ```y```, y el valor de basura allí apunta a algún área de la   memoria a la que probablemente no tengamos acceso.
  - Podemos escribir ```y = x;``` para que ```y``` apunte a la misma memoria asignada que ```x```, y use ```*y = 13;```       para establecer el valor allí.

## Swap
- Tendremos un voluntario en el escenario que intente intercambiar dos líquidos, un líquido naranja en un vaso y un líquido púrpura en otro. Pero necesitamos un tercer vaso para verter temporalmente un líquido, como el líquido naranja en el primer vaso. Luego, podemos verter el líquido morado en el primer vaso y, finalmente, el líquido naranja del tercer vaso en el segundo.
- Intentemos intercambiar los valores de dos enteros:

  ```C
  #include <stdio.h>

  void swap(int a, int b);

  int main(void)
  {
      int x = 1;
      int y = 2;

      printf("x is %i, y is %i\n", x, y);
      swap(x, y);
      printf("x is %i, y is %i\n", x, y);
  }

  void swap(int a, int b)
  {
      int tmp = a;
      a = b;
      b = tmp;
  }
  ```

  ```
  $ make swap
  $ ./swap
  x is 1, y is 2
  x is 1, y is 2
  ```
  - En nuestra función de ```swap```, también tenemos una tercera variable para usar como espacio de almacenamiento temporal. Ponemos ```a``` en ```tmp```, y luego establecemos ```a``` al valor de ```b```, y finalmente ```b``` se puede cambiar al valor original de ```a```, ahora en ```tmp```.
  - Pero, si tratamos de usar esa función en un programa, no vemos ningún cambio.
- Resulta que la función de ```swap``` se pasa en copias de las variables, ```a``` y ```b```, que son ```variables locales``` a las que solo puede acceder la función circundante. Cambiar esos valores no cambiará ```x``` e ```y``` en la función ```main```:
  ```C
  #include <stdio.h>

  void swap(int a, int b);

  int main(void)
  {
      int x = 1;
      int y = 2;

      printf("x is %i, y is %i\n", x, y);
      swap(x, y);
      printf("x is %i, y is %i\n", x, y);
  }

  void swap(int a, int b)
  {
      printf("a is %i, b is %i\n", a, b);
      int tmp = a;
      a = b;
      b = tmp;
      printf("a is %i, b is %i\n", a, b);
  }
  ```

  ```
  $ make swap
  $ ./swap
  x is 1, y is 2
  a is 1, b is 2
  a is 2, b is 1
  x is 1, y is 2
  ```
  - Nuestra función de ```swap``` funciona mientras estamos dentro de ella.
  
## Memory layout
- Dentro de la memoria de nuestra computadora, los diferentes tipos de datos que deben almacenarse para nuestro programa se organizan en diferentes secciones:

  <img src="https://cs50.harvard.edu/x/2022/notes/4/memory_layout.png" width="250" height="400" />

  - La sección de **código de máquina** es el código binario de nuestro programa compilado. Cuando ejecutamos nuestro programa, ese código se carga en la memoria.
  - Justo debajo, o en la siguiente parte de la memoria, están las **variables globales** que declaramos en nuestro programa.
  - La sección **heap** es un área vacía desde donde ```malloc``` puede obtener memoria libre para que la use nuestro programa. Cuando llamamos a ```malloc```, comenzamos a asignar memoria de arriba hacia abajo.
  - La sección **pila** es utilizada por funciones y variables locales en nuestro programa como se les llama, y crece hacia arriba.
- Si llamamos a ```malloc``` por demasiada memoria, tendremos un **desbordamiento de montón**, ya que terminaremos pasando nuestro montón. O, si llamamos a demasiadas funciones sin regresar de ellas, tendremos un **desbordamiento de pila**, donde nuestra pila también tiene demasiada memoria asignada.
- Nuestro programa para intercambiar enteros podría tener una pila como esta:
  
  ```
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       | tmp       |  |  |  |  |
  swap -------------------------
       | a    1    | b    2    |
       -------------------------
  main | x    1    | y    2    |
       -------------------------
  ```
  - Nuestra función ```main``` tiene dos variables locales, ```x``` e ```y```. Nuestra función de ```swap``` se crea encima de ```main``` cuando se llama y tiene tres variables locales, ```a```, ```b``` y ```tmp```.
  - Una vez que regresa el ```swap```, su memoria se libera y sus valores ahora son valores basura, y las variables en ```main``` no se han cambiado.
- Al pasar la dirección de ```x``` e ```y```, nuestra función de ```swap``` podrá cambiar los valores originales:

  ```C
  void swap(int *a, int *b)
  {
      int tmp = *a;
      *a = *b;
      *b = tmp;
  }
  ```
  
  - Las direcciones de ```x``` e ```y``` se pasan desde ```main``` para ```swap``` con ```&x``` e ```&y```, y usamos la sintaxis ```int *a``` para declarar que nuestra función de ```swap``` acepta punteros.
  - Guardamos el primer valor en ```tmp``` siguiendo el puntero ```a```, y luego establecemos el segundo valor en la ubicación a la que apunta ```a``` siguiendo el segundo puntero ```b```.
  - Finalmente, almacenamos el valor de ```tmp``` en la ubicación señalada por ```b```.
- Nuestra pila podría verse así:

  ```
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       | tmp       |  |  |  |  |
  swap -------------------------
       | a  0x123  | b  0x127  |
       -------------------------
  main | x    1    | y    2    |
       -------------------------
  ```
  - Si ```x``` está en ```0x123```, ```a``` contendrá ese valor. ```b``` tendrá la dirección de ```y```, ```0x127```.
- Nuestro primer paso será poner el valor de ```x``` en ```tmp``` siguiendo el puntero ```a```:

  ```
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       | tmp  1    |  |  |  |  |
  swap -------------------------
       | a  0x123  | b  0x127  |
       -------------------------
  main | x    1    | y    2    |
       -------------------------
  ```
- Luego, seguiremos el puntero ```b``` y almacenaremos el valor allí en la ubicación señalada por ```a```:

  ```
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       | tmp  1    |  |  |  |  |
  swap -------------------------
       | a  0x123  | b  0x127  |
       -------------------------
  main | x    2    | y    2    |
       -------------------------
  ```
- Finalmente, iremos a la ubicación señalada por ```b```, y le pondremos el valor de ```tmp```:
  ```
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       |  |  |  |  |  |  |  |  |
       -------------------------
       | tmp  1    |  |  |  |  |
  swap -------------------------
       | a  0x123  | b  0x127  |
       -------------------------
  main | x    2    | y    1    |
       -------------------------
  ```
- Ahora, el ```swap``` puede regresar y las variables en ```main``` aún se cambiarán.
- En nuestro programa, necesitaremos pasar las direcciones de ```x``` e ```y``` a nuestra función de ```swap```:

  ```C
  #include <stdio.h>

  void swap(int *a, int *b);

  int main(void)
  {
      int x = 1;
      int y = 2;

      printf("x is %i, y is %i\n", x, y);
      swap(&x, &y);
      printf("x is %i, y is %i\n", x, y);
  }

  void swap(int *a, int *b)
  {
      int tmp = *a;
      *a = *b;
      *b = tmp;
  }
  $ make swap
  $ ./swap
  x is 1, y is 2
  x is 2, y is 1
  ```
  - Con ```&x```, podemos obtener la dirección de ```x``` para pasar.

## Scanf
- Podemos obtener un número entero del usuario con una función de biblioteca C, ```scanf```:

  ```C
  #include <stdio.h>

  int main(void)
  {
      int x;
      printf("x: ");
      scanf("%i", &x);
      printf("x: %i\n", x);
  }
  ```
  ```
  $ make scanf 
  $ ./scanf
  x: 50
  x: 50
  ```
  - ```scanf``` toma un formato, ```%i```, por lo que la entrada se "escanea" para ese formato. También pasamos la dirección en la memoria donde queremos que vaya esa entrada con ```&x```.
- Podemos intentar obtener una cadena de la misma manera:

  ```C
  #include <stdio.h>

  int main(void)
  {
      char *s;
      printf("s: ");
      scanf("%s", s);
      printf("s: %s\n", s);
  }
  ```
  ```
  $ clang -o scanf scanf.c
  $ ./scanf
  s: HI!
  s: (null)
  ```
  - ```make``` evita que cometamos este error, así que usaremos ```clang``` para demostrarlo.
  - En realidad, no hemos asignado ninguna memoria para ```s```, por lo que ```scanf``` está escribiendo nuestra cadena en una dirección desconocida en la memoria.
- Podemos llamar a ```malloc``` para asignar memoria:

  ```C
  #include <stdio.h>

  int main(void)
  {
      char *s = malloc(4);
      printf("s: ");
      scanf("%s", s);
      printf("s: %s\n", s);
  }
  ```
  ```
  $ clang -o scanf scanf.c
  $ ./scanf
  s: HI!
  s: HI!
  ```
- Y podemos declarar una matriz de 4 caracteres:

  ```C
  #include <stdio.h>

  int main(void)
  {
      char s[4];
      printf("s: ");
      scanf("%s", s);
      printf("s: %s\n", s);
  }
  ```
  ```
  $ clang -o scanf scanf.c
  $ ./scanf
  s: helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
  s: helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
  Segmentation fault (core dumped)
  ```
  - Ahora, si el usuario escribe una cadena de longitud 3 o menos, nuestro programa funcionará de manera segura. Pero si el usuario escribe una cadena más larga, ```scanf``` podría estar intentando escribir más allá del final de nuestra matriz en una memoria desconocida, lo que hace que nuestro programa se bloquee.
- ```get_string``` de la biblioteca CS50 asigna continuamente más memoria a medida que ```scanf``` lee más caracteres, por lo que no tiene este problema.

## Files
- Con la capacidad de usar punteros, también podemos abrir archivos, como una guía telefónica digital en [```phonebook.c ```](https://cdn.cs50.net/2021/fall/lectures/4/src4/phonebook.c?highlight):

  ```C
  // Saves names and numbers to a CSV file

  #include <cs50.h>
  #include <stdio.h>
  #include <string.h>

  int main(void)
  {
      // Open CSV file
      FILE *file = fopen("phonebook.csv", "a");
      if (!file)
      {
          return 1;
      }

      // Get name and number
      string name = get_string("Name: ");
      string number = get_string("Number: ");

      // Print to file
      fprintf(file, "%s,%s\n", name, number);

      // Close file
      fclose(file);
  }
  ```
  - ```fopen``` es una nueva función que podemos usar para abrir un archivo con un nuevo tipo, ```FILE```.
  - Podemos usar ```fprintf``` para escribir en un archivo.
  - Veremos más detalles sobre cómo trabajar con archivos en el conjunto de problemas de esta semana.

## JPEG
- Veamos un programa que abre un archivo y nos dice si es un archivo JPEG, un formato particular para archivos de imagen, con  [```jpeg.c ```](https://cdn.cs50.net/2021/fall/lectures/4/src4/jpeg.c?highlight):

  ```C
  // Detects if a file is a JPEG

  #include <stdint.h>
  #include <stdio.h>

  typedef uint8_t BYTE;

  int main(int argc, char *argv[])
  {
      // Check usage
      if (argc != 2)
      {
          return 1;
      }

      // Open file
      FILE *file = fopen(argv[1], "r");
      if (!file)
      {
          return 1;
      }

      // Read first three bytes
      BYTE bytes[3];
      fread(bytes, sizeof(BYTE), 3, file);

      // Check first three bytes
      if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
      {
          printf("Yes, possibly\n");
      }
      else
      {
          printf("No\n");
      }

      // Close file
      fclose(file);
  }
  ```
  ```
  $ make jpeg
  $ ./jpeg .src4/lecture.jpg
  Yes, possibly
  ```
  - Primero, definimos un ```BYTE``` como 8 bits, por lo que podemos referirnos a un byte como un tipo más fácilmente en C
  - Luego, leeremos de un archivo con una función llamada ```fread```.
  - Podemos comparar los primeros tres bytes (en hexadecimal) con los tres bytes necesarios para comenzar un archivo JPEG. Si son iguales, es probable que nuestro archivo sea un archivo JPEG (aunque otros tipos de archivos aún pueden comenzar con esos bytes). Pero si no son iguales, sabemos que definitivamente no es un archivo JPEG.
- Resulta que los archivos BMP, otro formato para imágenes, tienen incluso más bytes en su encabezado o principio del archivo.
- También aprenderemos más sobre estos en el conjunto de problemas de esta semana, e incluso implementaremos nuestra propia versión de filtros de imagen, como uno que solo muestra el color rojo:

  ```C
  #include "helpers.h"

  // Only let red through
  void filter(int height, int width, RGBTRIPLE image[height][width])
  {
      // Loop over all pixels
      for (int i = 0; i < height; i++)
      {
          for (int j = 0; j < width; j++)
          {
              image[i][j].rgbtBlue = 0x00;
              image[i][j].rgbtGreen = 0x00;
          }
      }
  }
  ```
  - Here, we have a loop that iterates over all the pixels in a two-dimensional array, and sets the blue and green values to 0.
