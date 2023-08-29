/*
 Exemplo0317 - v0.0. - 06 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias

int main()
{
  int a=0;
  int b=0;
  int n=0;
  int x=0;
  int y=0;

  printf ( "Entrar com um valor do intervalo: " );
  scanf("%d", &a);

  printf ( "Entrar com um valor do intervalo: " );
  scanf("%d", &b);

  printf ( "Entrar com uma quantidade: " );
  scanf("%d", &n);

  for(y=1; y<=n; y=y+1)
  {
     printf ( "\nEntrar com um valor: " );
     scanf("%d", &x);

        if(x>a && x<b && x%5==0 || x<a && x>b && x%5==0)
        {
            printf ( "\nO valor %d e multiplo de 5 e esta no intervalo!\n", x );
        }
        else{
            printf ( "\nValor NAO multiplo de 5 ou fora do intervalo!\n" );
        }
  }

 printf("\nAperte ENTER para terminar");
 getchar();
 getchar();
 return  0 ;
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
 0.1 01. ( OK ) identificacao de programa
*/
