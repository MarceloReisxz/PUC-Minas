/*
 Exemplo0815 - v0.0. - 03 / 05 / 2022
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

// definir dado local

int y = 0;
int z = 0;
fscanf ( arquivo, "%d", &y );

int arranjo[y];
int controle = 0;
int maior = 0;

 for(controle = 0; controle<y; controle = controle +1)
 {
 // ler valor
 fscanf ( arquivo, "%d", &z );

 
     arranjo[controle] = z;
     printf("\n%d", arranjo[controle]);
     maior = z;

     
 }

 
for(controle = 0; controle<y; controle = controle +1)
 {
 
     if (arranjo[controle]>maior)
     {
         maior = arranjo[controle];
     } 

 }

printf("\n");
printf("\nMAIOR VALOR = %d", maior);



 fclose(arquivo);
 
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