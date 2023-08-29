/*
 Exemplo0311 - v0.0. - 04 / 04 / 2022
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
  

  printf( "Entrar com uma palavra: " );
  scanf("%s", &x);

  tamanho= strlen (x);


  for(posicao=0; posicao<tamanho; posicao=posicao+1)
  {
      c= x[posicao];

      if(c>='a' && c<='z')
      {
      printf("\n %c", c);
      } 
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
