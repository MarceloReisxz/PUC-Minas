/*
 Exemplo0615 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 sequencia
*/
void sequencia ( char palavra[], int x )
{
    char c;
    c= palavra[x];
    
    if (x>=0 )
    {

        sequencia(palavra, x-1);
        printf("\n%c", c );
        
      
        
    }
    
}


/**
 entrada
*/
void entrada ( )
{
    char palavra[80];

    printf("\nEntre com um valor:");
    scanf("%s", palavra);

    int x = strlen(palavra);

    sequencia(palavra, x);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}