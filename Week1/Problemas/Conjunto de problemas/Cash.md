# Cash

- ¿Hiciste la versión anterior de este problema?
  - La versión de Cash de CS50x 2022 es bastante diferente a la versión de CS50x 2021. Te convendrá hacer este problema desde cero. La versión del año pasado no se compilará cuando sea verificada por `check50` debido al hecho de que en esta nueva versión, usted debe implementar funciones que el conjunto de pruebas probará de forma independiente, más allá de simplemente verificar la respuesta final (como lo hizo la versión del año pasado).

## Comenzando

---


Abre [VS Code](https://code.cs50.io/ "VS Code").  
Comienza haciendo clic dentro de la ventana de la terminal, luego ejecuta `cd`. Deberías encontrar que el "indicador" se parece al siguiente:

```
$
```

Haz clic dentro de esa ventana de la terminal y luego ejecuta

```
wget https://cdn.cs50.net/2021/fall/psets/1/cash.zip
```

Luego, presiona Enter para descargar un ZIP llamado `cash.zip`.  
¡Ten cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter para el caso!.  
Ahora ejecuta:

```
unzip cash.zip
```

Para crear una carpeta llamada `cash`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

```
rm cash.zip
```

Después, responde con _"y"_, luego presiona Enter en el aviso para eliminar el archivo ZIP que se descargó.  
Ahora escribe:

```
cd cash
```

Luego presiona Enter para entrar (abrir) ese directorio. El mensaje ahora debería ser similar al siguiente.

```
cash/ $
```

Si todo salio exitosamente, debes ejecutar

```
ls
```

Y poder ver un archivo llamado `cash.c`. Ejecutar `code cash.c` debería abrir el archivo donde escribiras tu código para este conjunto de problemas. De lo contrario, regresa a los anteriores pasos y observa si puedes determinar dónde te equivocaste.

## Algoritmos codiciosos

---

![Alt text](https://cs50.harvard.edu/x/2022/psets/1/cash/coins.jpg)

Al realizar cambios, lo más probable es que deseas minimizar la cantidad de monedas que entregas a cada cliente, para que no se acaben (¡o eso moleste al cliente!). Afortunadamente, la informática ha proporcionado a los cajeros de todo el mundo formas de minimizar el número de monedas adeudadas: algoritmos codiciosos.

Según el Instituto Nacional de Estándares y Tecnología (NIST), un algoritmo codicioso es uno “que siempre toma la mejor solución inmediata o local mientras encuentra una respuesta. Los algoritmos codiciosos encuentran la solución óptima general o global para algunos problemas de optimización, pero pueden encontrar soluciones menos que óptimas para algunos casos de otros problemas”.

¿Qué significa todo eso? Bueno, supongamos que un cajero le debe a un cliente algo de cambio y en el cajón de ese cajero hay veinticinco centavos (25 centavos), diez centavos (10 centavos), cinco centavos (5 centavos) y un centavo (1 centavo). El problema a resolver es decidir qué monedas y cuántas de cada una entregar al cliente. Piense en un cajero "codicioso" como alguien que quiere sacar el mayor provecho posible de este problema con cada moneda que saca del cajón. Por ejemplo, si a un cliente se le deben 41¢, la primera opción más grande (es decir, la mejor opción inmediata) que se puede tomar es 25¢. (Esa opción es "mejor" en la medida en que nos acerca a 0¢ más rápido que cualquier otra moneda). Tenga en cuenta que una opción de este tamaño reduciría lo que era un problema de 41¢ a un problema de 16¢, ya que 41 - 25 = 16. Es decir, el resto es un problema similar pero más pequeño. No hace falta decir que otra moneda de 25 centavos sería demasiado grande (suponiendo que el cajero prefiera no perder dinero), por lo que nuestro cajero codicioso pasaría a elegir una moneda de 10 centavos, dejándolo con un problema de 6 centavos. En ese punto, la codicia exige una moneda de 5¢ seguido de otra moneda de 1¢, y en ese momento el problema se resuelve. El cliente recibe una moneda de veinticinco centavos, una moneda de diez centavos, una moneda de cinco centavos y un centavo: cuatro monedas en total.

Resulta que este enfoque codicioso (es decir, el algoritmo) no solo es óptimo a nivel local sino también globalmente para la moneda de Estados Unidos (y también la de la Unión Europea). Es decir, siempre que un cajero tenga suficiente de cada moneda, este enfoque de mayor a menor producirá la menor cantidad de monedas posible.

## Detalles de implementación

---

En `cash.c`, hemos implementado la mayor parte (pero no toda) de un programa que solicita al usuario la cantidad de centavos que se le debe a un cliente y luego imprime la menor cantidad de monedas con las que se puede hacer ese cambio. De hecho, `main` ya está implementado para ti. ¡Pero observa cómo `main` llama a varias funciones que aún no están implementadas! Una de esas funciones, `get_cents`, no acepta argumentos (como lo indica `void`) y devuelve un `int`. El resto de las funciones toman un argumento, un `int`, y también devuelven un `int`. Todos ellos actualmente devuelven `0` para que el código se compile. Pero querrás reemplazar cada `TODO` y `retornar 0`; con tu propio código. Específicamente, completa la implementación de esas funciones de la siguiente manera:

- Implementa `get_cents` de tal manera que la función solicite al usuario una cantidad de centavos usando `get_int` y luego devuelva ese número como un `int`. Si el usuario ingresa un `int` negativo, su código debería solicitar al usuario nuevamente. (Pero no necesita preocuparse de que el usuario ingrese, por ejemplo, un `string` (una cadena), ya que `get_int` se encargará de eso por usted). ¡Lo más probable es que encuentres a un bucle `do while` de mucha ayuda, como en `mario.c`!

- Implemente `calcular_veinticinco` de tal manera que la función calcule (y retorne como un `int`) cuántas monedas de veinticinco se le deben dar a un cliente si se le debe una cierta cantidad de centavos. Por ejemplo, si `centavos` es `25`, entonces `calcular_veinticinco` debería devolver `1`. Si `centavos` es `26` o `49` (o cualquier valor intermedio, `calcular_veinticinco` también debería retornar `1`. Si centavos es `50` o `74` (o cualquier valor intermedio), entonces `calcular_cuartos` debería devolver `2`. Y así sucesivamente.
- Implemente `calcular_diez` de tal manera que la función calcule lo mismo para las monedas de diez centavos.
- Implemente `calcule_cinco` de tal manera que la función calcule lo mismo para las monedas de cinco centavos.
- Implemente `calcule_uno` de tal manera que la función calcule lo mismo para monedas de un centavo.

Ten en cuenta que, a diferencia de las funciones que solo tienen efectos secundarios, las funciones que devuelven un valor deben hacerlo explícitamente con `retorno`. ¡Ten cuidado de no modificar el código de distribución en sí, solo reemplaza los `TODO` dados y el valor de `retorno` posterior!
Ten en cuenta también que, recordando la idea de abstracción, cada una de sus funciones de cálculo debe aceptar cualquier valor de `centavos`, no solo los valores que el algoritmo codicioso podría sugerir. Si `centavos` es 85, por ejemplo, `calcular_diez` debería devolver 8.

- Pista:
  - Recuerda que hay varios programas de muestra en el código fuente de la semana 1 que ilustran cómo las funciones pueden devolver un valor. Puedes encontrar discount1.c y discount2.c interesantes.

Tu programa debe comportarse según los ejemplos a continuación.

```
$ ./cash
Cambio: 41
4
```

```
$ ./cash
Cambio: -41
Cambio: foo
Cambio: 41
4
```

### **Como poner a prueba tu código**

Para este programa, intenta probar tu código manualmente; es una buena práctica:

- Si ingresas -1, ¿tu programa le pregunta de nuevo?
- Si ingresas 0, ¿tu programa genera 0?
- Si ingresas 1, ¿tu programa genera 1 (es decir, un centavo)?
- Si ingresas 4, ¿tu programa genera 4 (es decir, cuatro centavos)?
- Si ingresas 5, ¿tu programa genera 1 (es decir, una moneda de cinco centavos)?
- Si ingresas 24, ¿tu programa genera 6 (es decir, dos monedas de diez centavos y cuatro monedas de un centavo)?
- Si ingresas 25, ¿tu programa genera 1 (es decir, una moneda de veinticinco centavos)?
- Si ingresas 26, ¿tu programa genera 2 (es decir, una moneda de veinticinco centavos y un centavo)?
- Si ingresas 99, ¿tu programa genera 9 (es decir, tres monedas de veinticinco centavos, dos centavos y cuatro centavos)?

También puedes ejecutar lo siguiente para evaluar la corrección de su código usando `check50`. ¡Pero asegurate de compilarlo y probarlo tu mismo también!

```
check50 cs50/problems/2022/x/cash
```

- ¿Check50 no puede compilar su código?
  - La versión de Cash de CS50x 2022 es bastante diferente a la versión de CS50x 2021. La versión del año pasado no se compilará cuando sea verificada por `check50` (pero no necesariamente si la ejecuta usted mismo, asumiendo que su archivo consiste en un código C legal) debido al hecho de que en esta nueva versión debe implementar cinco funciones que probará el conjunto de pruebas de forma independiente, más allá de simplemente verificar la respuesta final (como lo hizo la versión del año pasado).

Y ejecuta lo siguiente para evaluar el estilo de tu código usando `style50`.

```
style50 cash.c
```

## Como subirlo

---

En tu terminal, ejecuta lo siguiente para subir tu trabajo:

```
submit50 cs50/problems/2022/x/cash
```
