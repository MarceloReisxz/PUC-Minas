/*
 Exemplo0816 - v0.0. - 03 / 05 / 2022
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


void task(char filename[])
{

 FILE*arquivo = fopen(filename, "rt");
 FILE*arquivo2 = fopen("ACIMA_MEDIA.txt", "wt");
 FILE*arquivo3 = fopen("ABAIXO_MEDIA.txt", "wt");

// definir dado local

int y = 0;
int z = 0;
fscanf ( arquivo, "%d", &y );

int arranjo[y];
int controle = 0;
double  total = 0.0;
double  media = 0.0;

 for(controle = 0; controle<y; controle = controle +1)
 {
 // ler valor
 fscanf ( arquivo, "%d", &z );

 
     arranjo[controle] = z;
     total = total + z;
     

     
 }


 media = (total + 1.0) / (y + 1.0);

 printf("\n");
 printf("\nVALOR MEDIA = %lf", media);
 printf("\n");

 printf("\nValores acima ou iguais a media = \n");

for(controle = 0; controle<y; controle = controle +1)
 {
 
     if (arranjo[controle]>=media)
     {
         printf("\n%d", arranjo[controle]);
         fprintf(arquivo2,"\n%d", arranjo[controle]);
     } 

 }

 printf("\n");

 printf("\nValores abaixo da media = \n");

 for(controle = 0; controle<y; controle = controle +1)
 {
 
     if (arranjo[controle]<media)
     {
         printf("\n%d", arranjo[controle]);
         fprintf(arquivo3,"\n%d", arranjo[controle]);
     } 

 }

 printf("\n");
 printf("\nOs valores foram gravados em seus arquivos");
 fclose(arquivo);
 fclose(arquivo2);
 fclose(arquivo3);

}


int main()
{
    char filename[80];

    printf("\nEntre com o nome do arquivo que quer ler:");
    scanf("%s", filename);

    task(filename);

    getchar();
    getchar();
    return 0;
}