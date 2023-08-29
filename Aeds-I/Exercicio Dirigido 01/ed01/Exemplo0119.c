/*
 Exemplo0119 - v0.0. - 30 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0119 exemplo0119.c
 Windows: gcc -o exemplo0119 exemplo0119.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0119
 Windows: exemplo0119
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
 double raio;
 double area;
 double alterado;

// identificar
 printf ( "%s\n", "Exemplo0119 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha

 printf ( "%s","De o valor do raio: ");
 scanf ( "%lf", &raio);

 printf ("\n");

 alterado= raio/2;
 area= (pow(alterado,2))*M_PI;
 printf ("%s%lf\n\n","A area do circulo com metade do raio= ", area);

 
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