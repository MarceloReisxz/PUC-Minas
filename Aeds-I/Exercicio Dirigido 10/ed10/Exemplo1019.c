/*
 Exemplo1019 - v0.0. - 28 / 05 / 2022
 Author: Marcelo Reis Esteves
*/

#include "io.h"
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

int lerArquivo(char* filename, int linhas, int colunas, int matriz[linhas][colunas])
{
    FILE* arquivo = fopen (filename, "rt");
    int x = 0;
    int y = 0;
    int z = 0;

 for (x=0; x<linhas; x= x+1)
 {
     for (y=0; y<colunas; y= y+1)
     {
          // ler valor
                fscanf ( arquivo, "%d", &z );

          // guardar valor
                matriz [ x ][ y ] = z;
     }
     
 }

    fclose(arquivo);

    return(matriz[linhas][colunas]);

}

 void soma(int linhas, int colunas, int matriz[linhas][colunas], int matriz2[linhas][colunas] )
 {
     int x = 0;
     int y = 0;
     bool igualdade = true;
     int matriz3[linhas][colunas];
     
     for ( x = 0; x < linhas; x++)
     {
         for ( y = 0; y < linhas; y++)
         {
             matriz3[x][y] = matriz[x][y] + matriz2[x][y];  
         }
         
     }

     printf("\n");

     for ( x = 0; x < linhas; x++)
     {
         for ( y = 0; y < linhas; y++)
         {
             printf("%d\t", matriz3[x][y]);
         }

         printf("\n");
         
     }
     
     
 }


int main()
{
    char filename[80];
    char filename2[80];
    int colunas = 0;
    int linhas = 0;

    printf("\nEntre com a quantidade de colunas: ");
    scanf("%d", &colunas);

    printf("\nEntre com a quantidade de linhas: ");
    scanf("%d", &linhas);

    int matriz[linhas][colunas];
    int matriz2[linhas][colunas];

    printf("\nEntre com o nome do arquivo: ");
    scanf("%s", filename);

    printf("\nEntre com o nome do segundo arquivo: ");
    scanf("%s", filename2);

    lerArquivo(filename, linhas, colunas, matriz);

    lerArquivo(filename2, linhas, colunas, matriz2);

        soma(linhas, colunas, matriz, matriz2);

    printf("\n");

    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
    return 0;
}