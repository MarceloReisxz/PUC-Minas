/*
 Exemplo0320 - v0.0. - 06 / 04 / 2022
 Author: Marcelo Reis Esteves
*/
// dependencias
#include "io.h" // para definicoes proprias

int main()
{
  double a=0;
  double b=0;
  double n=0;
  double x=0;
  int y=0;
  double z=0;

  printf ( "Entrar com um valor do intervalo: " );
  scanf("%lf", &a);

  printf ( "Entrar com um valor do intervalo: " );
  scanf("%lf", &b);

 if(a>0 && a<1  && b>0 && b<1)
 {
    printf ( "Entrar com uma quantidade: " );
    scanf("%lf", &n);

    for(y=1; y<=n; y=y+1)
    {
       printf ( "\nEntrar com um valor: " );
       scanf("%lf", &x);
       
           z=  x - (int)x;

        if(!(z>a && z<b || z<a && z>b))
        {
            printf ( "\nO valor %lf esta CORRETO!\n", z );
        }
        else{
            printf ( "\nValor %lf esta ERRADO!\n", z );
        }

  }
}

 printf("\nAperte ENTER para terminar");
 getchar();
 getchar();
 return  0 ;
} // fim main( )
/*
---------------------------------------------- documentacao complementar
---------------------------------------------- notas / observacoes / comentarios
---------------------------------------------- previsao de testes
---------------------------------------------- historico
Versao Data Modificacao
 0.1 __/__ esboco
---------------------------------------------- testes
Versao Teste
 0.1 01. ( OK ) identificacao de programa
*/
