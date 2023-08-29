/*
 Exemplo1014 - v0.0. - 25 / 05 / 2022
 Author: Marcelo Reis Esteves
*/
#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

void task(char filename[80], char filename2[80])
{
    FILE* arquivo = fopen(filename, "rt");

    FILE* arquivo2 = fopen(filename2, "rt");

    int controle = 0;
    int quantidade = 0;
    int quantidade2 = 0;
    int SOMA = 0;

    fscanf(arquivo, "%d", &quantidade);
    int arranjo[quantidade];

    fscanf(arquivo2, "%d", &quantidade2);
    int arranjo2[quantidade2];

    if (quantidade == quantidade2)
    {
        for ( controle = 0; controle < quantidade; controle = controle +1)
        {
            fscanf(arquivo, "%d", &arranjo[controle]); 
            fscanf(arquivo2, "%d", &arranjo2[controle]); 
        }

        for ( controle = 0; controle < quantidade; controle = controle +1)
        {
            SOMA = SOMA + arranjo[controle] + arranjo2[controle];   
        }
        
        printf("\nA soma dos arranjos e igual = %d", SOMA);
           
    }
    

    fclose(arquivo);
    fclose(arquivo2);
    
}

int main()
{
    char filename[80];
    char filename2[80];
    int valor = 0;

    printf("\nEntre com o nome do arquivo: ");
    scanf("%s", filename);

    printf("\nEntre com o nome do segundo arquivo: ");
    scanf("%s", filename2);

    task(filename,filename2);

    printf("\n");
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();

    return 0;
}