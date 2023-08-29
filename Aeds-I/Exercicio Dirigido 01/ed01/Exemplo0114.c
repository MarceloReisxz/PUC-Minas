/*
 Exemplo0114 - v0.0. - 29 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0114 exemplo0114.c
 Windows: gcc -o exemplo0114 exemplo0114.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0114
 Windows: exemplo0114
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
 int perimetro;
 

// identificar
 printf ( "%s\n", "Exemplo0114 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s","De o valor do lado do retangulo: ");
 scanf ( "%d", &lado1 );

 printf ("\n");

 printf ( "%s","De o valor de outro lado do retangulo: ");
 scanf ( "%d", &lado2 );

 printf ("\n");

 area= (lado1 * 2) * (lado2 * 2);
 printf ("%s%d\n\n","Area com o dobro do valor dos lados= ", area);

 perimetro = ((lado1 * 2) + (lado2 * 2)) *2;
 printf ("%s%d\n\n","Perimetro de um retangulo com o dobro do valor dos lados= ", perimetro);

 
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