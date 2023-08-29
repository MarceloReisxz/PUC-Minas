/*
 Exemplo0620 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

void entrada ()
{
   int contadormaiusculas(char c[], int x);
   char c[81];
   printf("Digite uma cadeia:");
   scanf("%s", c);
   printf("O total de letras maiusculas e %i\n ", contadormaiusculas(c, strlen(c)));

}

int contadormaiusculas(char c[], int x)
{
   int contador = 0;
   if (x >= 0)
   {
      contador = contador + contadormaiusculas(c, x-1);
      if(c[x] >='A' && c[x] <= 'Z')
      {
         contador++;
      }
     
   }
   return contador;
}
int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}