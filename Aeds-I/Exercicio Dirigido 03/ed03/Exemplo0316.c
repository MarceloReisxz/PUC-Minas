/*
 Exemplo0316 - v0.0. - 06 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias

int main()
{
  char x[80];
  char c='0';
  int tamanho=0;
  int posicao=0;

  printf ( "Entrar com uma palavra: " );
  scanf("%s", &x);

  tamanho = strlen (x);

  for(posicao=0; posicao<tamanho; posicao=posicao+1)
  {
    c= x [posicao];
      if(!((c>='a' && c<='z') ||
           (c>='A' && c<='Z') ||
           (c>='0' && c<='9')))
    {

      printf("%d. %c\n", posicao, c);

    }
  }
 printf("\nAperte ENTER para terminar");
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
 0.1 01. ( OK ) identificacao de programa
*/
