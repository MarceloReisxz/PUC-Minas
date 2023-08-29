/*
 Exemplo0717 - v0.0. - 03 / 05 / 2022
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
    FILE* arquivo = fopen ( "RESULTADO04.TXT", "r" );
    int y = 1;
    int z = 0;
    double soma = 0.0;
    int formula = 0;
 
    while ( ! feof ( arquivo ) && y < x )
 {

  formula = pow(3,y);
  
 // tentar ler
  
  fscanf ( arquivo, "%d", &z );

  soma = soma + (z * 1.0) / (formula * 1.0);

  y = y +1;
 
 }
 
    fclose(arquivo);

    FILE* arquivo2 = fopen ( "RESULTADO07.TXT", "wt" );

    fprintf(arquivo2,"\nQuantidade = %d", x);
    fprintf(arquivo2,"\nSoma = %lf", soma);

    fclose(arquivo2);
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