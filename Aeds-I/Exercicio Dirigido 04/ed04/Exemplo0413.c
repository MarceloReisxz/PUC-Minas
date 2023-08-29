/*
 Exemplo0413 - v0.0. - 13 / 04 / 2022
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

int maiusculas (char z[])
{
    int contador=0;
    char c;
    int posicao;
    int tamanho=0;
    tamanho= strlen (z);

  for(posicao=0; posicao<tamanho; posicao=posicao+1)
  {

      c=z[posicao];

      if( maiuscula(c) )
      {
          contador = contador + 1;
      }

  }


    return (contador);
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

 contador = maiusculas(x);

  printf("\nMaiusculas:%d", contador);


  printf("\nAperte ENTER para terminar");
  getchar();
  getchar();
  return 0;

}

