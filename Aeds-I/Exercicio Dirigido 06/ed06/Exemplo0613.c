/*
 Exemplo0613 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 soma
*/
void soma ( int x )
{
    if ( x>0 )
    {
            
        soma(x-1);
        printf("\n%d", x*7);
      
        
    }
    else if ( x==0 )
    {
        printf("\n%d", 1);
    }
    
}


/**
 entrada
*/
void entrada ( )
{
    int x = 0;

    printf("\nEntre com um valor:");
    scanf("%d", &x);

    soma(x);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}