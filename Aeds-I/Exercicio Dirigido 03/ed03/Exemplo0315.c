/*
 Exemplo0315 - v0.0. - 05 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias

int main()
{
  char x[80];
  int tamanho;
  int posicao;
  char c;
  

  printf( "Entrar com alguns caracteres: " );
  scanf("%s", &x);

  tamanho= strlen (x);


  for(posicao=tamanho; posicao>=0; posicao=posicao-1)
  {
      c= x[posicao];
      printf("\n[%d]. %c", posicao, c);

  }


printf("\nAperte ENTER para terminar.");
getchar();
getchar();
return 0;
}

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
