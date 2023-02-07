# Crédito
## Empezemos
Abrir  [VS Code](https://code.cs50.io/) 
Comience haciendo clic dentro de la ventana de su terminal, luego ejecute solamente el `cd` . Debería encontrar que su "solicitud" se asemeja a la siguiente.
  
    $
Haga click en esa terminal y ejecute lo siguiente: 

    wget https://cdn.cs50.net/2021/fall/psets/1/credit.zip
Seguido de Enter para descargar un ZIP llamado `credit.zip`  en su espacio de código. Tenga cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter para el caso.
Ahora ejecute 
 
    unzip credit.zip
para crear una carpeta llamada `credit`.  Ya no necesita el archivo ZIP, por lo que puede ejecutar

    rm credit.zip
y responda con "y" seguido de Enter  en el indicador para eliminar el archivo ZIP que descargó.
Ahora escriba 

    cd credit
seguido por Enter para moverse a (es decir, abrir) ese directorio. Su solicitud ahora debe parecerse a la siguiente.

    credit/$
Si todo fue un éxito, debe ejecutar

    ls

y vea un archivo llamado credit.c. Ejecutando code credit. c, debe abrir el archivo donde escribirá su código para este conjunto de problemas. Si no, ¡vuelve sobre tus pasos y ve si puedes determinar dónde te equivocaste!

## Tarjetas de crédito
Una tarjeta de crédito (o de débito), por supuesto, es una tarjeta de plástico con la que se puede pagar por bienes y servicios. Impreso en esa tarjeta se encuentra un número que también se almacena en una base de datos, de modo que cuando su tarjeta se utiliza para comprar algo, el acreedor sabe a quién facturar. En el mundo hay mucha gente con tarjetas de crédito, así que esos números son bastante largos: American Express usa números de 15 dígitos, MasterCard usa números de 16 dígitos, y Visa usa números de 13 y 16 dígitos. Estos son números decimales (0 a 9), no binarios, lo que significa, por ejemplo, que American Express podría imprimir hasta 10^15= ¡1,000,000,000,000,000 tarjetas únicas! (Eso es, um, un cuatrillón.) 
En realidad, eso es un poco exagerado, porque los números de las tarjetas de crédito en realidad tienen cierta estructura para ellos. Todos los números de American Express comienzan con 34 o 37; la mayoría de los números de MasterCard comienzan con 51, 52, 53, 54 o 55 (también tienen algunos otros números de inicio potenciales que no nos preocuparemos por este problema); y todos los números de Visa comienzan con 4. Pero los números de tarjetas de crédito también tienen una "suma de verificación" incorporada en ellos, una relación matemática entre al menos un número y otros. Esa suma de comprobación permite a las computadoras (o a los humanos que les gustan las matemáticas) detectar errores tipográficos (por ejemplo, transposiciones), si no son números fraudulentos, sin tener que consultar una base de datos, lo que puede ser lento. Por supuesto, un matemático deshonesto sin duda podría elaborar un número falso que, sin embargo, respeta la restricción matemática, por lo que una búsqueda de base de datos sigue siendo necesaria para los controles más rigurosos.

## Algoritmo de Luhn
Entonces, ¿cuál es la fórmula secreta? Bueno, la mayoría de las tarjetas utilizan un algoritmo inventado por Hans Peter Luhn de IBM. De acuerdo con el algoritmo de Luhn, puede determinar si un número de tarjeta de crédito es (sintácticamente) válido de la siguiente manera:
1. Multiplica cada dos dígitos por 2, comenzando con el penúltimo dígito del número y luego suma los dígitos de esos productos.
2. Agregue a la suma, la suma de los dígitos que no se multiplicaron por 2.
3. Si el último dígito del total es 0 (o, dicho más formalmente, si el módulo total 10 es congruente con 0), ¡el número es válido!
 
 Eso es un poco confuso, así que vamos a probar un ejemplo con la VISA de David: 4003600000000014.
 1.  Para facilitar la explicación, vamos a resaltar primero una de cada dos cifras, empezando por la penúltima cifra del número:
**4** 0 **0** 3 **6** 0 **0** 0 **0** 0 **0** 0 **0** 0 **1** 4
Okey, ahora multiplicaremos cada digito en negrita por 2:
1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
Eso nos da:
2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
Ahora sumemos los dígitos de esos productos (es decir, no los productos en sí):
2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
4. Ahora sumemos esa suma (13) a la suma de los dígitos que no fueron multiplicados por 2 (empezando por el final):
13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
5. Sí, el último dígito de esa suma (20) es un 0, así que la tarjeta de David es legítima.

Por lo tanto, la validación de los números de las tarjetas de crédito no es difícil, pero resulta un poco tediosa a mano. Así que, vamos a escribir un programa.

## Detalles de la implemetación
Abra el archivo llamado `credit.c`  y  en el directorio `credit`  , escriba un programa que pida al usuario un número de tarjeta de crédito y luego informe (mediante `printf` ) si es un número de tarjeta American Express, MasterCard o Visa válido, según las definiciones del formato de cada una de ellas. Para que podamos automatizar algunas pruebas de su código, le pedimos que la última línea de salida de su programa sea `AMEX\n` o `MASTERCARD\n` o `VISA\n` o `INVALID\n`, y no agregar o quitar nada más. Para simplificar, puede suponer que la entrada del usuario será totalmente numérica (es decir, sin guiones, como podría imprimirse en una tarjeta real) y que no tendrá ceros a la izquierda. Pero no asuma que la entrada del usuario se ajustará a un `int`. Es mejor utilizar `get_long` de la biblioteca de CS50 para obtener la entrada del usuario. (¿Por qué?)

Considere el siguiente ejemplo de cómo debería comportarse su propio programa cuando se le pasa un número de tarjeta de crédito válido (sin guiones).

~~~
$ ./credit
Número:4003600000000014
VISA
~~~
Ahora, el propio `get_long` rechazará los guiones (y más) de todos modos:

~~~
$ ./credit
Número: 4003-6000-0000-0014
Número: foo
Número: 4003600000000014
VISA
~~~
Pero es necesario captar las entradas que no son números de tarjeta de crédito (por ejemplo, un número de teléfono), aunque sean numéricas:
~~~
$ ./credit
Número: 6176292929
INVÁLIDO
~~~
Pruebe su programa con un montón de entradas, tanto válidas como no válidas. (¡Nosotros lo haremos!) Aquí hay [algunos números de tarjetas](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) que PayPal recomienda para las pruebas.

Si su programa se comporta de forma incorrecta con algunas entradas (o no compila en absoluto), ¡es hora de depurar!
## Recorrido
[![Alt text](https://img.youtube.com/vi/dF7wNjsRBjI/0.jpg)](https://www.youtube.com/watch?v=dF7wNjsRBjI)
## Cómo probar su código
También puede ejecutar lo siguiente para evaluar la corrección de su código utilizando  `check50`. Pero asegúrese de compilarlo y probarlo usted mismo.
```
check50 cs50/problems/2022/x/credit
```
Ejecute lo siguiente para evaluar el estilo de su código utilizando `style50`.
```
style50 credit.c
```
## Cómo entregar
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/problems/2022/x/credit
```