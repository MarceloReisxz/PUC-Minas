/*
 Exemplo1017 - v0.0. - 27 / 05 / 2022
 Author: Marcelo Reis Esteves
*/

#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>


void lerEprint(char* filename, int linhas, int colunas, int matriz[linhas][colunas])
{
    FILE* arquivo = fopen (filename, "wt");

    int x = 0;
    int y = 0;
    int z = 0;
    bool verifica = true;


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
            fprintf(arquivo, "%d\t", matriz[x][y]);

            if (matriz[x][y]!=0)
            {
                verifica = false;
            }
            
        }

        fprintf(arquivo, "\n");
        
    }

    if (verifica == false)
    {
        printf("\nA matriz contem valores diferentes de 0 ");
    }
    else
    {
        printf("\nA matriz somente contem valores iguais a 0 ");
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

    printf("\n");

    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
    return 0;
}