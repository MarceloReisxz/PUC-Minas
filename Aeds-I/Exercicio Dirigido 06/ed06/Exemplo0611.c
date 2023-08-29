/*
 Exemplo0611 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 impar
*/
void impar ( int x )
{
    if ( x>0 )
    {
        impar(x-1);
        printf("\n%d", (2*x)+7);
    }
    else
    {
        printf("\n%d", 7); //mostrar começando no 7
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

    impar(x);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}