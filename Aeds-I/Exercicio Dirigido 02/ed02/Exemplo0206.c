/*
 Exemplo0206 - v0.0. - 31 / 03 / 2022
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
 char x = '_'; // definir variavel com valor inicial
// identificar
 IO_id ( "EXEMPLO0206 - Programa - v0.0" );
// ler do teclado
 x = IO_readchar ( "Entrar com um caractere: " );
// testar valor
 if ( ( 'a' <= x && x <= 'z' ) || // minuscula OU
 ( 'A' <= x && x <= 'Z' ) ) // maiuscula
 {
 IO_printf ( "%s (%c)\n", "Letra", x );
 }
 else
 {
 IO_printf ( "%s (%c)\n", "Valor diferente de letra", x );
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