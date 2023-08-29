/*
 Exemplo0618 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

void entrada()
{
   int quantidade = 0;
   int resposta = 1;
   int fibpar ( int x );

   printf("Digite um numero par\n");

   scanf("%i", &quantidade);

   int aux = quantidade;

   while ( resposta % 2 != 0 )
   {
      resposta = fibpar  (aux);
      aux ++;
   }
   printf("O termo numero %i, par de fibonacci e %i\n",quantidade, resposta);
      
 }
 int fibpar(int x)
 {
    int fibonaccipar ( int x );
    int resposta = 1;
    int contador = 0;
    int aux = x;
        while (contador < x)
    {
       resposta = fibonaccipar ( aux );
       printf("%i - ", resposta);
       if ( resposta % 2 == 0 )
       {
         contador++;
         printf("\nContador =%i\n", contador);
       }
       aux++;
    }
 return resposta;
 }
 int fibonaccipar ( int x ) 
{      
   int resposta = 0; 
   if ( x == 1 || x == 2 )    
   {           
      resposta = 1; 
   } 
   else  
   {     
      if ( x > 1 )       
      {             
         resposta = fibonaccipar ( x-1 ) + fibonaccipar ( x-2 );       
      }      
   }  
   return ( resposta );
}


int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}
