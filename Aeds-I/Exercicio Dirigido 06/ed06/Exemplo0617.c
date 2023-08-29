/*
 Exemplo0617 - v0.0. - 28 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias
#include <math.h> // para definicoes proprias

/**
 impar
*/
double impar ( int x )
{
    double soma = 0.0;

    if ( x>0 )
    {
        int y = (2*x)+7;
        double z = 1.0/((2.0*x)+7.0);

        soma = z +  impar(x-1);
        printf("\n1/%d", y);       
        printf("\tResultado = %lf", z);
    }
    else
    {
        int y = (2*x)+7;
        double c = 1.0/7.0;
        
        printf("\n1/%d", y); //mostrar começando no 7
        printf("\tResultado = %lf", c); //mostrar começando no 7
        soma = soma + c;
    }

    return (soma);

}


/**
 entrada
*/
void entrada ( )
{
    int x = 0;
    double soma = 0.0;

    printf("\nEntre com um valor:");
    scanf("%d", &x);

    soma = impar(x);
    printf("\nSoma = %lf", soma);

} // fim entrada ( )

int main()
{
    entrada();
    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
}