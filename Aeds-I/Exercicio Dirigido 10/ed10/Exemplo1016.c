/*
 Exemplo1016 - v0.0. - 25 / 05 / 2022
 Author: Marcelo Reis Esteves
*/
#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void task(char filename[80])
{
    FILE* arquivo = fopen(filename, "rt");

    int controle = 0;
    int x = 0;
    int y = 0;
    int matriz[3][3];
    int transposta[3][3];

    for (x = 0; x < 3; x++)
    {

        for ( y = 0; y < 3; y++)
        {
            fscanf(arquivo, "%d", &matriz[x][y]);
            fscanf(arquivo, "%d", &transposta[y][x]);
            
        }

        printf("\n");
        
    }

    for (y = 0; y < 3; y++)
    {

        for ( x = 0; x < 3; x++)
        {
            printf("%d\t", transposta[x][y]);
        }

        printf("\n");
        
    }
  


    fclose(arquivo);
   
}

int main()
{
    char filename[80];
    int valor = 0;

    printf("\nEntre com o nome do arquivo: ");
    scanf("%s", filename);

    task(filename);

    printf("\n");
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();

    return 0;
}
