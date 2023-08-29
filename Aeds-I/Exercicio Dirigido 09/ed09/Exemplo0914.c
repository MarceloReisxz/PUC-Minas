/*
 Exemplo0914 - v0.0. - 17 / 05 / 2022
 Author: Marcelo Reis Esteves
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include "io.h"


void readMatriz(int linhas, int colunas, int matriz[linhas][colunas])
{
    int x = 0;
    int y = 0;
    int z = 0;
    int n = linhas;

    for(x=0; x<linhas; x=x+1)
    {
        for(y=0; y<colunas; y=y+1)
        {
            printf("\n(%d,%d): ", x, y);
            scanf("%d", &z);

            matriz[x][y] = z;

        }
    }

    printf("\n");

    for(x=0; x<linhas; x=x+1)
    {
        for(y=0; y<colunas; y=y+1)
        {
            printf("%d\t", matriz[x][y]);
        }

        printf("\n");
    }

    printf("\n");

    printf("Diagonal Secundaria =");

    printf("\n");


    if(linhas == colunas)
    {
        for(x=0; x<linhas; x=x+1)
            {
                for(y=0; y<colunas; y=y+1)

                        {
                            if(x+y==n-1)
                            {
                               printf("%d\t", matriz[x][y]);
                            }
                            else
                            {
                                printf("0\t");
                            }

                        }

                        printf("\n");
            }
    }



}


int main()
{
    int linhas = 0;
    int colunas = 0;

    printf("\nEntre com o numero de linhas: ");
    scanf("%d", &linhas);

    printf("\nEntre com o numero de colunas: ");
    scanf("%d", &colunas);

    int matriz[linhas][colunas];

    readMatriz(linhas, colunas, matriz);

    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();

    return 0;
}
