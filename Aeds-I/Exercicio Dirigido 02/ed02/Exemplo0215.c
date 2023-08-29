/*
 Exemplo0215 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0215 exemplo0215.c
 Windows: gcc -o exemplo0215 exemplo0215.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0215
 Windows: exemplo0215
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
printf( "EXEMPLO0215 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%d", &x);

// testar valor

if (x>=10 && x<=25 && x>=20 && x<=40)
{
    printf("\nEsse numero se encontra dentro de dois intervalos\n");
}

else if (x>=10 && x<=25 || x>=20 && x<=40)
{
    printf("\nEsse numero se encontra dentro de um intervalo\n");
}

else
{
    printf("\nValor fora dos intervalos\n");
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
