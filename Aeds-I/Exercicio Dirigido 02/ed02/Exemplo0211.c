/*
 Exemplo0211 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0211 exemplo0211.c
 Windows: gcc -o exemplo0211 exemplo0211.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0211
 Windows: exemplo0211
*/
// dependencias
#include "io.h" // para definicoes proprias
/*
 Funcao principal.
 @return codigo de encerramento
 @param argc - quantidade de parametros na linha de comandos
 @param argv - arranjo com o grupo de parametros na linha de comandos
*/
int main ( )
{
// definir dado
 int x; // definir variavel

// identificar
printf( "EXEMPLO0211 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%d", &x);

// testar valor
 if ( x%2 == 0 )
 {
   printf("\nEsse Numero e par!!");
 }
 else
 {
   printf ("\nEsse Numero e impar!! ");
    
 } // fim se

// encerrar
 printf( "\nApertar ENTER para terminar" );
 getchar();
 getchar();
 return ( 0 );

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
 0.1 01. ( OK )
*/
