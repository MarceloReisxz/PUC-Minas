/*
 Exemplo0716 - v0.0. - 03 / 05 / 2022
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
    FILE* arquivo = fopen ( "RESULTADO06.TXT", "wt" );

    int y = 0;
    int formula = 0;
    int impar = 1;
    double soma = 0.0;

    for(y=1; y<x; y=y+1)
    {
                  formula = pow(z,impar);

                  soma = soma + 1.0/formula;

                  fprintf(arquivo,"\n1/%d = %lf", formula, 1.0/formula);

                  impar = impar + 2;  

    }

    fprintf(arquivo,"\nSoma das frações = %lf", soma);

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