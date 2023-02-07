# Efectivo
Implementar un programa que calcule la cantidad mínima de monedas requeridas para dar cambio a un usuario.
```
$ python cash.py
Cambio debido: 0.41
4
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute ```cd``` por sí mismo. Debería encontrar que el mensaje de su ventana de terminal se parece al siguiente:
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-cash.zip
```
para descargar un ZIP llamado ```sentimental-cash.zip``` en su espacio de código.
Luego ejecuta
```
unzip sentimental-cash.zip
```
para crear una carpeta llamada ```sentimental-cash```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-cash.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.
Ahora escriba
```
cd sentimental-cash
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-cash/ $
```
Ejecute ```ls``` por sí mismo y debería ver ```cash.py```. Si se encuentra con algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde salió mal.
## Especificación
* Escribir, en un archivo llamado ```cash.py```, un programa que primero pregunte al usuario cuanto se debe de cambio y luego escupe la cantidad mínima de monedas con las que se puede realizar dicho cambio. Puede hacer esto exactamente como lo hizo en el Conjunto de problemas 1, excepto que su programa esta vez debe estar escrito en Python, y debe asumir que el usuario ingresará su cambio en dólares (por ejemplo, 0,50 dólares en lugar de 50 centavos).
* Utilice ```get_float``` de la biblioteca CS50 para obtener la entrada del usuario e ```imprimir``` para generar su respuesta. Suponga que las únicas monedas disponibles son veinticinco centavos (25 centavos), diez centavos (10 centavos), cinco centavos (5 centavos) y centavos (1 centavo).
     *   Le pedimos que utilice ```get_float``` para poder manejar dólares y centavos, aunque sin el signo de dólar. En otras palabras, si a algún cliente se le debe $9.75 (como en el caso en que un periódico cuesta 25¢ pero el cliente paga con un billete de $10), suponga que la entrada de su programa será ```9.75``` y no ```$9.75``` o ```975```. Sin embargo, si algún cliente se le deben $9 exactamente, asuma que la entrada de su programa será ```9.00``` o solo ```9``` pero, de nuevo, no ```$9``` o ```900```. Por supuesto, por la naturaleza de los valores de punto flotante, su programa probablemente también funcionará con entradas como ```9.0``` y ```9.000```; no debe preocuparse por verificar si la entrada del usuario tiene el "formato" como debería ser el dinero.
* Si el usuario no proporciona un valor no negativo, su programa debe volver a solicitar al usuario una cantidad válida una y otra vez hasta que el usuario cumpla.
* Por cierto, para que podamos automatizar algunas pruebas de su código, le pedimos que la última línea de salida de su programa sea solo la cantidad mínima de monedas posible: un número entero seguido de una nueva línea.
## Uso
Su programa debe comportarse según el siguiente ejemplo.
```
$ python cash.py
Cambio debido: 0.41
4
```
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```0.41``` y presione enter. Su programa debe dar como resultado ```4```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```0.01``` y presione Entrar. Su programa debe dar como resultado ```1```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```0.15``` y presione enter. Su programa debe dar como resultado ```2```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```1.60``` y presione enter. Su programa debe dar como resultado ```7```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```23``` y presione Entrar. Su programa debe dar como resultado ```92```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```4.2``` y presione Entrar. Su programa debe dar como resultado ```18```.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```-1``` y presione Entrar. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. Escriba ```foo``` y pulse enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
* Ejecute su programa como ```python cash.py``` y espere a que se le solicite una entrada. No escribas nada y presiona enter. Su programa debería rechazar esta entrada como inválida, pidiéndole al usuario que escriba otro número.
Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/sentimental/cash
```
Ejecute lo siguiente para evaluar el estilo de su código utilizando ```style50```.
```
style50 cash.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/cash
```