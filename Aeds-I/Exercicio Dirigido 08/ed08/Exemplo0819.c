/*
 Exemplo0819 - v0.0. - 03 / 05 / 2022
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


void ordem(int x)
{
FILE* arquivo = fopen("DADOS.txt", "rt");
// definir dado local
int y = 0;
int z = 0;
int controle = 0;
bool verifica = false; 


fscanf ( arquivo, "%d", &y );

int arranjo[y];


    for(controle = 0; controle<y; controle = controle +1)
    {
        // ler valor
        fscanf ( arquivo, "%d", &z );

        arranjo[controle] = z;    
     
    }

controle = 0;

    while (controle<y && verifica==false)
    {
        if (arranjo[controle]==x)
        {
            verifica = true;
        }
    
        controle = controle + 1;

    }

    if (verifica==true)
    {
        printf("\nO valor ESTA no arquivo na posicao %d.", controle);
    }
    else
    {
        printf("\nO valor NAO esta no arquivo.");
    }
    
 
}


int main()
{
    int x = 0;
    
    printf("\nEntre com um valor a ser procurado: ");
    scanf("%d", &x);

    ordem(x);

    getchar();
    getchar();
    return 0;
}

