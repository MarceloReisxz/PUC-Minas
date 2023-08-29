/*
 Exemplo0612 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 multiplo
*/
void multiplo ( int x )
{
    if ( x>0 )
    {
        int z = 0;
        z = 7 * x;

        if (z%7==0)
        {
            
        printf("\n%d", z);
        multiplo(x-1);
        }
        
        
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

    multiplo(x);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}