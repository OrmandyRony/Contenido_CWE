# Hola
Implemente un programa que imprima un saludo simple para el usuario, según se indica a continuación.
```
$ python hola.py
¿Cuál es su nombre?
David
Hola David
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el indicador de la ventana de su terminal se parece al siguiente:
```
$ 
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-hello.zip
```
para descargar un ZIP llamado ```sentimental-hello.zip``` en su espacio de código.
Luego ejecuta
```
unzip sentimental-hello.zip
```
para crear una carpeta llamada ```sentimental-hello```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-hello.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escribe
```
cd sentimental-hello
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-hello/ $
```
Ejecute ```ls``` por sí mismo y debería ver ```hello.py```. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.
## Especificación
Escriba, en un archivo llamado ```hello.py```, un programa que solicite al usuario su nombre y luego imprima hola, fulano de tal, donde fulano de tal es su nombre proporcionado, exactamente como lo hizo en el Conjunto de problemas 1. , excepto que su programa esta vez debe estar escrito en Python.
## Uso
Su programa debe comportarse según el siguiente ejemplo.
```
$ python hola.py
¿Cuál es su nombre?
Emma
hola Emma
```
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python hola.py```, y espere un mensaje de entrada. Escriba ```David``` y presione enter. Su programa deberia mostrar ```hola, David```.
* Ejecute su programa como ```python hola.py```, y espere un mensaje de entrada. Escriba ```Bernie``` y presione enter. Su programa deberia mostrar ```hola, Bernie```.
* Ejecute su programa como ```python hola.py```, y espere un mensaje de entrada. Escriba ```Carter``` y presione enter. Su programa deberia mostrar ```hola, Carter```.
Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/sentimental/hello
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 hello.py
```
## Cómo enviar
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/hello
```