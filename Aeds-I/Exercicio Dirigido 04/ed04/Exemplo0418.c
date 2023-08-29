/*
 Exemplo0418 - v0.0. - 13 / 04 / 2022
 Author: Marcelo Reis Esteves

*/
// dependencias
#include "io.h" // para definicoes proprias

bool letra (char c)
{
    bool teste=false;

    if ( ! ((c>='a'  &&  c<='z'  )  ||  (c>='0'  &&  c<='9')  ||  (c>='A'  &&  c<='Z'  )) ) 

    {teste = true;}

    return (teste);
}

int palavra (char z[])
{
    int contador=0;
    char c;
    int posicao;
    int tamanho=0;
    tamanho= strlen (z);

  for(posicao=0; posicao<tamanho; posicao=posicao+1)
  {

      c=z[posicao];

      if( letra(c) )
      {
          contador = contador + 1;
          printf("\n[%d] %c", contador, c);
          
      }

  }


    return 0;
}

int main()
{
  char x[80];
  char c;
  int contador;
  int tamanho;
  int posicao;

  printf("Entre com uma cadeia de caracteres:");
  scanf ("%s", x);

 contador = palavra(x);


  printf("\nAperte ENTER para terminar");
  getchar();
  getchar();
  return 0;

}