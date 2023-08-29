/*
 Exemplo0711 - v0.0. - 03 / 05 / 2022
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


void multiplo(int x)
{
    FILE* arquivo = fopen ( "RESULTADO01.TXT", "wt" );

    int y = 0;
    int formula = 0;

    for(y=0; y<x; y=y+1)
    {
        formula = (2 * y) -1;
        
        if ( formula%2!=0  &&  formula%3==0 )
         {
              fprintf(arquivo,"\n%d", formula);
         }
        
        else
        {
            x = x +1;
        }
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
