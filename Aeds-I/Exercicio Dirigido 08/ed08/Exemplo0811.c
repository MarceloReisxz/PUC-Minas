/*
 Exemplo0811 - v0.0. - 03 / 05 / 2022
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


void task(int x, int arranjo[])
{
    FILE* arquivo = fopen("DADOS_01.txt", "wt");
    
// definir dado local
 int controle = 0;
 int contador = 0;
 int y = 0;

// mostrar valores no arranjo
 for ( controle=0; controle<x; controle=controle+1 )
 {
    contador = contador + 1;
 }
 fprintf(arquivo,"\n%d\n", contador);
 printf("\nTamanho do Arranjo =  %d", contador);

// mostrar valores no arranjo
 for ( controle=0; controle<x; controle=controle+1 )
 {
    arranjo[controle] = y + 1;

   if (arranjo[controle]%2!=0)
   {
       arranjo[controle] = y + 2;
       y = y + 2;
   }
    
    printf("\n%d = %d", controle, arranjo[controle]);
    fprintf(arquivo,"\n%d", arranjo[controle]);
    
 }

 fclose(arquivo);

}


int main()
{
    int x = 0;
    
    printf("\nEntre com um valor:");
    scanf("%d", &x);
    
    int arranjo[x];

    task(x,arranjo);

    getchar();
    getchar();
    return 0;
}