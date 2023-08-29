/*
 Exemplo0912 - v0.0. - 17 / 05 / 2022
 Author: Marcelo Reis Esteves
*/

#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void lerArquivo(char* filename, int linhas, int colunas, int matriz[linhas][colunas])
{
    FILE* arquivo = fopen (filename, "rt");
    int x = 0;
    int y = 0;
    int z = 0;

 for (x=0; x<linhas; x= x+1)
 {
     for (y=0; y<colunas; y= y+1)
     {
          // ler valor
                fscanf ( arquivo, "%d", &z );

          // guardar valor
                matriz [ x ][ y ] = z;
     }
     
 }


    for (x=0; x < linhas; x = x +1)
    {
        for (y=0; y < colunas; y= y +1)
        {
            printf("%d\t", matriz[x][y]);
        }

        printf("\n");
        
    }


    fclose(arquivo);
}

void lerEprint(char* filename, int linhas, int colunas, int matriz[linhas][colunas])
{
    FILE* arquivo = fopen (filename, "wt");

    int x = 0;
    int y = 0;
    int z = 0;


    for (x=0; x < linhas; x = x +1)
    {
        for (y=0; y < colunas; y= y +1)
        {
            printf("\n(%d,%d): ", x,y);
            scanf("%d", &z);

            matriz[x][y] = z;
        }
        
    }

    printf("\n");

    for (x=0; x < linhas; x = x +1)
    {
        for (y=0; y < colunas; y= y +1)
        {
            fprintf(arquivo,"%d\t", matriz[x][y]);
        }

        fprintf(arquivo,"\n");
        
    }

    fclose(arquivo);

}


int main()
{
    char filename[80];
    int colunas = 0;
    int linhas = 0;

    printf("\nEntre com a quantidade de colunas: ");
    scanf("%d", &colunas);

    printf("\nEntre com a quantidade de linhas: ");
    scanf("%d", &linhas);

    int matriz[linhas][colunas];

    printf("\nEntre com o nome do arquivo em que quer gravar: ");
    scanf("%s", filename);

    lerEprint(filename, linhas, colunas, matriz);
    lerArquivo(filename, linhas, colunas, matriz);

    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
    return 0;
}