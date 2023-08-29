/*
 Exemplo0911 - v0.0. - 17 / 05 / 2022
 Author: Marcelo Reis Esteves
*/
#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void lerEprint(int linhas, int colunas, int matriz[linhas][colunas])
{
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
            printf("%d\t", matriz[x][y]);
        }

        printf("\n");
        
    }

}


int main()
{
    int colunas = 0;
    int linhas = 0;

    printf("\nEntre com a quantidade de colunas: ");
    scanf("%d", &colunas);

    printf("\nEntre com a quantidade de linhas: ");
    scanf("%d", &linhas);

    int matriz[linhas][colunas];

    lerEprint(linhas, colunas, matriz);
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
    return 0;
}