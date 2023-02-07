# Laboratorio 4: Volumen
>Le invitamos a colaborar con uno o dos compañeros en este laboratorio, aunque se espera que cada estudiante de dicho grupo contribuya de igual forma para su desarrollo.

Escriba un programa para modificar el volumen de un archivo de audio.
```
  $ ./volume INPUT.wav OUTPUT.wav 2.0
  ```
  
Donde ```INPUT.wav``` es el nombre de un archivo de audio original y ```OUTPUT.wav``` es el nombre de un archivo de audio con un volumen que ha sido escalado por el factor dado (por ejemplo, 2.0).
  
## Archivos WAV
Los archivos WAV son un formato de archivo común para representar audio. Almacenan audio como una secuencia de "muestras": números que representan el valor de alguna señal de audio en un momento determinado. Los archivos WAV comienzan con un "encabezado" de 44 bytes que contiene información sobre el archivo en sí, incluido el tamaño del archivo, la cantidad de muestras por segundo y el tamaño de cada muestra. Después del encabezado, el archivo WAV contiene una secuencia de muestras, cada una de las cuales es un entero de 2 bytes (16 bits) que representa la señal de audio en un momento determinado.

Escalar cada valor de muestra por un factor dado tiene el efecto de cambiar el volumen del audio. Multiplicar cada valor de muestra por 2.0, por ejemplo, tendrá el efecto de duplicar el volumen del audio de origen. Mientras tanto, multiplicar cada muestra por 0.5 tendrá el efecto de reducir el volumen a la mitad.

## Tipos
Hasta ahora, hemos visto varios tipos diferentes en C, incluidos ```int```, ```bool```, ```char```, ```double```, ```float``` y ```long```. Dentro de un archivo de encabezado llamado ```stdint.h``` están las declaraciones de otros tipos que nos permiten definir con mucha precisión el tamaño (en bits) y el signo (con o sin signo) de un número entero. Dos tipos en particular nos serán útiles en esta práctica de laboratorio.
* ```uint8_t``` es un tipo que almacena un entero de 8 bits sin signo (es decir, no negativo). Podemos tratar cada byte del encabezado de un archivo WAV como un valor ```uint8_t```.
* ```int16_t``` es un tipo que almacena un entero de 16 bits con signo (es decir, positivo o negativo). Podemos tratar cada muestra de audio en un archivo WAV como un valor ```int16_t```.

## Empezando

Abra VS Code.

Comience haciendo clic dentro de la ventana de su terminal, luego ejecute ```cd``` solo. Debería encontrar que su "indicador" se parece al siguiente.
```
  $
  ```
 
Haga clic dentro de esa ventana de terminal y luego ejecute
```
  wget https://cdn.cs50.net/2021/fall/labs/4/volume.zip
  ```
  
a continuación de Enter para descargar un ZIP llamado ```volume.zip``` en su espacio de código. ¡Tenga cuidado de no pasar por alto el espacio entre ```wget``` y la siguiente URL, o cualquier otro carácter para el caso!

Ahora ejecute
```
  unzip volume.zip
  ```
  
para crear una carpeta llamada ```volume```. Ya no necesitará el archivo ZIP, por lo que puede ejecutar
```
  rm volume.zip
  ```
  
y responda con "y" seguido de Enter en el aviso, para eliminar el archivo ZIP que descargó.

Ahora escriba
```
  cd volume
  ```
  
seguido de Enter para entrar (es decir, abrir) ese directorio. Su mensaje ahora debería parecerse al de abajo.
```
  volume/ $
  ```

Si todo fue exitoso, debe ejecutar
```
  ls
  ```
  
y debería ver un archivo ```volume.c``` junto a un archivo ```input.wav```.

Si tiene algún problema, siga de nuevo estos pasos y vea si puede determinar dónde se equivocó.

## Detalles de implementación

Complete la implementación de ```volume.c```, de modo que cambie el volumen de un archivo de sonido por un factor dado.

- El programa acepta tres argumentos de línea de comandos: ```input``` representa el nombre del archivo de audio original, ```output``` representa el nombre del nuevo archivo de audio que debe generarse y ```factor``` es la cantidad en la que debe escalarse el volumen del archivo de audio original.
  - Por ejemplo, si ```factor``` es ```2.0```, entonces su programa debería duplicar el volumen del archivo de audio ```input``` y guardar el archivo de audio recién generado en ```output```.
- Su programa debe leer primero el encabezado del archivo de entrada y escribir el encabezado en el archivo de salida. Recuerde que este encabezado siempre tiene exactamente 44 bytes de longitud.
  - Tenga en cuenta que ```volume.c``` ya define una variable para usted llamada ```HEADER_SIZE```, igual al número de bytes en el encabezado.
- Luego, su programa debería leer el resto de los datos del archivo WAV, una muestra de 16 bits (2 bytes) a la vez. Su programa debe multiplicar cada muestra por ```factor``` y escribir la nueva muestra en el archivo de salida.
  - Puede suponer que el archivo WAV utilizará valores de 16 bits como muestras. En la práctica, los archivos WAV pueden tener una cantidad variable de bits por muestra, pero supondremos muestras de 16 bits para esta práctica.
- Su programa, si usa ```malloc```, no debe perder memoria.

### Tutorial
>Este video se grabó cuando el curso aún usaba CS50 IDE para escribir código. Aunque la interfaz puede verse diferente de su espacio de código, ¡el comportamiento de los dos entornos debería ser muy similar!

### Sugerencias
- Es probable que desee crear una matriz de bytes para almacenar los datos del encabezado del archivo WAV que leerá del archivo de entrada. Usando el tipo ```uint8_t``` para representar un byte, puede crear una matriz de ```n``` bytes para su encabezado con sintaxis como
```
uint8_t header[n];
```
reemplazando ```n``` con el número de bytes. Luego puede usar headercomo argumento para leer freado fwriteescribir desde el encabezado.

- Es probable que desee crear un "búfer" en el que almacenar muestras de audio que lea del archivo WAV. Usando el tipo ```int16_t``` para almacenar una muestra de audio, puede crear una variable de búfer con sintaxis como
```
int16_t buffer;
```
Luego puede usar ```&buffer``` como argumento para ```fread``` o ```fwrite``` para leer o escribir desde el búfer. (Recuerde que el operador ```&``` se usa para obtener la dirección de la variable).

- Puede encontrar la documentación para fread y fwrite útil aquí.
    - En particular, tenga en cuenta que ambas funciones aceptan los siguientes argumentos:
      - ```ptr```: un puntero a la ubicación en la memoria para almacenar datos (al leer de un archivo) o desde donde escribir datos (al escribir datos en un archivo)
      - ```size```: el número de bytes en un elemento de datos
      - ```nmemb```: el número de elementos de datos (cada uno de los bytes ```size```) para leer o escribir
      - ```stream```: el puntero del archivo que se va a leer o escribir
- Según su documentación, ```fread``` devolverá la cantidad de elementos de datos leídos con éxito. ¡Puede encontrar esto útil para verificar cuando haya llegado al final del archivo!

### Cómo probar su código

Su programa debe comportarse según los ejemplos de a continuación.
```
$ ./volume input.wav output.wav 2.0
```

Cuando escuche ```output.wav``` (por ejemplo, al hacer clic sobre ```output.wav``` en el navegador de archivos, elegir **Descargar** y luego abrir el archivo en un reproductor de audio en su computadora), ¡debería ser el doble de fuerte que ```input.wav```!

```
$ ./volume input.wav output.wav 0.5
```

Cuando escuche ```output.wav```, debería ser la mitad de fuerte que ```input.wav```!

Ejecute lo siguiente para evaluar la corrección de su código usando ```check50```. ¡Pero asegúrese de compilarlo y probarlo usted mismo también!
```
check50 cs50/labs/2022/x/volume
```
Ejecute lo siguiente para evaluar el estilo de su código usando ```style50```.
```
style50 volume.c
```

### Cómo enviar
En su terminal, ejecute lo siguiente para enviar su trabajo.
```
submit50 cs50/labs/2022/x/volume
```
