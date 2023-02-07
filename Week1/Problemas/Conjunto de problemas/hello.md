# **HOLA**
## **Para comenzar** 
 Recuerda que Visual Studio Code  también conocido como VS Code) es un popular "entorno de desarrollo integrado" (IDE) a través del cual puedes escribir código. Para que no tengas que descargar, instalar y configurar tu propia copia de VS Code, utilizaremos una versión basada en la nube que tiene todo lo que necesitas preinstalado.

 Entra en [code.cs50.io](https://code.cs50.io) utilizando tu cuenta de GitHub. Una vez que su "espacio de código" se cargue, deberías ver que, por defecto, VS Code está dividido en tres regiones.En  la parte superior de VS Code está tu "editor de texto", donde escribirás todos tus programas. En  la parte inferior  se encuentra la "ventana de terminal", una interfaz de línea de comandos (CLI) que le permite explorar los archivos y directorios (también conocidos como carpetas) de su espacio de código, compilar código y ejecutar programas. Y a la izquierda está el "explorador" de archivos, una interfaz gráfica de usuario (GUI) a través de la cual también puedes explorar los archivos y directorios de tu espacio de código.

 Comienza por hacer clic dentro de la  ventana de terminal, luego ejecute cd por sí mismo. Debería encontrar que su "prompt" se asemeja a la siguiente.

```
  $
```
 Haga clic dentro de esa ventana de terminal y luego escriba
```
 mkdir hola 
```
Seguido de Enter para hacer un directorio llamado hola en su espacio de código. Ten cuidado de no pasar por alto el espacio entre mkdir y hola o c o cualquier otro carácter!

De aquí en adelante, ejecutar (es decir, correr) un comando significa escribirlo en una ventana de terminal y luego presionar Enter. Los comandos son "sensibles a mayúsculas", así que asegúrate de no escribir en mayúsculas cuando se refiere a  minúsculas o viceversa.
```
 cd hola 
```
Para trasladarse a (es decir, abrir) ese directorio. Su solicitud ahora debe parecerse a la siguiente.

```
 hola/ $
```
Si no es así, ¡vuelve sobre tus pasos y ve si puedes determinar en qué te equivocaste!.

¿Quieres escribir tu primer programa? Ejecuta
```
 code hola.c
```
Para crear un nuevo archivo llamado `hola.c`, que debería abrirse automáticamente en el editor de texto de tu espacio de código. En cuanto guardes el archivo con command-S (en macOS) o control-S (en Windows), también debería aparecer en el explorador de tu espacio de código.

Proceda a escribir su primer programa escribiendo precisamente estas líneas en `hola.c`:
```
 #include <stdio.h>

int main(void)
{
    printf("hola, mundo\n");
}
```
Observe cómo VS Code añade "resaltado de sintaxis" (es decir, color) a medida que escribe, aunque la elección de colores de VS Code puede diferir de la de este conjunto de problemas. Esos colores no se guardan realmente dentro del propio archivo; sólo son añadidos por VS Code para hacer resaltar cierta sintaxis. Si no hubiera guardado el archivo como `hola.c` desde el principio, VS Code no sabría (por la extensión del nombre del archivo) que está escribiendo código C, en cuyo caso esos colores estarían ausentes.

## **Listado de archivos** 
A continuación, en su ventana de terminal, inmediatamente a la derecha del prompt (`hola/$` ), ejecute
```
 ls
```
¿Debería ver sólo `hola.c`? Eso es porque acabas de listar los archivos de tu carpeta `hola`. En concreto, has ejecutado un comando llamado `ls`, que es la abreviatura de "lista". (Es un comando tan frecuentemente utilizado que sus autores lo llamaron simplemente  `ls` para ahorrar pulsaciones de teclado). ¿Tiene sentido?


## **Compilación de programas** 

Ahora, antes de poder ejecutar el programa `hola.c`, recuerda que debemos *compilarlo* con un *compilador*, traduciéndolo de *código fuente* a *código máquina* (es decir, ceros y unos). Ejecuta el siguiente comando para hacerlo:
```
make hola
```
Y luego ejecuta este de nuevo:
```
 ls
```
Esta vez, debería ver no sólo `hola.c` sino también `hola` en la lista? Ahora has traducido el código fuente de `hola.c` a código máquina en `hola`.

Ahora ejecute el programa mismo ejecutando lo siguiente.
```
 ./hola
```
¡Hola, mundo, en efecto!
## **Obtener la información del usuario** 

Obtener la entrada del InputSuffice basta  decir que, no importa cómo compiles o ejecutes este programa, sólo imprime `hola, mundo`. Vamos a personalizarlo un poco, tal y como hicimos en clase.

Modifica este programa de tal manera que primero pregunte al usuario su nombre y luego imprima `hola, fulano`, donde `fulano` es su nombre real.

Como antes, asegúrate de compilar tu programa con:
```
 ./hola
```
## **Recorrido** 
Aquí tienes un "walkthrough" (es decir, un recorrido) de este problema, por si también quieres una visión general de lo que hay que hacer.
[![Alt text](https://img.youtube.com/vi/dF7wNjsRBjI/0.jpg)](https://youtu.be/wSk1KSDUEYA)


## **Consejos** 
#### **¿No recuerdas cómo pedir al usuario su nombre?** 
Recuerda que puedes utilizar `get_string` de la siguiente manera, almacenando su valor de *retorno de variable* llamada `nombre` de tipo `string`.
```
 string nombre = get_string("¿cual es tu nombre?");
```
#### **¿No recuerdas cómo dar formato a una cadena?** 
¿No recuerdas cómo unir (es decir, concatenar) el nombre del usuario con un saludo? Recuerda que puedes utilizar printf no sólo para imprimir sino para formatear una cadena (de ahí la f de printf), como en el caso siguiente, en el que nombre es una cadena.
```
 printf("hola, %s\n", nombre);
```

#### **¿Usar un identificador no declarado?** 
Viendo lo siguiente, ¿tal vez encima de otros errores?
```
 error: use of undeclared identifier 'string'; did you mean 'stdin'? (error: uso de un identificador no declarado 'string'; ¿querías decir 'stdin'?)

```
Recuerda que, para usar `get_string`, necesitas incluir `cs50.h` (en el que se declara `get_string`) encima de un archivo, como con

```
 #include <cs50.h>
```
## **Cómo probar el código** 
Ejecute lo siguiente para evaluar la corrección de su código mediante `check50`, un programa de línea de comandos que mostrará caras felices cuando su código pase las pruebas automatizadas de CS50 y caras tristes cuando no lo haga. Pero asegúrate de compilarlo y probarlo tú mismo.
```
check50 cs50/problems/2022/x/hola
```
Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`, un programa de línea de comandos que mostrará las adiciones (en verde) y las eliminaciones (en rojo) que debería hacer a su programa para mejorar su estilo. Si tienes problemas para ver esos colores, style50 también soporta otros [modos](https://cs50.readthedocs.io/style50/).

```
style50 hola.c
```
## **Cómo presentar** 
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/problems/2022/x/hola
```