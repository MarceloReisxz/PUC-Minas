/*
 Exemplo0614 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 sequencia
*/
void sequencia ( int x )
{
    if ( x>0 )
    {
        int z = pow(7,x);
            
        printf("\n1/%d", z);
        sequencia(x-1);
      
        
    }
    else
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

    sequencia(x);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}