/*
 Exemplo1015 - v0.0. - 25 / 05 / 2022
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
    int quantidade = 0;
    bool crescente = true;

    fscanf(arquivo, "%d", &quantidade);
    int arranjo[quantidade];

        for ( controle = 0; controle < quantidade; controle = controle +1)
        {
            fscanf(arquivo, "%d", &arranjo[controle]);  
        }

        controle = 1;

        while (controle < quantidade && crescente == true)
        {
            if (arranjo[controle - 1] > arranjo[controle])
            {
                crescente = false;
            }
            
            controle = controle + 1;
        }

        if (crescente == true)
        {
            printf("\nO arranjo ESTA em ordem.");
        }
        else
        {
            printf("\nO arranjo NAO ESTA em ordem.");
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