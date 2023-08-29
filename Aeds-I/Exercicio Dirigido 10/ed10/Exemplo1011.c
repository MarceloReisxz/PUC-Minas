/*
 Exemplo1011 - v0.0. - 25 / 05 / 2022
 Author: Marcelo Reis Esteves
*/
#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void task(int sup, int inf, int quantidade)
{
    int controle = 0;
    int z = 0;
    int arranjo[quantidade];

    FILE* arquivo = fopen("DADOS.TXT", "wt");
    fprintf(arquivo, "%d", quantidade);

    for ( controle = 0; controle < quantidade; controle = controle +1)
    {
        int z = rand() %sup + inf;

        if(z > sup || z < inf)
        {
            controle = controle - 1;
        }
        else
        {
            arranjo[controle] = z;
            fprintf(arquivo,"\n%d",z);
        }
        
    }
    
}

int main()
{
    int sup = 0;
    int inf = 0;
    int quantidade = 0;

    printf("\nEntre com o limite supeior: ");
    scanf("%d", &sup);

    printf("\nEntre com o limite inferior: ");
    scanf("%d", &inf);

    printf("\nEntre com a quantidade: ");
    scanf("%d", &quantidade);

    task(sup,inf,quantidade);

    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();

    return 0;
}