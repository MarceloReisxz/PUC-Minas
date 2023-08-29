/*
 Exemplo0813 - v0.0. - 03 / 05 / 2022
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
#include <stdlib.h>
#include <time.h>


void task(int cima, int baixo, int testes)
{

// definir dado local
 int controle = 0;
 int y = 0;
 int arranjo[testes];

 srand(time(NULL));

 for ( controle = 0; controle < testes; controle = controle + 1)
 {

     y = baixo + rand() %cima;

     if(y>cima)
     {
        y = baixo + rand() %cima -1; 
     }

     arranjo[controle] = y;


     printf("\n%d", y);
 }

 FILE* arquivo = fopen("DADOS.txt", "wt");

 fprintf(arquivo,"\n%d\n", testes);

 for (controle = 0; controle<testes; controle = controle + 1)
 {
     fprintf(arquivo,"\n%d", arranjo[controle]);
 }
 
 

}


int main()
{
    int cima = 0;
    int baixo = 0;
    int testes = 0;
    
    printf("\nEntre com o limite inferior:");
    scanf("%d", &baixo);

    printf("\nEntre com o limite superior:");
    scanf("%d", &cima);

    printf("\nEntre com a quantidade de testes:");
    scanf("%d", &testes);

    task(cima, baixo, testes);

    getchar();
    getchar();
    return 0;
}