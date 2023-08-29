/*
 Exemplo0113 - v0.0. - 29 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0113 exemplo0113.c
 Windows: gcc -o exemplo0113 exemplo0113.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0113
 Windows: exemplo0113
*/
// dependencias
#include <stdio.h> // para as entradas e saidas
#include <math.h>
/*
 Funcao principal.
 @return codigo de encerramento
 @param argc - quantidade de parametros na linha de comandos
 @param argv - arranjo com o grupo de parametros na linha de comandos
*/
int main ( )
{
// definir dado
 int lado1;
 int lado2;
 int area;
 int terco;
 

// identificar
 printf ( "%s\n", "Exemplo0113 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s","De o valor de um lado do retangulo: ");
 scanf ( "%d", &lado1 );

 printf ("\n");

 printf ( "%s","De o valor de outro lado do retangulo: ");
 scanf ( "%d", &lado2 );

 area= lado1 * lado2;

 printf ("\n");

 printf ("%s%d\n","Valor da area do retangulo= ", area);

 terco= area / 3;
 printf ("%s%d\n","Valor do terco da area= ", terco);

 
 getchar ( ); // OBS.: Limpar a entrada de dados
 printf ( "\n\nApertar ENTER para terminar." );
 getchar( ); // aguardar por ENTER
 return ( 0 ); // voltar ao SO (sem erros)
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