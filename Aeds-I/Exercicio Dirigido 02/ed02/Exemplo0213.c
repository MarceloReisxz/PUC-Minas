/*
 Exemplo0213 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0213 exemplo0213.c
 Windows: gcc -o exemplo0213 exemplo0213.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0213
 Windows: exemplo0213
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
 int x; // definir variavel

// identificar
printf( "EXEMPLO0213 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%d", &x);

// testar valor
if (x>25 && x<40)
{
    printf("\nEsse numero se encontra dentro do intervalo\n");
}

else{
    printf("\nValor invalido\n");
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
