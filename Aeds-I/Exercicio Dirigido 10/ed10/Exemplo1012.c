/*
 Exemplo1012 - v0.0. - 25 / 05 / 2022
 Author: Marcelo Reis Esteves
*/
#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void task(char filename[80], int valor)
{
    FILE* arquivo = fopen(filename, "rt");

    int controle = 0;
    int x = 0;
    bool verifica = false;


    fscanf(arquivo, "%d", &x);

    int arranjo[x];
    

    for ( controle = 0; controle < x; controle = controle +1)
    {
        fscanf(arquivo, "%d", &arranjo[controle]);
        
        if (arranjo[controle] == valor)
        {
            verifica = true;
        }
        
    }

    if (verifica == true)
        {
            printf("\nO valor ESTA no arquivo");
        }

        else
        {
            printf("\nO valor NAO ESTA no arquivo");
        }


        fclose(arquivo);
    
}

int main()
{
    char filename[80];
    int valor = 0;

    printf("\nEntre com o nome do arquivo: ");
    scanf("%s", filename);

    printf("\nEntre com o valor que quer procurar: ");
    scanf("%d", &valor);

    task(filename,valor);

    printf("\n");
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();

    return 0;
}