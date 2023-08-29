/*
 Exemplo0412 - v0.0. - 13 / 04 / 2022
 Author: Marcelo Reis Esteves

*/
// dependencias
#include "io.h" // para definicoes proprias

bool maiuscula (char c)
{
    bool teste=false;

    if ('A'<= c && c<='K')

    {teste = true;}

    return (teste);
}

int main()
{
  char x[80];
  char c;
  int contador;
  int tamanho;
  int posicao;

  printf("Entre com uma palavra:");
  scanf ("%s", x);

  tamanho= strlen (x);

  for(posicao=0; posicao<tamanho; posicao=posicao+1)
  {
      c=x[posicao];

      if( maiuscula(c) )
      {
          printf("%c\n", c);
          contador = contador + 1;
      }


  }

  printf("\nMaiusculas:%d", contador);


  printf("\nAperte ENTER para terminar");
  getchar();
  getchar();
  return 0;

}
