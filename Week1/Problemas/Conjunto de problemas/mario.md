# Mario
## Empezemos
#

Abra [Vs Code](https://code.cs50.io/)

Comience haciendo clic dentro de su ventana de terminal, luego ejecute `cd` por sí mismo. Usted debe encontrar que su "indicador" se asemeja a la siguiente.

```
$
```

Haga clic dentro de esa ventana de terminal y luego ejecute

```
wget https://cdn.cs50.net/2021/fall/psets/1/mario-more.zip
```

seguido de Enter para descargar un ZIP llamado `mario-more.zip` en tu espacio de código. Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, ni ningún otro carácter.

Ahora ejecuta

```
unzip mario-more.zip
```

para crear una carpeta llamada `mario-more`. Ya no necesita el archivo ZIP, por lo que puede ejecutar

```
rm mario-more.zip
```

y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba

```
cd mario-more
```

seguido de Enter para entrar en ese directorio (es decir, abrirlo). El indicador debería parecerse al siguiente.

```
mario-more/ $
```

Si todo ha ido bien, deberías ejecutar

```
ls
```

y verás un archivo llamado `mario.c.` Ejecutar el `code mario.c` debería abrir el archivo donde escribirás tu código para este conjunto de problemas. Si no es así, vuelve sobre tus pasos y ve si puedes determinar dónde te equivocaste.

# Mundial 1-1


Hacia el principio del Mundo 1-1 en Super Mario Brothers de Nintendo, Mario debe saltar sobre pirámides de bloques adyacentes, como se indica a continuación.

![Mario, Mundial 1-1](https://cs50.harvard.edu/x/2022/psets/1/mario/more/pyramids.png)

Vamos a recrear esas pirámides en C, aunque en texto, utilizando hashes (`#`) para los ladrillos, a la manera de lo que se muestra a continuación. Cada hash es un poco más alto que ancho, por lo que las pirámides también serán más altas que anchas.

```
   #  #
  ##  ##
 ###  ###
####  ####
```

El programa que escribiremos se llamará `Mario`. Y vamos a permitir que el usuario decida la altura de las pirámides pidiéndole primero un número entero positivo entre, digamos, 1 y 8, ambos inclusive.

Así es como el programa podría funcionar si el usuario introduce `8` cuando se le pide:

```
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

Así es como podría funcionar el programa si el usuario ingresa `4` cuando se le solicita:

```
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Así es como podría funcionar el programa si el usuario ingresa `2` cuando se le solicita:

```
$ ./mario
Height: 2
 #  #
##  ##
```

Y así es como podría funcionar el programa si el usuario ingresa `1` cuando se le solicite:

```
$ ./mario
Height: 1
#  #
```

Si el usuario, de hecho, no ingresa un número entero positivo entre 1 y 8, inclusive, cuando se le solicite, el programa debería volver a preguntarle al usuario hasta que coopere:

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Tenga en cuenta que el ancho de la "brecha" entre las pirámides adyacentes es igual al ancho de dos hashes, independientemente de la altura de las pirámides.

¡ Abra su `mario.c` archivo para implementar este problema como se describe!

## Tutorial
#

[![Alt text](https://img.youtube.com/vi/dF7wNjsRBjI/0.jpg)](https://www.youtube.com/watch?v=FzN9RAjYG_Q)

### Cómo probar su código

¿Funciona su código como se indica cuando introduce

■ `-1`(u otros números negativos)?

■ `0`?

■ `1` a través de `8`?

■ `9` u otros números positivos?

■ letras o palabras?

■ ninguna entrada en absoluto, cuando solo presiona Enter?

También puede ejecutar lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!

```
check50 cs50/problems/2022/x/mario/more
```

Ejecute lo siguiente para evaluar el estilo de su código usando style50.

```
style50 mario.c
```

# Cómo presentarse

En su terminal, ejecute lo siguiente para enviar su trabajo.

```
submit50 cs50/problems/2022/x/mario/more
```