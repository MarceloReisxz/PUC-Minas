/*
 Exemplo0517 - v0.0. - 20 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

void multiplo ( int n, int x )
{
// definir dado local
 int y = 1; // controle
 int z = 0;
 int w = 0;
 double soma = 0.0;
 double fracao = 0.0;
 

 

// repetir enquanto controle menor que a quantidade desejada
 while ( y <= n )
 {
         
         z = 7 + w;

     if (z%3!=0 && z>0)
     {
         
        
         fracao = 1.0 / (z * 1.0);
         printf("\n[1/%d ", z);
         printf("= %lf]", fracao);
         soma = soma + fracao;
     }
     else
     {
         y = y - 1;
     }

   w = w + 2;
   
   
   y = y + 1;

 }
 
       printf("\nSoma:[%lf]", soma);

} // fim multiplo( )

void entrada ( )
{

//variaveis

int x=0;
int controle=0;
int n=0;

// entrar com valor

printf("\nEntre com a quantidade:");
scanf("%d", &x);

for (controle=0; controle<x; controle=controle+1)
{
   printf("\nEntre com um valor:");
scanf("%d", &n);

multiplo ( n, x);
}

// encerrar

 printf( "\nApertar ENTER para continuar" );
 getchar();
 getchar();

} // fim method01 ( )

int main ( )
{
    entrada();

} // fim main( )
/*
---------------------------------------------- documentacao complementar
---------------------------------------------- notas / observacoes / comentarios
---------------------------------------------- previsao de testes
---------------------------------------------- historico
Versao Data Modificacao
 0.1 __/__ esboco
---------------------------------------------- testes
Versao Teste
 0.1 01. ( OK ) identificacao de programa
*/
