# **Lectura 6**

* [Sintaxis de Python](#sintaxis-de-python)
* [Librerias](#librerias)
* [Entrada, condiciones](#input-conditions-entradas-condiciones)
  * [Meow](#meow)
* [Mario](#mario)
* [Documentación](#documentación)
* [Listas, cadenas](#listas-cadenas)
* [Argumentos de línea de comandos, códigos de salida](#argumentos-de-línea-de-comandos-códigos-de-salida)
* [Algoritmos](#algoritmos)
* [Archivos](#archivos)
* [Más librerias](#más-librerias)

# **Sintaxis de Python**

* Hoy aprenderemos un nuevo lenguaje de programación llamado Python, aunque nuestro objetivo principal es aprender a aprender nuevos lenguajes por nosotros mismos.

* El código fuente en Python parece mucho más simple que en C, aunque tiene muchas de las mismas ideas. Para imprimir “hola, mundo”, todo lo que necesitamos escribir es:
---
```python
print("Hello, world");
```

---

* Note que, a diferencia de C, no necesitamos especificar una nueva línea en la función de impresión, o usar un punto y coma para terminar nuestra línea.

* En Scratch y C, podríamos haber tenido múltiples funciones
---

![](/Notas6_markdown/foto_notas.jpg)

----

```python  
 String answer = get_string("Cual es tu nombre ?");
 printf("hola, %s\n" responder);
```
----

* En Python, el equivalente se vería así: 

---
```python
      answer = get_string ("cual es tu nombre ?")
      Print("hola, " + answer)
 
```
----
  * Podemos crear una variable llamada  ***answer***(respuesta) sin especificar el tipo, y podemos unir o concatenar dos cadenas con el operador + antes de pasarla a la ***Print*** (impresión).

    * La función ***get_string*** también proviene de la versión Python de la biblioteca CS50.

* También podemos escribir:
---
```python
      Print(f"herlo, {answer}")  
```
---

  * La ***f*** antes de las comillas dobles indica que se trata de una cadena de formato, lo que nos permitirá usar llaves,***{ }***, para incluir variables que deben sustituirse o interpolarse.

* Podemos crear variables con just ***counter = 0***. Para incrementar una variable, podemos escribir counter = ***counter + 1 o counter += 1***.

* Las condicionales se ven así:
---
```python
      if x < y:
           print("x is less than y")
      elif x > y:
           print("x is greater than y")
      else:
           print("x is equal to y")
```
---
  * A diferencia de C, donde se usan llaves para indicar bloques de código, la sangría exacta de cada línea determina el nivel de anidamiento en Python. Y no necesitamos paréntesis alrededor de las expresiones booleanas.

  * Y en lugar de ***else if***, simplemente decimos ***elif***.

* Podemos escribir un ciclo while con una variable:
---
  
```python  
      while True:
          print("meow")
```
---

* Podemos escribir un ciclo while con una variable:
```python
      i = 0
      while i < 3:
          print("meow")
          i += 1
``` 
* Podemos escribir un ciclo for, donde podemos hacer algo para cada valor en una lista:
---
```python
 for i in [0, 1, 2]:
    print("hello, world")
```
----
  * Las listas en Python, ***[0, 1, 2]***, son como arreglos o listas enlazadas en C.
  * Este bucle for establecerá la variable ***i*** en ***0***, ejecutar, luego en el segundo valor, ***1***, ejecutar, y así sucesivamente.

* Y podemos usar una función especial, ***range***, para obtener cualquier número de valores:
---
  
```python  
      for i in range(3):
           print("hello, world")
```
---
  * ***range(3)*** nos dará una lista hasta el 3, pero sin incluirlo, con los valores ***0***,***1*** y ***2***, que luego podemos usar.
 
  * ***range()*** también toma otros argumentos, por lo que podemos tener listas que comienzan en diferentes valores y tienen diferentes incrementos entre valores.

* En Python, hay tipos de datos integrados similares a los de C:
  
  * ***Bool***, ***verdadera*** o ***falso***
  * ***float***, números rales.
  * ***int***, números enteros que pueden crecer según sea necesario
  * ***str***, strings

* Otros tipos en Python incluyen

   * ***range***, secuencia de numeros
   * ***list***, secuencia de valores mutables, o valores que podemos cambiar 
   * ***tuple***, secuencia de valores inmutables
   * ***dict***, diccionarios, colección de pares clave/valor, como una tabla hash
   * ***set***, colección de valores únicos, o valores sin duplicados
   
* La biblioteca CS50 para Python también incluye funciones para obtener información del usuario:

   *    ***get_float***
   *    ***get_int***
   *    ***get_string***

* Y podemos importar una biblioteca completa, funciones de una en una o múltiples funciones: 
---
```python
       * import cs50 
       
```
----
---
```python
       * from cs50 import get_float
       * from cs50 import get_int
       * fron cs50 import get_string
```
---
```python
       * from cs50 import get_float, get_int, get_string
```

# ***Librerias***

* Recuerde que, en C, necesitábamos compilar un programa con make hello antes de poder ejecutarlo.

* Para ejecutar un programa que escribimos en Python, solo necesitaremos ejecutar:
---
```python
       python hello.py
```

   * ***python*** es el nombre de un programa llamado ***interpreter***, que lee nuestro código fuente y lo traduce a un código que nuestra CPU puede entender, línea por línea.

   * Nuestros archivos de código fuente también terminarán en ***.py***, para indicar que están escritos en lenguaje Python.

* Por ejemplo, si nuestro pseudocódigo para encontrar a alguien en una guía telefónica estuviera en español y no entendiéramos español, primero tendríamos que traducirlo lentamente, línea por línea, al inglés:
 ---

       1   Recoge guía telefónica
       2   Abre a la mitad de guía telefónica
       3   Ve la página
       4   Si la persona está en la página
       5       Llama a la persona
       6   Si no, si la persona está antes de mitad de guía telefónica
       7       Abre a la mitad de la mitad izquierda de la guía telefónica
       8       Regresa a la línea 3
       9   Si no, si la persona está después de mitad de guía telefónica
      10      Abre a la mitad de la mitad derecha de la guía telefónica
      11      Regresa a la línea 3
      12  De lo contrario
      13      Abandona
---

   * Del mismo modo, los programas en Python tardarán un poco más en interpretarse a medida que se ejecutan.

* Nosotras podemos difuminar una imagen con:
```python
       from PIL import Image, ImageFilter

       before = Image.open("bridge.bmp")
       after = before.filter(ImageFilter.BoxBlur(10))
      after.save("out.bmp")
```     
   * En Python, incluimos otras bibliotecas con **import***, y aquí importaremos los nombres de ***Imagen*** e ***ImageFilter*** de la biblioteca ***PIL***.
   
   * La imagen es un ***objeto***, como una estructura en C. Los objetos en Python no solo pueden tener valores, sino también funciones a las que podemos acceder con . syntax, such as with ***Image.open***. Y antes también hay un objeto con una función de ***filtro***, que podemos encontrar en la documentación de la biblioteca.

   * Podemos ejecutar esto con ***python blur.py*** en el mismo directorio que nuestro archivo ***bridge.bmp***:
  
         filter/ $ ls
         blur.py  bridge.bmp
         filter/ $ python blur.py
         filter/ $ ls
         blur.py  bridge.bmp  out.bmp
         filter/ $ 

* También podemos encontrar los bordes en la imagen con:
   
```python   
         from PIL import Image, ImageFilter

         before = Image.open("bridge.bmp")
         after = before.filter(ImageFilter.FIND_EDGES)
         after.save("out.bmp")
```
* Nosotros podemos implementar un diccionario con:

```python
      words = set()

      def check(word):
          if word.lower() in words:
              return True
          else:
              return False

       def load(dictionary):
           file = open(dictionary, "r")
           for line in file:
                word = line.rstrip()
                words.add(word)
           file.close()
             return True

      def size():
             return len(words)

      def unload():
             return True
  ```

  * Primero, creamos un nuevo conjunto llamado ***words*** al que podemos agregar valores, y hacer que el idioma verifique si hay duplicados por nosotros.

  * Definiremos una función con ***def*** y comprobaremos si ***word***, el argumento, está en nuestra tabla hash. (También llamaremos a una función, ***.lower***(), para obtener la versión en minúsculas de la palabra).

  * Nuestra función ***load***  tomará un nombre de archivo, un ***dictionary*** y lo abrirá para su lectura. Recorreremos las líneas en el archivo con ****for line in file:*** y agregaremos cada palabra después de eliminar la nueva línea de cada línea con ***rstrip***.

  * Para ***size*** , podemos usar ***len*** para contar la cantidad de elementos en nuestro diccionario y, finalmente, para ***unload***, no tenemos que hacer nada, ya que Python administra la memoria por nosotros.

* Podemos ejecutar nuestro programa con ***python speller.py texts/holmes.txt***, pero notaremos que tarda unos segundos más en ejecutarse que la versión C. A pesar de que fue mucho más rápido para nosotros escribir, no podemos optimizar completamente nuestro código administrando la memoria e implementando todos los detalles nosotros mismos. 

* Resulta que podemos almacenar en caché o guardar la versión interpretada de nuestro programa Python, por lo que se ejecuta más rápido después de la primera vez. Y Python también está parcialmente compilado, en un paso intermedio llamado bytecode, que luego ejecuta el intérprete.

# **Input, conditions( entradas, condiciones)**

   * Podemos practicar obteniendo información del usuario:
```python
    from cs50 import get_string

    answer = get_string("What's your name? ")
    print("hello, " + answer)

    $ python hello.py
    What's your name? David
    hello, David
```
  * Tenga en cuenta que nuestro programa no necesita una función ***main***. En su lugar, nuestro código se ejecutará automáticamente línea por línea.

  * También podemos usar una cadena de formato: ***print(f"hola, {respuesta}")***.

* También podemos usar una función que viene con Python, input:
```python
   
      answer = input("What's your name? ")
      print("hello, " + answer)
```
  * Dado que solo obtenemos una cadena del usuario, input es la misma que ***get_string***.

* ***get_int*** y ***get_float*** tendrán una verificación de errores para nosotros, por lo que podemos obtener valores numéricos más fácilmente:
```python
      from cs50 import get_int

      x = get_int("x: ")
      y = get_int("y: ")
      print(x + y)
```
  * Como estamos imprimiendo solo un valor, podemos pasarlo a ***print*** directamente.

* Si importamos toda la biblioteca, vemos un error con un seguimiento de pila o seguimiento:
```python

       import cs50

       x = get_int("x: ")
       y = get_int("y: ")
       print(x + y)
```
---
```python
      $ python calculator.py
      Traceback (most recent call last):
      File "/workspaces/20377622/calculator.py", line 3, in <module>
       x = get_int("x: ")
       NameError: el nombre 'get_int' no está definido
```
---
   *  Resulta que necesitamos escribir ***cs50.get_int(...)*** cuando importamos toda la libreria. Esto nos permite la funcion ***namespace***, o mantener sus nombres en diferentes espacios, con diferentes prefijos. Entonces, varias bibliotecas con una función ***get_int*** no colisionarán.

* Si llamamos a input nosotros mismos, obtenemos cadenas para nuestros valores:
---
```python
       x = input("x: ")
       y = input("y: ")
       print(x + y)
```
---
```python
      $  python calculator.py
      x: 1
      y: 2 
      12
```
  
   * imprimimos las dos cadenas, unidas como una cadena más.

* Entonces, necesitamos ***cast***, o convertir, cada valor de ***imnput*** entrada en un ***int***antes de almacenarlo:

```python
      x = int(input("x: "))
      y = int(input("y: "))
      print(x + y)
```

   * Tenga en cuenta que ***int***en Python es una función a la que podemos pasar un valor.
   
   * Pero si el usuario no ingresó un número, tendremos que hacer una verificación de errores o nuestro programa fallará:


         $ python calculator.py
         x: cat 
         Traceback (most recent call last):
           File "/workspaces/20377622/calculator.py", line 1, in <module>
             x = int(input("x: "))
         ValueError: invalid literal for int() with base 10: 'cat'

* ***ValueError*** es un tipo de ***excption***, o algo que sale mal cuando nuestro código se está ejecutando. En Python, podemos intentar hacer algo y detectar si hay una excepción:
```python
        try:
            x = int(input("x: "))
        except ValueError:
            print("That is not an int!")
            exit()
        try:
            y = int(input("y: "))
            except ValueError:
            print("That is not an int!")
            exit()
        print(x + y)
```

   * Ahora, si hay una excepción al convertir la entrada en un número entero, podemos imprimir un mensaje y salir sin fallar.

* Podemos dividir valores:
```python
        from cs50 import get_int

        x = get_int("x: ")
        y = get_int("y: ")

        z = x / y
        print(z)
```
---
```python
        $ python calculator.py
        x: 1
        y: 10
        0.1
```

  * Observe que obtenemos valores decimales de coma flotante, incluso si dividimos dos enteros. El operador de división en Python no trunca esos valores por defecto. (Podemos obtener el mismo comportamiento que en C, truncamiento, con el operador //, como ***z = x // y)***.

* Podemos usar una cadena de formato para imprimir más dígitos después del punto decimal:
```python
      from cs50 import get_int

       x = get_int("x: ")
       y = get_int("y: ")

       z = x / y
       print(f"{z:.50f}")
```
---
     $ python calculator.py
      x: 1
      y: 10
      0.10000000000000000555111512312578270211815834045410
 
    * Desafortunadamente, todavía tenemos imprecisión de punto flotante.

* Los comentarios en Python comienzan con un ***#***:
```python

      from cs50 import get_int
  
      # Prompt user for points
      points = get_int("How many points did you lose? ")
        # Compare points against mine
      if points < 2:
          print("You lost fewer points than me.")
      elif points > 2:
          print("You lost more points than me.")
      else:
          print("You lost the same number of points as me.")
```
 
   * Nuestro código también es mucho más corto que el mismo programa en C.

* Podemos comprobar la paridad de un número con el operador , %:

```python
     from cs50 import get_int
  
        n = get_int("n: ")
  
       if n % 2 == 0:
           print("even")
       else:
           print("odd")
```
---

        $ python parity.py
       n: 50
       even
 

* Para comparar cadenas, podemos decir:
```python

     from cs50 import get_string

      s = get_string("Do you agree? ")

      if s == "Y" or s == "y":
          print("Agreed.")
      elif s == "N" or s == "n":
          print("Not agreed.")
---
        $ python agree.py
        Do you agree? y
        Agreed.
  ```
  * Python no tiene un tipo de datos para caracteres individuales, por lo que verificamos Y y otras letras como cadenas. (También podemos usar comillas simples o dobles para las cadenas, siempre que seamos coherentes).

    * Podemos comparar cadenas directamente con ==, y podemos usar or y and en nuestras expresiones booleanas.

* También podemos verificar si nuestra cadena está en una lista, después de convertirla primero a minúsculas:
```python
      from cs50 import get_string

      s = get_string("Do you agree? ")

      s = s.lower()

      if s in ["y", "yes"]:
          print("Agreed.")
      elif s in ["n", "no"]:
          print("Not agreed.")
```
 * Llamamos a ***s.lower()*** para obtener la versión en minúsculas de la cadena y luego la almacenamos de nuevo en ***s***.

* Incluso podemos simplemente decir ***s = get_string("¿Está de acuerdo?").lower()*** para convertir la entrada a minúsculas inmediatamente, antes de almacenarla en ***s***.

* En Python, las cadenas también son inmutables o no modificables. Cuando hacemos cambios en una cadena, se hace una nueva copia para nosotros, junto con toda la gestión de la memoria.

# ***#meow***

  * También podemos demostrar mejoras de diseño en nuestro programa meow:
---    
```python
print("meow")
print("meow")
print("meow")
```
* Aquí, tenemos la misma línea de código tres veces.
* Pdemos usar un bucle:

```python
for i in range(3):
print("meow")
´´´
---

*Podemos definir una función que podemos reutilizar:

---
```python
for i in range(3):
meow()

def meow():
print("meow")
```
---
* Pero esto provoca un error cuando intentamos ejecutarlo: NameError: name 'meow' no está definido. Resulta que, como en C, necesitamos definir nuestra función antes de usarla. Así que definiremos una función principal primero:

```python
      def main():
        for i in range(3):
           meow()

      def meow():
        print("meow")

      main()
```
   * Ahora, para cuando llamemos a nuestra función main al final de nuestro programa, la función meow ya habrá sido definida.

  * La parte importante de nuestro código seguirá estando en la parte superior de nuestro archivo, por lo que es fácil de encontrar.

* También podríamos ver ejemplos que llaman a una función main  con:
---

```python
if __name__ == "__main__":
main()
```
---
   * Esto resuelve los problemas de incluir nuestro código en las bibliotecas, pero no necesitaremos considerar eso todavía, por lo que simplemente podemos llamar a main().

* Nuestras funciones también pueden tomar argumentos:
---
```python
     def main():
         meow(3)

     def meow(n):
         for i in range(n):
              print("meow")

      main()
```
   * Nuestra función ***meow*** toma un parámetro, ***n***, y lo pasa al ***range*** en un bucle for.

  * Tenga en cuenta que no necesitamos especificar el tipo de un argumento.

* Podemos crear variables globales inicializándolas fuera de ***main***, aunque Python no tiene constantes.
# Mario
* Podemos imprimir una fila de simbolos de numeral en pantalla:
    ```python
    from cs50 import get_int

    n = get_int("Altura: ")

    for i in range(n):
        print("#")
    ```
    ```
    $ python mario.py
    Altura: -1
    ```  
   * Si el usuario ingresa un número negativo, no vemos ningún resultado. En su lugar, deberíamos volver a preguntar al usuario.
* En Python, no hay bucle do while, pero podemos hacer el mismo efecto:
    ```python
    from cs50 import get_int

    while True:
        n = get_int("Altura: ")
        if n > 0:
            break

    for i in range(n):
        print("#")
    ```
    * Escribiremos un bucle infinito, por lo que haremos una acción al menos una vez, y luego usaremos `break` para salir del bucle si cumplimos alguna condición. 
* Podemos usar una función para apoyarnos:
    ```python
    from cs50 import get_int

    def main():
        altura = get_altura()
        for i in range(altura):
            print("#")

    def get_altura():
        while True:
            n = get_int("Altura: ")
            if n > 0:
                break
        return n

    main()
    ```
    * Nuestra función `get_altura()` devolverá n después de que se cumpla nuestra condición. Hay que tener en cuenta que en Python, las variables están en el ámbito de una función, lo que significa que podemos usarlas fuera del bucle en el que se crean.
* Podemos usar `input` nosotros mismos:
    ```python
    def main():
        altura = get_altura()
        for i in range(altura):
            print("#")
    
    def get_altura():
        while True:
            n = int(input("Altura: "))
            if n > 0:
                break
        return n
    
    main()
    ```
    ```
    $ python mario.py
    Altura: cat
    Traceback (most recent call last):
    File "/workspaces/20377622/mario.py", line 13, in <module>
        main()
    File "/workspaces/20377622/mario.py", line 2, in main
        altura = get_altura()
    File "/workspaces/20377622/mario.py", line 8, in get_altura
        n = int(input("Altura: "))
    ValueError: invalid literal for int() with base 10: 'cat'
    ```
    * Si no obtenemos una entrada válida, nuestro rastreo muestra la pila de funciones que condujeron a la excepción.
* Intentaremos (`try`) convertir la entrada en un número entero e imprimir (`print`) un mensaje si hay una excepción. Pero no necesitamos salir, ya que nuestro bucle volverá a avisar al usuario. Si no hay una excepción, continuaremos verificando si el valor es positivo y romperemos (`break`) si es así:
    ```python
    def main():
        altura = get_altura()
        for i in range(altura):
            print("#")
    
    def get_altura():
        while True:
            try:
                n = int(input("Altura: "))
                if n > 0:
                    break
            except ValueError:
                print("Ese no es un entero!")
        return n
    
    main()
    ```
    * Ahora podemos intentar imprimir signos de interrogación en la misma línea:
    ```python
    for i in range(4):
        print("?", end="")
    print()
    ```
    ```
    $ python mario.py
    ????
    ```
    * Cuando imprimimos cada signo de interrogación, no queremos la nueva línea automáticamente, por lo que podemos pasar un **argumento con nombre**, también conocido como argumento de palabra clave, a la función de impresión(`print`). (Hasta ahora, solo hemos visto **argumentos posicionales**, donde los argumentos se establecen en función de su posición en la llamada de función).
    * Aquí, pasamos `end=""` para especificar que no se debe imprimir nada al final de nuestra cadena. Si observamos la documentación para imprimir (`print`), veremos que el valor predeterminado para `end` es `\n`, una nueva línea.
    * Finalmente, después de imprimir nuestra fila con el bucle, podemos llamar a `print` sin otros argumentos para obtener una nueva línea.
* También podemos usar el operador de multiplicación para unir una cadena consigo misma muchas veces e imprimirla directamente con: `print("?" * 4)`.
* También podemos implementar bucles anidados:
```python
for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```
```
$ python mario.py
###
###
###
```
# Documentación
* La documentación oficial de Python incluye referencias para funciones integradas.
* Podemos usar la función de búsqueda para encontrar una página sobre funciones que vienen con cadenas, por ejemplo, incluida la función `lower()` para convertir una cadena a minúsculas. En la misma página, veremos muchas otras funciones, aunque no debemos preocuparnos por aprenderlas todas inmediatamente. 
# Listas, cadenas
* Podemos crear una lista:
    ```python
    notas = [72, 73, 33]

    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    ```
    * Podemos usar `sum`, una función integrada en Python, para sumar los valores de nuestra lista y dividirla por el número de notas, usando la función `len` para obtener la longitud de la lista.
* Podemos agregar elementos a una lista con:
    ```python
    from cs50 import get_int

    notas = []
    for i in range(3):
        nota = get_int("Nota: ")
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    ```
    * Con el método `append`, una función integrada en los objetos de lista, podemos agregar nuevos valores a las `notas`.
    * También podemos unir dos listas con `notas += [nota]`. Tenga en cuenta que necesitamos poner `nota` en una lista propia.
* Podemos iterar sobre cada carácter en una cadena:
    ```python
    from cs50 import get_string

    antes = get_string("Antes:  ")
    print("Despues:  ", end="")
    for c in antes:
        print(c.upper(), end="")
    print()
    ```
    * Python iterará sobre cada carácter de la cadena para nosotros con solo `for c in antes:`.
* Para poner una cadena en mayúsculas, también podemos simplemente escribir `despues = antes.upper()`, sin tener que iterar sobre cada carácter nosotros mismos.

# **Argumentos de línea de comandos, códigos de salida**
- Podemos tomar argumentos de línea de comandos con:

    ```python
        from sys import argv

        if len(argv) == 2:
            print(f"hola, {argv[1]}")
        else:
            print("hola, mundo")
    ```
    ```
        $ python argv.py
        hola, mundo
        $ python argv.py David
        hola, David
    ```

    * Importamos `argv` desde `sys` , el módulo del sistema, integrado en Python. 
 
    * Dado que `argv` es una lista, podemos obtener el segundo elemento com `argv[1]`.

    * `argv[0]` sería el nombre de nuestro programa, como `argv.py` y no Python.


- También podemos dejar que Python itere sobre la lista por nosotros:

    ```python
    from sys import argv

    for arg in argv:
        print(arg)
    ```
    ```
    $ python argv.py
    argv.py
    $ python argv.py foo bar baz
    argv.py
    foo
    bar
    baz
    ```
    - Con Python, podemos empezar en un índice diferente en una lista:
        
        ```python
        for arg in argv[1: ]:
            print(arg)
        ```
        - Esto nos permite **dividir** la lista desde 1 hasta el final.
        - Podemos escribir ```argv[:-1]``` para obtener todo lo que hay en la lista, excepto el último elemento.
- También podemos devolver códigos de salida cuando nuestro programa finaliza:

    ```python
    from sys import argv, exit

    if len(argv) != 2:
        print("Falta el argumento de la línea de comandos")
        exit(1)

    print(f"hola, {argv[1]}")
    exit(0)
    ```
    * Ahora, podemos usar `exit()` para salir de nuestro programa con un código específico.
* Podemos importar toda la biblioteca `sys` y dejar claro en nuestro programa de dónde provienen estas funciones:
    ```python
    import sys

    if len(sys.argv) != 2:
        print("Falta el argumento de la línea de comandos")
        sys.exit(1)
      
    print(f"hola, {sys.argv[1]}")
    sys.exit(0)
    ```
    ```
    $ python exit.py
    Falta el argumento de la línea de comandos
    $ python exit.py David
    hola, David
    ```

# **Algoritmos**
- Podemos tomar argumentos de línea de comandos con:

    ```python
    import sys

    numeros = [4, 6, 8, 2, 7, 5, 0]

    if 0 in numeros:
        print("Encontrado")
        sys.exit(0)

    print("No encontrado")
    sys.exit(1)
    ```
    * Con `if 0 en numeros:`, le estamos pidiendo a Python que verifique la lista por nosotros.
*  Una lista de cadenas, también, se puede buscar con:
    ```python
    import sys

    nombres = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

    if Ron in nombres:
        print("Encontrado")
        sys.exit(0)

    print("No encontrado")
    sys.exit(1)
    ```
* Si tenemos un diccionario, un conjunto de pares clave-valor, también podemos verificar una clave en particular y ver el valor almacenado para ella:
    ```python
    from cs50 import get_string

    personas = {
        "Carter" : "+1-617-495-1000",
        "David" : "+1-949-468-2750"
    }

    nombre = get_string("Nombre: ")
    if nombre in personas:
        numero = persona[nombre]
        print(f"Numero: {numero}")
    ```
    ```
    $ python guiatelefonica.py
    Nombre: David
    Numero: +1-949-468-2750
    ```
* Primero declaramos un diccionario, `personas`, donde las claves son cadenas de cada nombre que queremos almacenar, y el valor de cada clave es una cadena de un número de teléfono correspondiente.

* Luego, usamos `if nombre in personas:` para buscar un nombre en las claves de nuestro diccionario. Si la clave existe, entonces podemos obtener el valor con la notación de paréntesis, `personas[nombre]`.

# **Archivos**
- Abramos un archivo CSV, con valores separados por comas:

    ```python
    import csv
    from cs50 import get_string

    file = open("guiatelefonica.csv", "a")

    nombre = get_string("Nombre: ")
    numero = get_string("Numero: ")

    escritor = csv.escritor(file)
    escritor.filaescritor([nombre, numero])

    file.close()
    ```
    ```
    $ python guiatelefonica.py
    Nombre: Carter
    Numero: +1-617-495-1000
    $ls
    guiatelefonica.csv guiatelefonica.py
    ```
    * Resulta que Python también tiene una biblioteca `csv` que nos ayuda a trabajar con archivos CSV, por lo que después de abrir el archivo para agregarlo, podemos llamar a `escritor` para crear un objeto de `escritor` a partir del archivo. Luego, podemos usar un método dentro, `escritor.filaescritor`, para escribir una lista como una fila.

*  Nuestro archivo `guiatelefonica.csv` tendrá nuestros datos:
    ```
     Carter, +1-617-495-1000
    ```
    * Podemos volver a ejecutar nuestro programa y ver cómo se agregan nuevos datos a nuestro archivo.

* Podemos usar la palabra clave `with`, que cerrará el archivo una vez que hayamos terminado:

    ```python
    ...
    with open("guiatelefonica.csv", "a") as file:
        escritor = csv.escritor(file)
        escritor.filaescritor((nombre, numero))
    ```
* Visitaremos un Formulario de Google y seleccionaremos una [`"casa"`](https://harrypotter.fandom.com/wiki/Hogwarts_Houses) en la que nos gustaría estar.

* Descargaremos los datos como un archivo CSV, que se ve así:
    ```
    Timestamp, House
    10/13/2021 16:00:07, Ravenclaw
    10/13/2021 16:00:07, Gryffindor
    10/13/2021 16:00:09, Ravenclaw
    10/13/2021 16:00:10, Gryffindor
    10/13/2021 16:00:10, Gryffindor
    ...
    ```
* Ahora podemos contar el número de veces que una casa aparece:
    ```python
        import csv

        casas = {
        "Gryffindor": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
        "Slytherin": 0
        }

        with open("hogwarts.csv", "r") as file:
        lector = csv.lector(file)
        next(lector)
        for fila in lector:
            casa = fila[1]
            casas[casa] += 1
        for casa in casas:
        contador = casas[casa]
        print(f"{casa}: {contador}")
    ```
    * Usamos la función de `lector` de la libreria `csv`, omitimos la fila del encabezado con `next(lector)` y luego iteramos sobre cada una de las filas restantes.

    * El segundo elemento de cada fila, `fila[1]`, es la cadena de una casa, por lo que podemos usar eso para acceder al valor almacenado en `casas` para esa clave, y agregarle uno con `casas[casa] += 1`.

    * Finalmente, imprimiremos el conteo de cada casa.

* Podemos mejorar nuestro programa leyendo cada fila como un diccionario, usando la primera fila en el rchivo como las claves para cada valor:
    ```python
    ...
    with open("hogwarts.csv", "r") as file:
        lector = csv.Dictlector(file)
        for fila in lector:
            casa = fila["Casa"]
            casas[casa] += 1
    ...
    ```
    * Ahora, podemos decir `casa = fila["Casa"]` para obtener el valor en esa columna.  

# **Más librerias**
- En nuestra propia Mac o PC, podemos usar otra libreria para convertir texto a voz (ya que VS Code en la nube no admite audio):
    ```python
       import pyttsx3

       motor = pyttsx3.init()
       motor.dice("hola, mundo")
       motor.correyEspera()
    ```
    * Al leer la documentación, podemos usar una libreria de Python llamada `pyttsx3` para reproducir algunas cadenas como audio.
    * Incluso podemos pasar una cadena de formato con `engine.dice(f"hola, {nombre}")` para decir alguna entrada.
* Podemos usar otra libreria, `reconocimiento_facial`, para encontrar rostros en imágenes con [`detect.py`](https://cdn.cs50.net/2021/fall/lectures/6/src6/6/faces/detect.py?highlight):
    ```python
       # Encuentra caras en la imagen
       # https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py

       from PIL import Imagen
       import reconocimiento_facial

       # Cargue el archivo jpg en una matriz numpy
       imagen = reconocimiento_facial.carga_imagen_file("oficina.jpg")

       # Encuentre todas las caras en la imagen usando el modelo basado en HOG predeterminado.
       # Este método es bastante preciso, pero no tanto como el modelo CNN y no acelerado por GPU.
       # Ver también: reconocimiento_facial_en_imagen_cnn.py
       ubicaciones_de_rostros = reconocimiento_facial. ubicaciones_de_rostros(imagen)

       for ubicacion_de_rostro in ubicaciones_de_rostros:

        # Imprime la ubicación de cada rostro en esta imagen.
        arriba, derecha, abajo, izquierda = ubicacion_de_rostro

        # Puede acceder a la cara real en sí misma de esta manera:
        cara_imagen = imagen[arriba:abajo, izquierda:derecha]
        pil_imagen = Imagen.delamatriz(cara_imagen)
        pil_imagen.show()
    ```
* En [`reconocer.py`](https://cdn.cs50.net/2020/fall/lectures/6/src6/6/faces/recognize.py), podemos ver un programa que encuentra una coincidencia para una cara en particular.
* En [`listen0.py`](https://cdn.cs50.net/2021/fall/lectures/6/src6/6/listen/listen0.py?highlight), podemos responder a la entrada del usuario:
    ```python
       # Reconoce un saludo

       # Obtener entrada
       palabras = input(¡Di algo!\n).lower()

       # Responder al discurso
       if "hola" en palabras:
        print("¡Hola a ti también!")
       elif "como estas" en palabras:
        print("¡Estoy bien, gracias!")
       elif "adios" en palabras:
        print("¡Adiós a ti también!")
       else:
        print("¿Eh?")
    ```
* Podemos reconocer la entrada de audio de un micrófono y responder con [`listen2.py`](https://cdn.cs50.net/2021/fall/lectures/6/src6/6/listen/listen2.py?highlight):
    ```python
       # Responde a un saludo
       # https://pypi.org/project/SpeechRecognition/

       import reconocimiento_de_voz

       # Obtener audio desde el micrófono
       reconocedor = reconocimiento_de_voz.Reconocedor()
       with reconocimiento_de_voz.Microfono() as fuente:
            print("Di algo:")
            audio = reconocedor.escuchar(fuente)

       # Reconocer el habla usando el reconocimiento de voz de Google
       palabras = reconocedor.reconoce_google (audio)

       # Responder al discurso
       if "hola" en palabras:
        print("¡Hola a ti también!")
       elif "como estas" en palabras:
        print("¡Estoy bien, gracias!")
       elif "adios" en palabras:
        print("¡Adiós a ti también!")
       else:
        print("¿Eh?")
    ```
* Podemos incluso agregar más lógica para escuchar un nombre:
    ```python
       # Responde a un nombre
       # https://pypi.org/project/SpeechRecognition/

       import re
       import reconocimiento_de_voz

       # Obtener audio desde el micrófono
       reconocedor = reconocimiento_de_voz.Reconocedor()
       with reconocimiento_de_voz.Microfono() as fuente:
            print("Di algo:")
            audio = reconocedor.escuchar(fuente)

       # Reconocer el habla usando el reconocimiento de voz de Google
       palabras = reconocedor.reconoce_google (audio)

       # Responder al discurso
       coincidencias = re.buscar("mi nombre es (.*)", palabras)
       if coincide:
        print(f"Hey, {coincidencias[1]}.")
      else:
        print("Hey, tú")
    ```
* Podemos crear un [`código QR`](https://en.wikipedia.org/wiki/QR_code), o un código de barras bidimensional, con otra librería:
    ```python
       import os
       import qrcode

       img = qrcode.hacer("https://youtu.be/xvFZjo5PgG0")
       img.guardar("qr.png", "PNG")
       os.system("open qr.png")
    ```