/*
 Exemplo0219 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0219 exemplo0219.c
 Windows: gcc -o exemplo0219 exemplo0219.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0219
 Windows: exemplo0219
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
printf( "EXEMPLO0219 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &x);

printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &y);

printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &z);

// testar valor
if (y!=z && x>z && x<y)
{
    printf("\nO primeiro numero esta entre os outros dois!\n");
}

else if (y!=z && x<z && x>y)
{
    printf("\nO primeiro numero esta entre os outros dois!\n");
}

else
{
    printf("\nO primeiro numero NAO esta entre os outros dois!\n");
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
