# Lab 6: Copa Mundial

Le invitamos a colaborar con uno o dos compañeros de clase en este laboratorio, aunque se espera que todos los estudiantes contribuyan por igual al laboratorio.

Escriba un programa para correr simulaciones de la Copa Mundial de la FIFA.
```
$ python torneo.py 2018m.csv
Belgica: 20.9% oportunidad de ganar
Brasil: 20.3% oportunidad de ganar
Portugal: 14.5% oportunidad de ganar
España: 13.6% oportunidad de ganar
Suiza: 10.5% oportunidad de ganar
Argentina: 6.5% oportunidad de ganar
Inglaterra: 3.7% oportunidad de ganar
Francia: 3.3% oportunidad de ganar
Dinamarca: 2.2% oportunidad de ganar
Croacia: 2.0% oportunidad de ganar
Colombia: 1.8% oportunidad de ganar
Suecia: 0.5% oportunidad de ganar
Uruguay: 0.1% oportunidad de ganar
Mexico: 0.1% oportunidad de ganar
```
# Fondo
En la Copa del Mundo de fútbol, ​​la ronda eliminatoria consta de 16 equipos. En cada ronda, cada equipo juega contra otro equipo y los equipos perdedores son eliminados. Cuando solo quedan dos equipos, el ganador del partido final es el campeón.

En el fútbol, los equipos reciben [clasificaciones de la FIFA](https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking#Current_calculation_method), que son valores numéricos que representan el nivel de habilidad relativo de cada equipo. Las clasificaciones de FIFA más altas indican mejores resultados de juegos anteriores, y dadas las clasificaciones de FIFA de dos equipos, es posible estimar la probabilidad de que cualquiera de los equipos gane un juego en función de sus clasificaciones actuales. Las clasificaciones de la FIFA de dos Copas Mundiales anteriores están disponibles como las [clasificaciones de la FIFA para hombres de mayo de 2018](https://www.fifa.com/fifa-world-ranking/men?dateId=id13750) y las [clasificaciones de la FIFA para mujeres de marzo de 2019](https://www.fifa.com/fifa-world-ranking/women?dateId=ranking_20220805).

Usando esta información, podemos simular todo el torneo simulando repetidamente rondas hasta que nos quedemos con un solo equipo. Y si queremos estimar la probabilidad de que cualquier equipo gane el torneo, podemos simular el torneo muchas veces (por ejemplo, 1000 simulaciones) y contar cuántas veces gana cada equipo un torneo simulado.

¡Su tarea en este laboratorio es hacer exactamente eso usando Python!

# Empezando

Abra [VS Code](https://code.cs50.io)

Comience haciendo clic dentro de la ventana de su terminal, luego ejecute `cd` por sí mismo. Debería encontrar que su "indicador" se parece al siguiente.
```
$
```
Haga clic dentro de esa ventana de terminal y luego ejecute
```
wget https://cdn.cs50.net/2021/fall/labs/6/world-cup.zip
```
seguido de Enter para descargar un ZIP llamado `copa-mundial.zip` en su espacio de código. ¡Tenga cuidado de no pasar por alto el espacio entre `wget` y la siguiente URL, o cualquier otro carácter para el caso!

Ahora ejecuta
```
unzip copa-mundial.zip
```
para crear una carpeta llamada `copa-mundial`. Ya no necesita el archivo ZIP, por lo que puede ejecutar
```
rm copa-mundial.zip
```
y responda con "y" seguido de Enter en el aviso para eliminar el archivo ZIP que descargó.

Ahora escriba
```
cd copa-mundial
```
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al siguiente.
```
copa-mundo/ $
```
Si todo fue exitoso, debe ejecutar
```
ls
```
y debería ver los siguientes archivos:
```
2018m.csv 2019w.csv torneo.py
```
Si tiene algún problema, siga estos mismos pasos nuevamente y vea si puede determinar dónde se equivocó.

# Comprensión
Comience echando un vistazo al `archivo 2018m.csv`. Este archivo contiene los 16 equipos en la ronda eliminatoria de la Copa Mundial Masculina 2018 y las calificaciones de cada equipo. Observe que el archivo CSV tiene dos columnas, una llamada `equipo` (que representa el nombre del país del equipo) y otra llamada `clasificación` (que representa la clasificación del equipo).

El orden en que se enumeran los equipos determina qué equipos jugarán entre sí en cada ronda (en la primera ronda, por ejemplo, Uruguay jugará contra Portugal y Francia jugará contra Argentina; en la siguiente ronda, el ganador del partido Uruguay-Portugal jugará el ganador del partido Francia-Argentina). ¡Así que asegúrese de no editar el orden en que aparecen los equipos en este archivo!

En última instancia, en Python podemos representar cada equipo como un diccionario que contiene dos valores: el nombre del equipo y la calificación. Uruguguay, por ejemplo lo querremos representar en Python como `{"equipo": "Uruguay", "calificación": 976}`.

A continuación, eche un vistazo a `2019w.csv`, que contiene datos con el mismo formato para la Copa Mundial Femenina de 2019.

Ahora, abre `torneo.py` y verás que ya hemos escrito algo de código para ti. La variable `N` en la parte superior representa cuántas simulaciones de la Copa Mundial ejecutar: en este caso, 1000.

La función `simular_juego` acepta dos equipos como entradas (recuerde que cada equipo es un diccionario que contiene el nombre del equipo y la calificación del equipo) y simula un juego entre ellos. Si gana el primer equipo, la función devuelve `True`; de lo contrario, la función devuelve `False`.

La función de `simular_ronda` acepta una lista de equipos (en una variable llamada `equipos`) como entrada y simula juegos entre cada par de equipos. Luego, la función devuelve una lista de todos los equipos que ganaron la ronda.

En la función `main`, observe que primero nos aseguramos de que `len(sys.argv)` (la cantidad de argumentos de la línea de comandos) sea 2. Usaremos los argumentos de la línea de comandos para decirle a Python qué archivo CSV del equipo usar para ejecutar el torneo. simulación. Luego definimos una lista llamada `equipos` (que eventualmente será una lista de equipos) y un diccionario llamado `contador` (que asociará los nombres de los equipos con la cantidad de veces que ese equipo ganó un torneo simulado). En este momento, ambos están vacíos, ¡así que llenarlos depende de usted!

Finalmente, al final del `main`, clasificamos los equipos en orden descendente de cuántas veces ganaron las simulaciones (según `contador`) e imprimimos la probabilidad estimada de que cada equipo gane la Copa del Mundo.

¡Poblar `equipos` y `contador` y escribir la función simular_torneo depende de ti!

# Detalles de la implementación
Complete la implementación de `torneo.py`, de modo que simule una cantidad de torneos y genere la probabilidad de ganar de cada equipo.

Primero, en el `main`, lea los datos del equipo del archivo CSV en la memoria de su programa y agregue cada equipo a la lista de `equipos`.

* El archivo a utilizar se proporcionará como un argumento de línea de comandos. Puede acceder al nombre del archivo, entonces, con `sys.argv[1]`.
* Recuerde que puede abrir un archivo con `open(filename)`, donde `filename` es una variable que almacena el nombre del archivo.
* Una vez que tenga un archivo f, puede usar `csv.DictReader(f)` para obtener un "lector": un objeto en Python que puede recorrer para leer el archivo una fila a la vez, tratando cada fila como un diccionario.
* De forma predeterminada, todos los valores leídos del archivo serán cadenas. Así que asegúrese de convertir primero la `calificación` del equipo a un `int` (puede usar la función `int` en Python para hacer esto).
* En última instancia, agregue el diccionario de cada equipo a los `equipos`. La llamada a la función `teams.append(x)` agregará `x` a la lista de `equipos`.
* Recuerde que cada equipo debe ser un diccionario con un nombre de `equipo` y una `calificación`.

A continuación, implemente la función `simular_torneo`. Esta función debería aceptar como entrada una lista de equipos y debería simular rondas repetidamente hasta que te quedes con un equipo. La función debería devolver el nombre de ese equipo.

* Puede llamar a la función `simular_ronda`, que simula una sola ronda, acepta una lista de equipos como entrada y devuelve una lista de todos los ganadores.
* Recuerda que si `x` es una lista, puedes usar `len(x)` para determinar la longitud de la lista.
* No debe suponer el número de equipos en el torneo, pero puede suponer que será una potencia de 2.

Finalmente, regrese a la función `main`, ejecute `N` simulaciones de torneos y realice un seguimiento de cuántas veces gana cada equipo en el diccionario de `contador`.

* Por ejemplo, si Uruguay ganó 2 torneos y Portugal ganó 3 torneos, entonces su diccionario de `contador` debería ser `{"Uruguay": 2, "Portugal": 3}`.
* Debe usar su `simulación_torneo` para simular cada torneo y determinar el ganador.
* Recuerde que si `contador` es un diccionario, entonces una sintaxis como `contador[equipo_nombre] = x` asociará la clave almacenada en `team_name` con el valor almacenado en `x`.
* Puede usar la palabra clave `in` en Python para verificar si un diccionario ya tiene una clave en particular. Por ejemplo, `if "Portugal" in contador:` comprobará si `"Portugal"` ya tiene un valor existente en el diccionario de `contador`.

# Consejos

* Cuando lea el archivo, puede encontrar útil esta sintaxis, con ```nombrearchivo``` como el nombre de su archivo y ```archivo``` como una variable.

``` python
with abre(nombrearchivo) as archivo
    lector = csv.DictReader(archivo)
```
* En Python, para agregar al final de una lista, use la función ```.append()```

# Pruebas

* Su programa debería comportarse de acuerdo con los ejemplos a continuación. Dado que las simulaciones tienen aleatoriedad dentro de cada una, es probable que su salida no coincida perfectamente con los ejemplos a continuación.
```
$ python torneo.py 2018m.csv
Bélgica: 20.9% probabilidad de ganar
Brasil: 20.3% probabilidad de ganar
Portugal: 14.5% probabilidad de ganar
España: 13.6% probabilidad de ganar
Suiza: 10.5% probabilidad de ganar
Argentina: 6.5% probabilidad de ganar
Inglaterra: 3.7% probabilidad de ganar
Francia: 3.3% probabilidad de ganar
Dinamarca: 2.2% probabilidad de ganar
Croacia: 2.0% probabilidad de ganar
Colombia: 1.8% probabilidad de ganar
Suecia: 0.5% probabilidad de ganar
Uruguay: 0.1% probabilidad de ganar
México: 0.1% probabilidad de ganar
```
```
$ python torneo.py 2019m.csv
Alemania: 17.1% probabilidad de ganar
Estados Unidos: 14.8% probabilidad de ganar
Inglaterra: 14.0% probabilidad de ganar
Francia: 9.2% probabilidad de ganar
Canada: 8.5% probabilidad de ganar
Japon: 7.1% probabilidad de ganar
Australia: 6.8% probabilidad de ganar
Países Bajos: 5.4% probabilidad de ganar
Suecia: 3.9% probabilidad de ganar
Italia: 3.0% probabilidad de ganar
Noruega: 2.9% probabilidad de ganar
Brasil: 2.9% probabilidad de ganar
España: 2.2% probabilidad de ganar
RP China: 2.1% probabilidad de ganar
Nigeria: 0.1% probabilidad de ganar
```
* ¡Quizás se pregunte qué sucedió realmente en las Copas Mundiales de 2018 y 2019! Para los hombres, ganó Francia, derrotando a Croacia en la final. Bélgica derrotó a Inglaterra por el tercer lugar. Para las mujeres, Estados Unidos ganó, derrotando a Holanda en la final. Inglaterra derrotó a Suecia por el tercer puesto.

# Cómo probar su código

Ejecute lo siguiente para evaluar la corrección de su código usando ```check50``` .¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/labs/2022/x/copa mundial
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
torneo style50.py
```

# Cómo enviar
Cómo enviar
En su terminal, ejecute lo que se indica a continuación para enviar su trabajo.
```
enviar50 cs50/labs/2022/x/copa mundial
```