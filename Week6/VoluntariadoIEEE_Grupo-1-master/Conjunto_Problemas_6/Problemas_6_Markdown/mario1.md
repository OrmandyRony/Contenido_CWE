# Mario
![](/Conjunto_Problemas_6/Problemas_6_Markdown/Mario1.png)\
Implemente un programa que imprima una media pirámide de una altura específica, según se indica a continuación.
```
$ ./mario
Altura: 4
   #
  ##
 ###
####
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el mensaje de su ventana de terminal se parece al siguiente:
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-mario-less.zip
```
para descargar un ZIP llamado sentimental-mario-less.zip en su espacio de código.
Luego ejecuta
```
unzip sentimental-mario-less.zip
```
para crear una carpeta llamada ```sentimental-mario-less```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-mario-less.zip
```
y responda con "y" seguido de Enter cuando se le indique que elimine el archivo ZIP que descargó.
Ahora escriba
```
cd sentimental-mario-less
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-mario-less/ $
```
Ejecute ```ls``` solo y debería ver un ```mario.py```. Si se encuentra con algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde salió mal.
## Especificación
* Escriba, en un archivo llamado ```mario.py```, un programa que recree la media pirámide usando hashes (```#```) para bloques, exactamente como lo hizo en el Conjunto de problemas 1, excepto que su programa esta vez debe estar escrito en Python.
* Para hacer las cosas más interesantes, primero solicite al usuario ```get_int``` la altura de la media pirámide, un número entero positivo entre ```1``` y ```8```.
* Si el usuario no proporciona un número entero positivo no superior a ```8```, debe volver a solicitar lo mismo.
* Luego, genere (con la ayuda de ```print```  y uno o más bucles) la media pirámide deseada.
* Tenga cuidado de alinear la esquina inferior izquierda de su media pirámide con el borde izquierdo de la ventana de su terminal.
## Uso
Su programa debe comportarse según el siguiente ejemplo.
```
$ ./mario
Altura: 4
   #
  ##
 ###
####
```
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python mario.py``` y espere  a que se le solicite la entrada. Escribe ```-1``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python mario.py ``` y espere a que se le solicite la entrada. Escribe  ```0 ``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
*  Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```1``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
#
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```2``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
 #
##
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```8``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
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
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```9``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número. Luego, escribe ```2``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
 #
##
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```foo``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. No escribas nada y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
Ejecute lo siguiente para evaluar la exactitud de su código utilizando ```check50```. ¡Pero asegúrese de compilarlo y probarlo también!
```
check50 cs50/problems/2022/x/sentimental/mario/less
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 mario.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/mario/less
```