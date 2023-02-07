# Credito
Implemente un programa que determine si un número de tarjeta de crédito proporcionado es válido según el algoritmo de Luhn.
```
$ python credit.py
Número: 378282246310005
AMEX
```
## Empezando
Inicie sesión en [code.cs50.io](https://code.cs50.io), haga clic en la ventana de su terminal y ejecute cd por sí mismo. Debería encontrar que el mensaje de su ventana de terminal se parece al siguiente:
```
$
```
Siguiente ejecución
```
wget https://cdn.cs50.net/2021/fall/psets/6/sentimental-credit.zip
```
para descargar un ZIP llamado ```sentimental-credit.zip``` en su espacio de código.
Luego ejecuta
```
unzip sentimental-credit.zip
```
para crear una carpeta llamada ```sentimental-credit```. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm sentimental-credit.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.
Ahora escribe
```
cd sentimental-credit
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
sentimental-credit/ $
```
Ejecute ```ls``` por sí mismo y debería ver ```credit.py```. Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.
## Especificación
* En ```credit.py```, escriba un programa que solicite al usuario un número de tarjeta de crédito y luego informe (por medio de ```print```) si es un número de tarjeta American Express, MasterCard o Visa válido, exactamente como lo hizo en el Grupo de problemas 1, excepto que su programa esta vez debe estar escrito en Python.
* Para que podamos automatizar algunas pruebas de su código, solicitamos que la última línea de salida de su programa sea ```AMEX\n``` o ```MASTERCARD\n``` o ```VISA\n``` o ```INVALID\n```, nada más, nada menos.
* Para simplificar, puede asumir que la entrada del usuario será totalmente numérica (es decir, sin guiones, como podría estar impreso en una tarjeta real).
* Es mejor usar ```get_int``` o ```get_string``` de la biblioteca de CS50 para obtener la entrada de los usuarios, dependiendo de cómo decida implementar este.
## Uso
Su programa debe comportarse según el siguiente ejemplo.
```
$ python credit.py
Numero: 378282246310005
AMEX
```
## Sugerencias
* Es posible utilizar expresiones regulares para validar las entradas del usuario. Podrías usar el módulo 
[re](https://docs.python.org/3/library/re.html) de Python, por ejemplo, para comprobar si la entrada del usuario es realmente una secuencia de dígitos de la longitud correcta.
## Pruebas
Si bien ```check50``` está disponible para este problema, le recomendamos que primero pruebe su código por su cuenta para cada uno de los siguientes.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Ingrese ```378282246310005``` y presione enter. Su programa debe dar como resultado ```AMEX```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Ingrese ```371449635398431``` y presione enter. Su programa debe dar como resultado ```AMEX```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Ingrese ```5555555555554444``` y presione enter. Su programa debería mostrar ```MASTERCARD```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Ingrese ```5105105105105100``` y presione enter. Su programa debería mostrar ```MASTERCARD```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Escriba ```4111111111111111``` y presione enter. Su programa debe dar como resultado ```VISA```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Escriba ```4012888888881881``` y presione enter. Su programa debe dar como resultado ```VISA```.
* Ejecute su programa como ```python credit.py``` y espere a que se le solicite la entrada. Escriba ```1234567890``` y presione enter. Su programa debe mostrar ```INVALID```.
Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/problems/2022/x/sentimental/credit
```
Ejecute lo siguiente para evaluar el estilo de su código utilizando ```style50```.
```
style50 credit.py
```
## Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
submit50 cs50/problems/2022/x/sentimental/credit
```