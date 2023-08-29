/*
 Exemplo0118 - v0.0. - 30 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0118 exemplo0118.c
 Windows: gcc -o exemplo0118 exemplo0118.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0118
 Windows: exemplo0118
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
 double largura;
 double comprimento;
 double altura;
 double volume;
 

// identificar
 printf ( "%s\n", "Exemplo0118 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s","De o valor do comprimento: ");
 scanf ( "%lf", &comprimento );

 printf ( "%s","De o valor da largura: ");
 scanf ( "%lf", &largura );

 printf ( "%s","De o valor da altura: ");
 scanf ( "%lf", &altura );

 printf ("\n");

volume= (largura*6.0)*(comprimento*6.0)*(altura*6.0);
 printf ("%s%lf\n\n","Seis vezes o volume do paralelepipedo= ", volume);

 
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