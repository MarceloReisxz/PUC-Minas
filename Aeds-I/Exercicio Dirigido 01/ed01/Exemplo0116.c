/*
 Exemplo0116 - v0.0. - 30 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0116 exemplo0116.c
 Windows: gcc -o exemplo0116 exemplo0116.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0116
 Windows: exemplo0116
*/
// dependencias
#include <stdio.h> // para as entradas e saidas
/*
 Funcao principal.
 @return codigo de encerramento
 @param argc - quantidade de parametros na linha de comandos
 @param argv - arranjo com o grupo de parametros na linha de comandos
*/
int main ( )
{
// definir dado
double lado = 0.0;
double area = 0.0;
double perimetro = 0.0;
double altura =0.0;


 printf ( "%s\n", "Exemplo0116 - Programa = v0.0" );
 printf ( "%s\n", "Autor: Marcelo Reis" );
 printf ( "\n" ); // mudar de linha
// mostrar valor inicial
 printf ( "%s", "Entre com o valor do lado do triangulo=");
 scanf ( "%lf", &lado );

 area= ((lado/2.0)*(lado/2.0))/2;
 perimetro= (lado/2.0)*3.0;
 altura= ((lado/2.0)+(lado/2.0)+(lado/2.0))/2.0;

 printf ( "%s%lf\n", "Area=", area );
 printf ( "%s%lf\n", "Perimetro=", perimetro );
 printf ( "%s%lf\n", "Altura=", altura );


// encerrar
 printf ( "\n\nApertar ENTER para terminar." );
 getchar( ); // aguardar por ENTER
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
