/*
 Exemplo0817 - v0.0. - 03 / 05 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0201 exemplo0201.c
 Windows: gcc -o exemplo0201 exemplo0201.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0201
 Windows: exemplo0201
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>


void ordem(int x, int arranjo[])
{

// definir dado local
 int controle = 0;
 bool verifica = true; 

    while (controle<x-1 && verifica==true)
    {
        if (arranjo[controle]>arranjo[controle+1])
        {
            verifica = true;
        }
        else
        {
            verifica = false;
        }
    
        controle = controle + 1;
    }

    if (verifica==true)
    {
        printf("\nOs valores estao em ordem DECRESCENTE");
    }
    else
    {
        printf("\nOs valores NAO estao em ordem");
    }
    
 
}


int main()
{
    int x = 0;
    int z = 0;
    int controle = 0;
    
    printf("\nEntre com um tamanho para o arranjo:");
    scanf("%d", &x);

    int arranjo[x];

    for (controle = 0; controle <x; controle = controle + 1)
    {
        printf("\nEntre com um valor para [%d]:", controle);
        scanf("%d", &z);

        arranjo[controle] = z;
    }

    ordem(x,arranjo);

    getchar();
    getchar();
    return 0;
}