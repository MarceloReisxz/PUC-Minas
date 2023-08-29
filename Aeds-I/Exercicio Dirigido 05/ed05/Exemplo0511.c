/*
 Exemplo0511 - v0.0. - 19 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias

void multiplo ( int x )
{
// definir dado local
 int y = 1; // controle
 int z = 1; // contagem
// repetir enquanto controle menor que a quantidade desejada
 while ( y <= x )
 {

     z = y * 7;
     y = y + 1;
     
     printf ( "\n[%d]", z );
 
 } // fim while
} // fim multiplo( )

void entrada ( )
{

//variaveis

int x=0;

// entrar com valor

printf("Entre com um valor inteiro:");
scanf("%d", &x);

// executar o metodo auxiliar

 multiplo ( x );

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