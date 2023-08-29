/*
 Exemplo0411 - v0.0. - 12 / 04 / 2022
 Author: Marcelo Reis Esteves

*/
// dependencias
#include "io.h" // para definicoes proprias

int main()
{
    double x=0;
    double y=0;
    double teste=0;


    printf("\nValor para o intervalo:");
    scanf("%lf", &x);

    printf("\nValor para o intervalo:");
    scanf("%lf", &y);

    printf("\nEntre com um valor:");
    scanf("%lf", &teste);

          if( teste>=x  &&  teste<=y  ||  teste<=x  &&  teste>=y)
          {
              printf("\nO valor esta DENTRO do intervalo");
          }
          else
          {
              printf("\nO valor esta FORA do intervalo");
          }


    printf("\nAperte ENTER para terminar");
    getchar();
    getchar();
    return 0;

}