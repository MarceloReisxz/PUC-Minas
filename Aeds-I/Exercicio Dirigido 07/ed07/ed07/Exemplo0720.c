/*
 Exemplo0720 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

int digito(char palavra[])
{

    int posicao = strlen (palavra);
    int controle = 0;
    int contador = 0;
    char letra;

    for (controle = 0; controle < posicao; controle = controle + 1)
    {
        letra = palavra[controle];
        
        if( letra>='7' && letra<='9' )
        {
            contador = contador + 1;
        }
    
    }
    
    return (contador);
}

void entrada()
{
    FILE* arquivo = fopen ("RESULTADO10.TXT", "wt");

   char palavra[80];
   int teste = 0;
   int y = 0;
   int contador = 0;

   printf("\nDigite uma quantidade: ");
   scanf("%d", &teste);

   for (y=0; y<teste; y=y+1)
   {

       printf("\nDigite uma palavra: ");
       scanf("%s", palavra);

       int contador = digito(palavra);

       fprintf(arquivo,"\nPalavra = %s\n", palavra);
       fprintf(arquivo,"\nDigitos maiores ou iguais a 7 = %d\n", contador);

       printf("\nOs valores foram gravados no arquivo.\n");
   
   } 

   fclose(arquivo);

}

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}
