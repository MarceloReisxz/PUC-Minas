/*
 Exemplo0616 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 impar
*/
int impar ( int x )
{
    int soma = 0;

    if ( x>0 )
    {
        int z = (2*x)+7;
        soma = z +  impar(x-1);       
        printf("\n%d", z);
    }
    else
    {
        printf("\n%d", 7); //mostrar começando no 7
    }

    return (soma);

}


/**
 entrada
*/
void entrada ( )
{
    int x = 0;
    int soma = 0;

    printf("\nEntre com um valor:");
    scanf("%d", &x);

    soma = impar(x);
    printf("\nSoma = %d", soma + 7);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}