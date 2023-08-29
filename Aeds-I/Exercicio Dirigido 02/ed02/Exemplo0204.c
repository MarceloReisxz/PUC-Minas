/*
 Exemplo0204 - v0.0. - 31 / 03 / 2022
 Author: Marcelo Reis Esteves
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
 double x = 0.0; // definir variavel com valor inicial
// identificar
 IO_id ( "EXEMPLO0204 - Programa - v0.0" );
// ler do teclado
 x = IO_readdouble ( "Entrar com um valor real: " );
// testar valor
 if ( 1.0 <= x && x <= 10.0 )
 {
 IO_printf ( "%s (%lf)\n", "Valor dentro do intervalo [1:10] ", x );
 }
 else
 {
 IO_printf ( "%s (%lf)\n", "Valor fora do intervalo [1:10] ", x );
 if ( x < 1.0 )
 {
 IO_printf ( "%s (%lf)\n", "Valor abaixo do intervalo [1:10] ", x );
 }
 else
 {
 IO_printf ( "%s (%lf)\n", "Valor acima do intervalo [1:10]", x );
 } // fim se
 } // fim se
// encerrar
 IO_pause ( "Apertar ENTER para terminar" );
 return ( 0 );
} // fim main( )
/*
---------------------------------------------- documentacao complementar
---------------------------------------------- notas / observacoes / comentarios
---------------------------------------------- previsao de testes
a.) 0
b.) 1
c.) 10
d.) -1
e.) 100
---------------------------------------------- historico
Versao Data Modificacao
 0.1 __/__ esboco
---------------------------------------------- testes
Versao Teste
 0.1 01. ( OK ) identificacao de programa
*/
