Resolución de Laboratorio 4: Volumen
```C
// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t header[HEADER_SIZE]; // Matriz de bytes para almacenar los datos del encabezado del archivo WAV
    fread(header, sizeof(uint8_t), HEADER_SIZE, input); // Leer el encabezado del input
    fwrite(header, sizeof(uint8_t), HEADER_SIZE, output); // Transferir los datos al output


    // TODO: Read samples from input file and write updated data to output file
    int16_t buffer;  // Declaración de variable buffer (será cada muestra)
    // Bucle para lectura de input y escritura de output (16 bits a la vez)
    while(fread(&buffer, sizeof(int16_t), 1, input))
    {
        buffer = buffer * factor; // Multiplicando cada muestra por el factor dado
        fwrite(&buffer, sizeof(int16_t), 1, output); // Escribiendo cada muestra en el archivo output
    }

    // Close files
    fclose(input);
    fclose(output);

    return 0;
}
```
