/*
 Exemplo0619 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

void entrada()
{
   char c[81];
   int contardorpares(char i[],int x, int y);
   printf("Digite uma cadeia:");
   scanf("%s",c);
   int total = contardorpares(c, strlen(c), 0);
   printf("O total de pares e %i \n", total);
   
}
int contardorpares(char i[],int x, int y)
{
   int contador = 0;
   if( x > 0)
   {
      contador = contardorpares(i, x-1 , y+1);
      if (i[y] >= '0' && i[y] <= '9' &&  (int)i[y] % 2 == 0)
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