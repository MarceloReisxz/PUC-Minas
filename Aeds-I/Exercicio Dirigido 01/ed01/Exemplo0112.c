/*
 Exemplo0112 - v0.0. - 29 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0112 exemplo0112.c
 Windows: gcc -o exemplo0112 exemplo0112.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0112
 Windows: exemplo0112
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
 int lado;
 int area;
 int perimetro;
 

// identificar
 printf ( "%s\n", "Exemplo0112 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s","De o valor do lado do quadrado: ");
 scanf ( "%d", &lado );

 printf ("\n");

 area= (lado * 3)*(lado * 3);
 printf ("%s%d\n\n","Valor da area de um quadrado com o triplo do lado= ", area);

 perimetro = (lado * 3) * 4;
 printf ("%s%d\n\n","Valor do perimetro de um quadrado com o triplo do lado= ", perimetro);

 
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