# Lectura 7

*   Procesamiento de datos

*   Limpieza
*   Conteo

*   Bases de datos relacionadas

*   SQL
*   Tablas

*   SQL con Python
*   IMDb
*   Problemas

## Procesamiento de datos

*   La semana pasada, recopilamos una encuesta sobre las preferencias de la casa de Hogwarts y recopilamos los datos de un archivo CSV con Python.

*   Esta semana recopilaremos algunos datos más sobre tus programas de TV favoritos y sus géneros.

*   Recibimos cientos de respuestas de la audiencia y comenzamos a mirarlas en Hojas de cálculo de Google, una aplicación de hoja de cálculo basada en la web, que muestra nuestros datos en filas y columnas: ![hola](https://cs50.harvard.edu/x/2022/notes/7/favorites.png)

*   Como hicimos la semana pasada, podemos descargar nuestros datos como un archivo CSV, que es un ejemplo de una base de datos de archivo plano, donde los datos de cada columna están separados por comas y cada fila está en una nueva línea, guardada simplemente como un archivo de texto en ASCII o Unicode.

*   Una base de datos de archivo plano es completamente portátil, lo que significa que podemos abrirla en casi cualquier sistema operativo sin software especial como Microsoft Excel o Apple Numbers.

*   Subiremos el archivo CSV a nuestra instancia de VS Code arrastrándolo y soltándolo: ![hola1](https://cs50.harvard.edu/x/2022/notes/7/uploading.png)

*   Luego, veremos el archivo abierto en un editor: ![hola2](https://cs50.harvard.edu/x/2022/notes/7/csv.png)

*   Tenga en cuenta que algunas filas tienen varios géneros y están rodeadas de comillas, como "Crimen, Drama", para que las comas dentro de nuestros datos no se malinterpreten.

*   Escribamos un nuevo programa, favoritos.py, para leer nuestro archivo CSV: ``` import csv with open("favorites.csv", "r") as file: reader = csv.reader(file) next(reader) for row in reader: print(row[1]) ```

*   Abriremos el archivo con una referencia llamada archivo, usando la palabra clave with en Python que cerrará nuestro archivo por nosotros.
*   La biblioteca csv tiene una función de lector que creará una variable de lector que podemos usar para leer el archivo como CSV.
*   Llamaremos a next para omitir la primera fila, ya que esa es la fila del encabezado.
*   Luego, usaremos un bucle para imprimir la segunda columna de cada fila, que es el título.

*   Ahora, si ejecutamos nuestro programa, veremos una lista de títulos de programas: ``` $ python favorites.py ... Friends ... friends ... Friends ... ```

*   Pero para el programa titulado "Amigos", algunas entradas están en mayúsculas y otras en minúsculas.

## Limpieza

*   Para mejorar nuestro programa, primero usaremos un DictReader, un lector de diccionarios, que crea un diccionario de cada fila, permitiéndonos acceder a cada columna por su nombre. Tampoco necesitamos omitir la fila del encabezado en este caso, ya que DictReader la usará automáticamente.

*   Dado que la primera fila en nuestro CSV tiene los nombres de las columnas, también se puede usar para etiquetar cada columna en nuestros datos. Ahora nuestro programa seguirá funcionando, incluso si se cambia el orden de las columnas.

*   Ahora intentemos filtrar los duplicados en nuestras respuestas:

*   Haremos una nueva lista llamada títulos y solo agregaremos el título de cada fila si aún no está en la lista. Entonces, podemos imprimir todos los títulos:

*   Vemos que todavía hay casi duplicados, ya que Amigos y amigos son, de hecho, cadenas diferentes todavía.

*   Queremos cambiar el título actual a mayúsculas y eliminar los espacios en blanco a su alrededor antes de agregarlo a nuestra lista:

*   Ahora, hemos canonicalizado o estandarizado nuestros datos, y nuestra lista de títulos es mucho más limpia:

*   Resulta que Python tiene otra estructura de datos incorporada, establecida, que garantiza que todos los valores sean únicos: ``` import csv titles = set() with open("favorites.csv", "r") as file: reader = csv.DictReader(file) for row in reader: title = row["title"].strip().upper() titles.add(title) for title in titles: print(title) ```

*   Ahora, podemos llamar a agregar en el conjunto y no tener que verificar nosotros mismos si ya está en el conjunto.

*   Para ordenar los títulos, podemos simplemente cambiar nuestro ciclo a for title en sorted(titles), lo que ordenará nuestro conjunto antes de iterarlo: ``` import csv titles = set() with open("favorites.csv", "r") as file: reader = csv.DictReader(file) for row in reader: title = row["title"].strip().upper() titles.add(title) for title in sorted(titles): print(title) ``` ``` $ python favorites.py ADVENTURE TIME ANNE WITH AN E ... AVATAR AVATAR THE LAST AIRBENDER AVATAR: THE LAST AIRBENDER ... BROOKLYN 99 BROOKLYN-99 ... ```

*   Ahora, vemos nuestros títulos en orden alfabético, pero todavía había algunas formas diferentes de ingresar el título de un programa. Dejaremos estas diferencias ahí por ahora, ya que probablemente requerirá un poco más de esfuerzo estandarizar completamente nuestros datos.

## Contando

*   Podemos usar un diccionario, en lugar de un conjunto, para contar la cantidad de veces que hemos visto cada título, siendo las claves los títulos y los valores un número entero contando la cantidad de veces que vemos cada uno de ellos: ``` import csv titles = {} with open("favorites.csv", "r") as file: reader = csv.DictReader(file) for row in reader: title = row["title"].strip().upper() titles[title] += 1 for title in sorted(titles): print(title) ```

*   A medida que leemos cada fila, aumentamos el valor almacenado para ese título en el diccionario en 1.

*   Ejecutaremos este programa y veremos: ``` $ python favorites.py Traceback (most recent call last): File "/workspaces/20377622/favorites.py", line 9, in <module>titles[title] += 1 KeyError: 'HOW I MET YOUR MOTHER' ```</module>

*   Tenemos un KeyError, ya que el título CÓMO CONOCÍ A TU MADRE aún no está en el diccionario.

*   Primero tendremos que agregar cada título a nuestro diccionario y establecer el valor inicial en 1: ``` import csv titles = {} with open("favorites.csv", "r") as file: reader = csv.DictReader(file) for row in reader: title = row["title"].strip().upper() if title in titles: titles[title] += 1 else: titles[title] = 1 for title in sorted(titles): print(title, titles[title]) ```

*   Agregaremos los valores, o conteos, a nuestro ciclo que imprime cada nombre de programa.

*   También podemos establecer el valor inicial en 0 y luego incrementarlo en 1 sin importar qué: ``` import csv titles = {} with open("favorites.csv", "r") as file: reader = csv.DictReader(file) for row in reader: title = row["title"].strip().upper() if not title in titles: titles[title] = 0 titles[title] += 1 for title in sorted(titles): print(title, titles[title]) ``` ``` $ python favorites.py ADVENTURE TIME 1 ANNE WITH AN E 1 ARCHER 1 ... AVATAR THE LAST AIRBENDER 5 ... COMMUNITY 8 ... ```

*   Ahora, la clave existirá en el diccionario y podemos referirnos con seguridad a su valor en el diccionario.
*   Así que ahora veremos los programas más populares impresos:

*   De hecho, podemos definir nuestra función en la misma línea, con esta sintaxis:

*   Podemos escribir y pasar una función lambda, o anónima, que no tiene nombre pero toma algún argumento o argumentos y devuelve un valor inmediatamente.
*   Tenga en cuenta que no hay paréntesis ni palabra clave de retorno, pero de manera concisa tiene el mismo efecto que nuestra función get_value anterior.

*   También podemos intentar contar todas las apariciones de un título específico:

*   Tendremos una variable de contador simple y le agregaremos una.

*   Ahora, si nuestros datos se refieren al mismo programa de diferentes maneras, podemos intentar verificar si la palabra "OFICINA" estaba en el título:

*   Resulta que una fila tiene un error tipográfico, "Thevoffice", por lo que ahora nuestro recuento es correcto.

*   También podemos usar expresiones regulares, una forma estandarizada de representar un patrón que debe coincidir con una cadena.
*   Por ejemplo, podemos escribir una expresión regular que coincida con las direcciones de correo electrónico:

*   El primer punto, ., indica cualquier carácter. El siguiente asterisco, *, indica 0 o más veces. Entonces, queremos un signo de arroba, @. Luego queremos 0 o más caracteres nuevamente, .*, y luego un punto literal en nuestra cadena, escapado con \.. Finalmente, queremos 0 o más caracteres nuevamente con .*.

*   Dado que probablemente queremos al menos 1 carácter en cada segmento de una dirección de correo electrónico, debemos cambiar nuestra expresión regular a:

*   El signo más, +, significa que estamos haciendo coincidir el carácter anterior 1 o más veces.
*   Podemos restringir el dominio del correo electrónico a .edu cambiando nuestra expresión regular a .+@.+\.edu.

*   Los lenguajes como Python y JavaScript admiten expresiones regulares, que son como un minilenguaje en sí mismos, con una sintaxis como:

*   . para cualquier personaje
*   .* para 0 o más caracteres
*   .+ para 1 o más caracteres
*   ? para un personaje opcional
*   ^ for start of input
*   $ for end of input
*   …

*   Podemos cambiar nuestro programa antes para usar re, una biblioteca de Python para expresiones regulares:

*   La biblioteca re tiene una función, buscar, a la que podemos pasar un patrón y una cadena para ver si hay una coincidencia.
*   Podemos cambiar nuestra expresión a "^(OFICINA|LA OFICINA)$", que coincidirá con OFICINA o LA OFICINA, pero solo si comienzan al principio de la cadena y terminan al final de la cadena (es decir, hay no hay otras palabras antes o después).
*   Incluso podemos cambiar THE OFFICE a THE.OFFICE, permitiendo que cualquier carácter (como un error tipográfico) esté entre esas palabras.

*   También podemos escribir un programa para pedirle al usuario un título en particular e informar su popularidad:

*   Le pedimos al usuario que ingrese y luego abrimos nuestro archivo CSV. Como estamos buscando un solo título, podemos tener una variable de contador que incrementamos.
*   Verificamos una coincidencia después de estandarizar tanto la entrada del usuario como el título de cada fila.

## Bases de datos relacionales

*   Las bases de datos relacionales son programas que almacenan datos, en última instancia, en archivos, pero con estructuras e interfaces de datos adicionales que nos permiten buscar y almacenar datos de manera más eficiente.
*   Cuando trabajamos con datos, generalmente necesitamos cuatro tipos de operaciones básicas con el acrónimo CRUD:

*   CREATE
*   READ
*   UPDATE
*   DELETE

## SQL

*   Con otro lenguaje de programación, SQL (pronunciado como “sequel”), podemos interactuar con bases de datos con verbos como:

*   CREATE, INSERT
*   SELECT
*   UPDATE
*   DELETE, DROP

*   La sintaxis en SQL podría verse así:

*   Con esta declaración, podemos crear una tabla, que es como una hoja de cálculo con filas y columnas.
*   En SQL, elegimos los tipos de datos que almacenará cada columna.

*   Usaremos un programa de base de datos común llamado SQLite, uno de los muchos programas disponibles que admiten SQL. Otros programas de bases de datos incluyen Oracle Database, MySQL, PostgreSQL y Microsoft Access.
*   SQLite almacena nuestros datos en un archivo binario, con 0 y 1 que representan los datos de manera eficiente. Interactuaremos con nuestras tablas de datos a través de un programa de línea de comandos, sqlite3.
*   Ejecutaremos algunos comandos en VS Code para importar nuestro archivo CSV a una base de datos:

*   Primero, ejecutaremos el programa sqlite3 con favoritos.db como el nombre del archivo de nuestra base de datos.
*   Con .import, SQLite crea una tabla en nuestra base de datos con los datos de nuestro archivo CSV.

*   Ahora, veremos tres archivos, incluido favorites.db:

*   Podemos abrir nuestro archivo de base de datos nuevamente y verificar el esquema o diseño de nuestra nueva tabla con .schema:

*   Vemos que .import usó el comando CREATE TABLE ... para crear una tabla llamada favoritos, con los nombres de las columnas copiados automáticamente de la fila del encabezado del CSV y los tipos para cada uno de ellos se supone que son texto.

*   Podemos seleccionar, o leer datos, con:

*   Con un comando en el formato SELECCIONAR columnas DE la tabla, podemos leer datos de una o más columnas. Por ejemplo, podemos escribir SELECCIONAR título, género DE favoritos; para seleccionar tanto el título como el género.

*   SQL admite muchas funciones que podemos usar para contar y resumir datos:

*   AVG
*   COUNT
*   DISTINCT
*   LOWER
*   MAX
*   MIN
*   UPPER
*   ...

*   Podemos limpiar nuestros títulos como antes, convirtiéndolos a mayúsculas e imprimiendo solo los valores únicos:

*   También podemos hacer un recuento de cuántas respuestas hay:

*   También podemos agregar más frases a nuestro comando:

*   WHERE, agregando una expresión booleana para filtrar nuestros datos
*   LIKE, filtrar las respuestas de forma más flexible
*   ORDER BY
*   LIMIT
*   GROUP BY

*   Podemos limitar el número de resultados:

*   También podemos buscar títulos que coincidan con una cadena:

*   El carácter % es un marcador de posición para cero o más caracteres, por lo que SQL admite algunas coincidencias de patrones, aunque no es tan eficaz como las expresiones regulares.

*   Podemos seleccionar solo el conteo en nuestro comando:

*   Si no nos gusta un programa, incluso podemos eliminarlo:

*   Con SQL, podemos cambiar nuestros datos de manera más fácil y rápida que con Python.

*   Podemos actualizar una fila específica de datos:

*   Ahora, hemos cambiado el valor de esa fila.

*   También podemos cambiar los valores en varias filas:

*   Con DELETE y DROP, podemos eliminar filas e incluso tablas completas también.
*   Y observe que en nuestros comandos, hemos escrito palabras clave de SQL en mayúsculas, para que se destaquen más.
*   Tampoco hay una forma integrada de deshacer los comandos, por lo que si cometemos un error, ¡podríamos tener que construir nuestra base de datos nuevamente!

## Tablas

*   Echaremos un vistazo a nuestro esquema de nuevo:

*   Si miramos nuestros valores de géneros, vemos cierta redundancia:

*   Y si queremos buscar programas que sean comedias, tenemos que buscar no solo con SELECT title FROM favorites WHERE genre = "Comedy";,pero también ... WHERE genre = "Comedy, Drama";, ... WHERE genre = "Comedy, News"; , y así.
*   Podemos usar la palabra clave LIKE nuevamente, pero dos géneros, "Música" y "Musical", son lo suficientemente similares como para que eso sea problemático.
*   De hecho, podemos escribir nuestro propio programa Python que usará SQL para importar nuestros datos CSV en dos tablas:

*   Primero, importamos la biblioteca Python cs50 para poder ejecutar comandos SQL más fácilmente.
*   Luego, el resto de este código importará cada fila de favorites.csv.

*   Ahora, nuestra base de datos tendrá este diseño:

*   Tenemos una tabla, espectáculos, con una columna de identificación y una columna de título. Podemos especificar que un título no sea nulo y que la identificación sea la columna que queremos usar como clave principal.
*   Luego, tendremos una tabla llamada géneros, donde tenemos una columna show_id que hace referencia a nuestra tabla de espectáculos, junto con una columna de género.
*   Este es un ejemplo de una relación, como un enlace, entre filas en diferentes tablas en nuestra base de datos.

*   En nuestra tabla de programas, veremos cada programa con un número de identificación:

*   Y podemos ver que la tabla de géneros tiene una o más filas para cada show_id:

*   Dado que cada programa puede tener más de un género, podemos tener más de una fila por programa en nuestra tabla de géneros, lo que se conoce como una relación de uno a muchos.
*   Además, los datos ahora son más limpios, ya que cada nombre de género está en su propia fila.

*   Podemos seleccionar todos los programas que son comedias seleccionando primero de la tabla de géneros y luego buscando esos identificadores en la tabla de programas:

*   Tenga en cuenta que hemos anidado dos consultas, donde la interna devuelve una lista de ID de programas y la externa las usa para seleccionar los títulos de los programas que coinciden.

*   Ahora podemos ordenar y mostrar solo los títulos únicos agregando a nuestro comando:

*   Y podemos agregar nuevos datos a cada tabla, para poder agregar otro espectáculo. Primero, agregaremos una nueva fila a la tabla de espectáculos para Seinfeld:

*   Luego, podemos obtener la identificación de nuestra fila buscándola en la tabla:

*   Lo usaremos como show_id para agregar una nueva fila en la tabla de géneros:

*   Luego, usaremos UPDATE para poner el título en mayúsculas:

*   Finalmente, ejecutaremos el mismo comando que antes y veremos que nuestro nuevo programa está en la lista de comedias:

## SQL en Python

*   Resulta que podremos escribir código Python que automatice esto, por lo que podemos imaginar la creación de aplicaciones web que pueden almacenar y buscar mediante programación datos de usuarios, pedidos de compras en línea y más.
*   Podemos escribir un programa que le pida al usuario el título de un programa y luego imprima su popularidad:

*   Usaremos la biblioteca cs50 para ejecutar comandos SQL más fácilmente y abriremos la base de datos de favoritos.db que creamos anteriormente.
*   Le pediremos al usuario un título y luego ejecutaremos un comando. A ? en el comando nos permitirá sustituir variables de forma segura en nuestro comando.
*   Los resultados se devuelven en una lista de filas y COUNT(*) devuelve solo una fila. En nuestro comando, agregaremos el contador AS, por lo que el recuento se devuelve en la fila (que es un diccionario) con el nombre de la columna contador.

*   Podemos ejecutar nuestro programa y buscar “The Office”:

*   Y podemos modificar nuestro programa para imprimir todas las filas que coincidan:

*   Dado que LIKE no distingue entre mayúsculas y minúsculas, vemos todas las diversas formas en que se capitalizaron los títulos.

## IMDb

*   IMDb, o Internet Movie Database, tiene conjuntos de datos disponibles para descargar como archivos TSV (valores separados por tabuladores).
*   Abriremos una base de datos que el personal ha creado previamente:

*   Tenga en cuenta que tenemos varias tablas, cada una de las cuales tiene columnas de varios tipos de datos.
*   Tanto en la tabla de estrellas como en la de escritores, por ejemplo, tenemos una columna show_id que hace referencia a la identificación de alguna fila en la tabla de espectáculos y una columna person_id que hace referencia a la identificación de alguna fila en la tabla de personas. Efectivamente, vinculan programas y personas por sus identificaciones.

*   Resulta que SQL también tiene sus propios tipos de datos:

*   BLOB, para "objeto binario grande", datos binarios sin procesar que podrían representar archivos
*   INTEGER
*   NUMERIC, como un número pero no exactamente un número, como una fecha o una hora
*   REAL, para valores de punto flotante
*   TEXT, como cadenas

*   Las columnas también pueden tener atributos adicionales:

*   PRIMARY KEY, como las columnas de identificación anteriores que se utilizarán para identificar de forma única cada fila
*   FOREIGN KEY, como la columna show_id anterior que hace referencia a una columna en alguna otra tabla

*   Podemos ver que hay millones de filas en la tabla de personas:

*   Pero como antes, podemos buscar solo una fila:

*   Resulta que hay algunos programas titulados "La oficina":

*   El más popular, con 188 episodios, es el que queremos, así que podemos conseguir solo ese:

*   Podemos activar un temporizador y ver que nuestro comando original tardó unos 0,02 segundos en ejecutarse:

*   Podemos crear un índice o estructuras de datos adicionales que nuestro programa de base de datos utilizará para futuras búsquedas:

*   Ahora, nuestro comando de búsqueda casi no toma tiempo:

*   Resulta que estas estructuras de datos son generalmente árboles B, como los árboles binarios que hemos visto en C pero con más hijos, con nodos organizados de tal manera que podemos buscar más rápido que linealmente: ![hola5](https://cs50.harvard.edu/x/2022/notes/7/b_tree.png)

*   La creación de un índice lleva algo de tiempo al principio, tal vez ordenando los datos, pero luego podemos buscar mucho más rápido.

*   Con nuestros datos repartidos entre diferentes tablas, podemos anidar nuestras consultas para obtener datos útiles. Por ejemplo, podemos obtener todos los títulos de programas protagonizados por una persona en particular:

*   SELECCIONAREMOS el título de la tabla de programas para programas con una identificación que coincida con una lista de show_ids de la tabla de estrellas. Esos show_ids, a su vez, deben tener un person_id que coincida con el id de Steve Carell en la tabla de personas.

*   Nuestra consulta se ejecuta bastante rápido, pero podemos crear algunos índices más:

*   Cada índice tarda casi un segundo en construirse, pero luego, nuestra misma consulta tarda muy poco tiempo en ejecutarse.

*   Resulta que podemos usar comandos JOIN para combinar tablas en nuestras consultas:

*   Con la sintaxis JOIN, podemos combinar tablas virtualmente en función de sus claves externas y usar sus columnas como si fueran una sola tabla. Aquí, estamos haciendo coincidir la tabla de personas con la tabla de estrellas y luego con la tabla de espectáculos.

*   Podemos formatear la misma consulta un poco mejor enumerando las tablas que queremos usar todas a la vez:

*   La desventaja de tener muchos índices es que cada uno de ellos ocupa cierta cantidad de espacio, lo que puede volverse significativo con muchos datos y muchos índices.

## Problemas

*   Un problema en SQL se llama ataque de inyección de SQL, donde alguien puede inyectar o colocar sus propios comandos en las entradas que luego ejecutamos en nuestra base de datos.
*   Podríamos encontrar una página de inicio de sesión para un sitio web que solicite un nombre de usuario y una contraseña, y los verifique en una base de datos SQL.
*   Nuestra consulta para buscar un usuario podría ser:

*   ¿Usando el ? símbolos como marcadores de posición, nuestra biblioteca SQL escapará de la entrada o evitará que los caracteres peligrosos se interpreten como parte del comando.

*   Por el contrario, podríamos tener una consulta SQL que es una cadena formateada, como:

*   Si un usuario escribe malan@harvard.edu'-- como entrada, la consulta terminará siendo:

*   Esta consulta en realidad seleccionará la fila donde nombre de usuario = 'malan@harvard.edu', sin verificar la contraseña, ya que las comillas simples terminan la entrada y convierte el resto de la línea en un comentario en SQL.

*   El usuario podría incluso agregar un punto y coma, ;, y escribir un nuevo comando propio, que ejecutará nuestra base de datos.
*   Otro conjunto de problemas con las bases de datos son las condiciones de carrera, en las que los datos compartidos se modifican involuntariamente mediante el código que se ejecuta en diferentes dispositivos o servidores al mismo tiempo.
*   Un ejemplo es una publicación popular que obtiene muchos Me gusta. Un servidor podría intentar incrementar la cantidad de Me gusta, solicitando a la base de datos la cantidad actual de Me gusta, agregando uno y actualizando el valor en la base de datos:

*   Dos servidores diferentes, que responden a dos usuarios diferentes, pueden obtener el mismo número inicial de Me gusta, ya que la primera línea de código se ejecuta al mismo tiempo en cada servidor.
*   Luego, ambos usarán UPDATE para establecer la misma nueva cantidad de Me gusta, aunque debería haber dos incrementos separados.

*   Otro ejemplo podría ser el de dos compañeros de cuarto y un refrigerador compartido en su dormitorio. El primer compañero de piso llega a casa y ve que no hay leche en la nevera. Así que el primer compañero de cuarto se va a la tienda a comprar leche. Mientras están en la tienda, el segundo compañero de cuarto llega a casa, ve que no hay leche y se va a otra tienda a comprar leche también. Más tarde, habrá dos jarras de leche en la nevera.
*   Podemos resolver este problema cerrando la nevera para que nuestro compañero de cuarto no pueda comprobar si hay leche hasta que volvamos.
*   Para resolver este problema, SQL admite transacciones, donde podemos bloquear filas en una base de datos, de modo que un conjunto particular de acciones sea atómico o se garantice que sucedan juntas.
*   Por ejemplo, podemos solucionar nuestro problema anterior con:

*   La base de datos se asegurará de que todas las consultas intermedias se ejecuten juntas.

*   Pero cuantas más transacciones tengamos, más lentas pueden ser nuestras aplicaciones, ya que cada servidor tiene que esperar a que finalicen las transacciones de otros servidores.

Ejemplo parrafo y etiquetas html