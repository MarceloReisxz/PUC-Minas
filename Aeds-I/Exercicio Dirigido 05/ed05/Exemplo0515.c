/*
 Exemplo0515 - v0.0. - 20 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

void multiplo ( int n, double x )
{
// definir dado local
 int y = 1; // controle
 int z = 1;
 double w= 0.0;
 

// repetir enquanto controle menor que a quantidade desejada
 while ( y <= n )
 {
     if (w == 0.0)
     {
         printf("[1]");
         y = y + 1;
     }
     
         w = w + 1.0;

         z = pow(x, w);
        
         printf("[1/%d]", z);


   y = y + 1;
 }
} // fim multiplo( )

void entrada ( )
{

//variaveis

double x=0.0;
int n=0;

// entrar com valor

printf("Entre com um valor real:");
scanf("%lf", &x);

printf("Entre com um valor inteiro:");
scanf("%d", &n);

// executar o metodo auxiliar

 multiplo ( n, x );

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
