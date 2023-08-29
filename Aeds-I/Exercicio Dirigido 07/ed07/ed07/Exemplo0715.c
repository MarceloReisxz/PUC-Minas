/*
 Exemplo0715 - v0.0. - 03 / 05 / 2022
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


void multiplo(int x, double z)
{
    FILE* arquivo = fopen ( "RESULTADO05.TXT", "wt" );

    int y = 0;
    int formula = 0;
    int impar = 1;

    for(y=1; y<x; y=y+1)
    {
        formula = pow(z,impar);
        
              if(y==1)
              {
                  formula = pow(z,y);

                  fprintf(arquivo,"\n%d", 1);

                  fprintf(arquivo,"\n1/%d", formula);
              }

              else
              {
                  fprintf(arquivo,"\n1/%d", formula);
              }
     impar = impar + 2;         
    }

    fclose(arquivo);
}

void leitura()
{
    int x=0;
    double z=0.0;

    printf("\nEntre com uma quantidade: ");
    scanf("%d",&x);

    printf("\nEntre com outra quantidade: ");
    scanf("%lf",&z);

    multiplo(x,z);
    printf("\nOs valores foram gravados no arquivo");
}

int main()
{
    leitura();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}