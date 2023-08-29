/*
 Exemplo0713 - v0.0. - 03 / 05 / 2022
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
#include <math.h>


void multiplo(int x)
{
    FILE* arquivo = fopen ( "RESULTADO03.TXT", "wt" );

    int y = 0;
    int formula = 0;

    for(y=0; y<x; y=y+1)
    {
        formula = pow(5,y);
        
              fprintf(arquivo,"\n%d", formula);
        
    }

    fclose(arquivo);
}

void leitura()
{
    int x=0;

    printf("\nEntre com uma quantidade: ");
    scanf("%d",&x);

    multiplo(x);
    printf("\nOs valores foram gravados no arquivo");
}

int main()
{
    leitura();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}