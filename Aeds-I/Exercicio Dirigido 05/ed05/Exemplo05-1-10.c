/*
 Exemplo0501 - Exemplo0510 - v0.0. - 20 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
/**
 Method00 - nao faz nada.
*/
void method00 ( )
{
// nao faz nada
} // fim method00 ( )
/**
 Method01a - Mostrar certa quantidade de valores.
 @param x - quantidade de valores a serem mostrados
*/
void method01a ( int x )
{
// definir dado local
 int y = 1; // controle
// repetir enquanto controle menor que a quantidade desejada
 while ( y <= x )
 {
 // mostrar valor
 IO_printf ( "%s%d\n", "Valor = ", y );
 // passar ao proximo
 y = y + 1;
 } // fim se
} // fim method01a( )
/**
 Method01 - Mostrar certa quantidade de valores.
 OBS.: Preparacao e disparo de outro metodo.
*/
void method01 ( )
{
// identificar
 IO_id ( "EXEMPLO0501 - Method01 - v0.0" );
// executar o metodo auxiliar
 method01a ( 5 );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method01 ( )
/**
 Method02a - Mostrar certa quantidade de valores pares.
 @param x - quantidade de valores a serem mostrados
*/
void method02a ( int x )
{
// definir dado local
 int y = 1; // controle
 int z = 2;
// repetir enquanto controle menor que a quantidade desejada
 while ( y <= x )
 {
 // mostrar valor
 IO_printf ( "%d: %d\n", y, z );
 // passar ao proximo par
 z = z + 2;
 // passar ao proximo valor controlado
 y = y + 1;
 } // fim se
} // fim method02a( )
/**
 Method02.
*/
void method02 ( )
{
// identificar
 IO_id ( "EXEMPLO0502 - Method02 - v0.0" );
// executar o metodo auxiliar
 method02a ( 5 );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method02 ( )
/**
 Method03a - Mostrar certa quantidade de valores pares.
 @param x - quantidade de valores a serem mostrados
*/
void method03a ( int x )
{
// definir dado local
 int y = 1; // controle
 int z = 0;
// repetir enquanto controle menor que a quantidade desejada
 while ( y <= x )
 {
 // vincular o valor a ser mostrado ao controle
 z = 2 * y;
 // mostrar valor
 IO_printf ( "%d: %d\n", y, z );
 // passar ao proximo valor controlado
 y = y + 1;
 } // fim se
} // fim method03a( )
/**
 Method03.
*/
void method03 ( )
{
// identificar
 IO_id ( "EXEMPLO0503 - Method03 - v0.0" );
// executar o metodo auxiliar
 method03a ( 5 );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method03 ( )
/**
 Method04.
*/
/**
 Method04a - Mostrar certa quantidade de valores pares.
 @param x - quantidade de valores a serem mostrados
*/
void method04a ( int x )
{
// definir dado local
 int y = x; // controle
 int z = 0;
// repetir enquanto controle menor que a quantidade desejada
 while ( y > 0 )
 {
 // vincular o valor a ser mostrado ao controle
 z = 2 * y;
 // mostrar valor
 IO_printf ( "%d: %d\n", y, z );
 // passar ao proximo valor controlado
 y = y - 1;
 } // fim se
} // fim method04a( )
/**
 Method04.
*/
void method04 ( )
{
// identificar
 IO_id ( "EXEMPLO0504 - Method04 - v0.0" );
// executar o metodo auxiliar
 method04a ( 5 );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method04 ( )
/**
 Method05a - Mostrar certa quantidade de valores pares.
 @param x - quantidade de valores a serem mostrados
*/
void method05a ( int x )
{
// definir dado local
 int y = 0; // controle
// repetir enquanto controle menor que a quantidade desejada
 for ( y = x; y > 0; y = y-1 )
 {
 // mostrar valor
 IO_printf ( "%d: %d\n", y, (2*y) );
 } // fim se
} // fim method05a( )
/**
 Method05.
*/
void method05 ( )
{
// identificar
 IO_id ( "EXEMPLO0505 - Method05 - v0.0" );
// executar o metodo auxiliar
 method05a ( 5 );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method05 ( )
/**
 somarValores - funcao para somar certa quantidade de pares.
 @return soma dos valores
 @param x - quantidade de valores a serem mostrados
*/
int somarValores ( int x )
{
// definir dados locais
 int soma = 1;
 int y = 0; // controle
// repetir enquanto controle menor que a quantidade desejada
 for ( y = x-1; y > 0; y = y-1 )
 {
 // mostrar valor
 IO_printf ( "%d: %d\n", y, (2*y) );
 // somar valor
 soma = soma + (2*y);
 } // fim se
// retornar resultado
 return ( soma );
} // fim somarValores ( )
/**
 Method06.
*/
void method06 ( )
{
// definir dado
 int soma = 0;
// identificar
 IO_id ( "EXEMPLO0506 - Method06 - v0.0" );
// chamar e receber resultado da funcao
 soma = somarValores ( 5 );
// mostrar resultado
 IO_printf ( "soma de pares = %d\n", soma );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method06 ( )
/**
 somarFracao - funcao para somar certa quantidade de fracoes.
 @return soma dos valores
 @param x - quantidade de valores a serem mostrados
*/
double somarFracao ( int x )
{
// definir dados locais
 double soma = 1.0;
 double numerador = 0.0;
 double denominador = 0.0;
 int y = 0 ; // controle
// repetir enquanto controle menor que a quantidade desejada
 for ( y = x-1; y > 0; y = y-1 )
 {
 // calcular numerador
 numerador = 1.0;
 // calcular denominador
 denominador = 2.0*y;
 // mostrar valor
 IO_printf ( "%d: %7.4lf/%7.4lf = %lf\n",
 y, numerador, denominador, (numerador/denominador) );
 // somar valor
 soma = soma + (1.0)/(2.0*y);
 } // fim se
// retornar resultado
 return ( soma );
} // fim somarFracao ( )
/**
 Method07.
*/
void method07 ( )
{
// definir dado
 double soma = 0.0;
// identificar
 IO_id ( "EXEMPLO0507 - Method07 - v0.0" );
// chamar e receber resultado da funcao
 soma = somarFracao ( 5 );
// mostrar resultado
 IO_printf ( "soma de fracoes = %lf\n", soma );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method07 ( )
/**
 Method08.
*/
void method08 ( )
{
// definir dado
 double soma = 0.0;
// identificar
 IO_id ( "EXEMPLO0508 - Method08 - v0.0" );
// chamar e receber resultado da funcao
 soma = somarFracao ( 5 );
// mostrar resultado
 IO_printf ( "soma de fracoes = %lf\n", soma );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method08 ( )

/**
 somarFracao2 - funcao para somar certa quantidade de fracoes.
 @return soma dos valores
 @param x - quantidade de valores a serem mostrados
*/
double somarFracao2 ( int x )
{
// definir dados locais
 double soma = 1.0;
 int y = 0 ; // controle
// mostrar primeiro valor
 IO_printf ( "%d: %7.4lf/%7.4lf\n", 1, 1.0, soma );
// repetir enquanto controle menor que a quantidade desejada
 for ( y = 1; y <= (x-1); y = y+1 )
 {
 // mostrar valor
 IO_printf ( "%d: %7.4lf/%7.4lf = %7.4lf\n",
 y+1, (2.0*y), (2.0*y+1), ((2.0*y)/(2.0*y+1)) );
 // somar valor
 soma = soma + (2.0*y)/(2.0*y+1);
 } // fim se
// retornar resultado
 return ( soma );
} // fim somarFracao2 ( )
/**
 Method09.
*/
void method09 ( )
{
// definir dado
 double soma = 0.0;
// identificar
 IO_id ( "EXEMPLO0509 - Method09 - v0.0" );
// chamar e receber resultado da funcao
 soma = somarFracao2 ( 5 );
// mostrar resultado
 IO_printf ( "soma de fracoes = %lf\n", soma );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method09 ( )

/**
 multiplicarValores - funcao para multiplicar certa quantidade de valores impares.
 @return produto de valores
 @param x - quantidade de valores
*/
int multiplicarValores ( int x )
{
// definir dados locais
 int produto = 1;
 int y = 0; // controle
// repetir enquanto controle menor que a quantidade desejada
 for ( y = 1; y <= x; y = y+1 )
 {
 // mostrar valor
 IO_printf ( "%d: %d\n", y, (2*y-1) );
 // somar valor
 produto = produto * (2*y-1);
 } // fim se
// retornar resultado
 return ( produto );
} // fim multiplicarValores ( )
/**
 Method10.
*/
void method10 ( )
{
// identificar
 IO_id ( "EXEMPLO0510 - Method10 - v0.0" );
// mostrar produto de valores
 IO_printf ( "%s%d\n", "produto = ", multiplicarValores ( 5 ) );
// encerrar
 IO_pause ( "Apertar ENTER para continuar" );
} // fim method10 ( )
/*
 Funcao principal.
 @return codigo de encerramento
*/
int main ( )
{
// definir dado
 int x = 0; // definir variavel com valor inicial
// repetir até desejar parar
 do
 {
 // identificar
 IO_id ( "EXEMPLO0501 - Programa - v0.0" );

 // ler do teclado
 IO_println ( "Opcoes" );
 IO_println ( " 0 - parar" );
 IO_println ( " 1 - mostrar certa quantidade de valores" );
 IO_println ( " 2 - " );
 IO_println ( " 3 - " );
 IO_println ( " 4 - " );
 IO_println ( " 5 - " );
 IO_println ( " 6 - " );
 IO_println ( " 7 - " );
 IO_println ( " 8 - " );
 IO_println ( " 9 - " );
 IO_println ( "10 - " );
 IO_println ( "" );
 x = IO_readint ( "Entrar com uma opcao: " );

 // testar valor
 switch ( x )
 {
 case 0:
 method00 ( );
 break;
 case 1:
 method01 ( );
 break;
 case 2:
 method02 ( );
 break;
 case 3:
 method03 ( );
 break;
 case 4:
 method04 ( );
 break;
 case 5:
 method05 ( );
 break;
 case 6:
 method06 ( );
 break;
 case 7:
 method07 ( );
 break;
 case 8:
 method08 ( );
 break;
 case 9:
 method09 ( );
 break;
 case 10:
 method10 ( );
 break;
 default:
 IO_println ( "ERRO: Valor invalido." );
 } // fim escolher
 }
 while ( x != 0 );
// encerrar
 IO_pause ( "Apertar ENTER para terminar" );
 return ( 0 );
} // fim main( )
/*
---------------------------------------------- documentacao complementar
---------------------------------------------- notas / observacoes / comentarios
---------------------------------------------- previsao de testes
a.) 5 -> { 1, 2, 3, 4, 5 }
---------------------------------------------- historico
Versao Data Modificacao
 0.1 __/__ esboco
---------------------------------------------- testes
Versao Teste
 0.1 01. ( OK ) identificacao de programa
*/