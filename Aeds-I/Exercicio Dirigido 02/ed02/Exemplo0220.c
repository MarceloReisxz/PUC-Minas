/*
 Exemplo0220 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0220 exemplo0220.c
 Windows: gcc -o exemplo0220 exemplo0220.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0220
 Windows: exemplo0220
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
 double x; // definir variavel
 double y; // definir variavel
 double z; // definir variavel
// identificar
printf( "EXEMPLO0220 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &x);

printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &y);

printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &z);

// testar valor
if (y!=z && y!=x && z!=x && x>=z && x>=y)
{
    printf("\nO primeiro numero NAO esta entre os outros dois!\n");
}

else if (y!=z && y!=x && z!=x && x<=z && x<=y)
{
    printf("\nO primeiro numero NAO esta entre os outros dois!\n");
}

else
{
    printf("\nO primeiro numero ESTA entre os outros dois OU ha valores iguais!\n");
}

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
