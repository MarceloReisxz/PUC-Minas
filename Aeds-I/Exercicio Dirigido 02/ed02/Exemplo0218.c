/*
 Exemplo0218 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0218 exemplo0218.c
 Windows: gcc -o exemplo0218 exemplo0218.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0218
 Windows: exemplo0218
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
// identificar
printf( "EXEMPLO0218 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &x);

printf( "\nEntrar com um valor inteiro: " );
scanf("%lf", &y);
// testar valor

if (y==x)
{
    printf("\nO segundo numero e igual ao primeiro\n");
}

else if (y>x)
{
    printf("\nO segundo numero e maior do que o primeiro\n");
}

else if (y<x)
{
    printf("\nO segundo numero e menor que o primeiro\n");
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
