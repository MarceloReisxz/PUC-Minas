/*
 Exemplo0217 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves

 Para compilar em terminal (janela de comandos):
 Linux : gcc -o exemplo0217 exemplo0217.c
 Windows: gcc -o exemplo0217 exemplo0217.c
 Para executar em terminal (janela de comandos):
 Linux : ./exemplo0217
 Windows: exemplo0217
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
 int y; // definir variavel
// identificar
printf( "EXEMPLO0217 - Programa - v0.0\n" );

// ler do teclado
printf( "\nEntrar com um valor inteiro: " );
scanf("%d", &x);

printf( "\nEntrar com um valor inteiro: " );
scanf("%d", &y);
// testar valor

if (x%2==0 && x<0)
{
    printf("\nO primeiro numero e par,negativo!\n");
}

else
{
    printf("\nValor invalido para o primeiro!\n");
}

if  (y%2!=0 && y>=0) 
{
    printf("\nO segundo numero e impar,positivo!\n");
}
else
{
    printf("\nValor invalido para o segundo!\n");
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
