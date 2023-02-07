# Mario
![](/Conjunto_Problemas_6/Problemas_6_Markdown/Mario2.png)\
Implemente un programa que imprima una media pirámide doble de una altura específica, según se indica a continuación.
```
$ ./mario
Altura: 4
   #  #
  ##  ##
 ###  ###
####  ####
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente:
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-mario-more.zip
```
para descargar un ZIP llamado ```sentimental-mario-more.zip``` en su espacio de códigos.
Luego ejecuta
```
unzip sentimental-mario-more.zip
```
para crear una carpeta llamada ```sentimental-mario-more```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-mario-more.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.
Ahora escriba
```
cd sentimental-mario-more
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-mario-more/ $
```
Ejecute ```ls``` solo y debería ver ```mario.py```. Si se encuentra con algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde salió mal.
## Especificación
* Escriba, en un archivo llamado ```mario.py```, un programa que recree estas medias pirámides usando hashes (```#```) para bloques, exactamente como lo hizo en el Conjunto de problemas 1, excepto que su programa esta vez debe estar escrito en Python.
* Para hacer las cosas más interesantes, primero solicite al usuario ```get_int``` la altura de la media pirámide, un número entero positivo entre ```1``` y ```8```. (La altura de las medias pirámides que se muestran arriba es ```4```, el ancho de cada media pirámide ```4```, con un espacio de tamaño ```2``` que las separa).
* Si el usuario no proporciona un número entero positivo que no sea mayor que ```8```, debe volver a solicitar lo mismo nuevamente.
* Luego, genera (con la ayuda de ```print``` y uno o más bucles) las medias pirámides deseadas. 
* Tenga cuidado de alinear la esquina inferior izquierda de su pirámide con el borde izquierdo de la ventana de su terminal y asegúrese de que haya dos espacios entre las dos pirámides y que no haya espacios adicionales después del último conjunto de hash en cada uno. fila.
## Uso
Su programa debe comportarse según el ejemplo a continuación.
```
$ ./mario
Altura: 4
   #  #
  ##  ##
 ###  ###
####  ####
```
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```-1``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```0``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```1``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
#  #
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```2``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
 #  #
##  ##
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```8``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```9``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número. Luego, escribe ```2``` y presiona enter. Su programa debería generar el siguiente resultado. Asegúrese de que la pirámide esté alineada con la esquina inferior izquierda de su terminal y que no haya espacios adicionales al final de cada línea.
```
 #  #
##  ##
```
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. Escribe ```foo``` y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python mario.py``` y espere a que se le solicite la entrada. No escribas nada y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo también!
```
check50 cs50/problems/2022/x/sentimental/mario/more
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 mario.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/mario/more
```