/*
 Exemplo0812 - v0.0. - 03 / 05 / 2022
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


void task(int x, int arranjo[], char filename[])
{
 FILE*arquivo = fopen(filename, "rt");
// definir dado local
 int controle = 0;
 int y = 0;
 int copia;

// ler a quantidade de dados
 fscanf ( arquivo, "%d", &copia );
 if ( x <= 0 || x > copia )
 {
   printf ( "ERRO: Valor invalido." );
 }
 else
 {
 // ler e guardar valores em arranjo
 copia = 0;
 while ( ! feof ( arquivo ) && copia < x )
 {
 // ler valor
 fscanf ( arquivo, "%d", &y );
 printf("\n%d", y);
 // guardar valor
 arranjo [ copia ] = y;
 // passar ao proximo
 copia = copia+1;
 } // fim repetir
 } // fim se
 fclose(arquivo);


}


int main()
{
    int x = 0;
    char filename[80];
    
    printf("\nEntre com um valor:");
    scanf("%d", &x);

    printf("\nEntre com o nome do arquivo que quer ler:");
    scanf("%s", filename);
    
    int arranjo[x];

    task(x,arranjo,filename);

    getchar();
    getchar();
    return 0;
}