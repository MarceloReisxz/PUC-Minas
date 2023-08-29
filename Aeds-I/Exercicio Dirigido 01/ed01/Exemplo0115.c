/*
 Exemplo0115 - v0.0. - 29 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0115 exemplo0115.c
 Windows: gcc -o exemplo0115 exemplo0115.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0115
 Windows: exemplo0115
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
 int base;
 int altura;
 int area;
 int perimetro;
 

// identificar
 printf ( "%s\n", "Exemplo0115 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s","De o valor da base do triangulo: ");
 scanf ( "%d", &base );

 printf ("\n");

 printf ( "%s","De o valor da altura do triangulo: ");
 scanf ( "%d", &altura );

 printf ("\n");

 area= (base * (altura/5)) /2;
 printf ("%s%d\n\n","Area do triangulo com um quinto de sua altura= ", area);

 
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