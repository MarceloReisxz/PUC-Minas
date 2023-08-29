#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void questao1()
{
    bool b=false;
    int x=0;
    double d=0.0;
    char c='0';

    b=(x<=5)&&(d<=1/2);
    c=(char)(((int)'0'+1)-48);
    d=7/8+(int)(double)3/4;
    x=(int)(M_PI*1.0)/3;

    printf("\nb = %d", b);
    printf("\nc = %d", c);
    printf("\nd = %d", d); //resposta certa
    printf("\nx = %d", x);


}

void questao2()
{

    int x=0;
    int y=0;
    int n=5;

    y=n*(n+1)/2+1;

    for(x=1; x<=n; x=x+1)
    {

        y=y-x;
        printf("\n%d",y);
    }


}

void questao3()
{
    for(int x=1; x<=5; x=x+1)
    {
       printf("\nx = %d", 2*x-1);
    }

    printf("\n");

    for(int x=1; x<=5*3; x=x+3)
    {
        printf("\nx = %d", x-x/3);
    }
}

void questao4()
{
    int a=10;
    int b=20;
    int c=30;
    int maior=0;

    if(c>b>a||c>a>b)
    {
        maior=c;
    }

    else if(b>c>a||b>a>c)
    {
        maior=b;
    }

    else if(a>b>c||a>c>b)
    {
        maior=a;
    }

    printf("\nMaior = %d", maior);

    //A comparação x>y>z nao e aceita

}

void questao5()
{
    int x=0;
    int y=0;

    for(x=1; x<=5; x=x+1)
    {
        for(y=(x+1)/3; y>0; y=y-1)
        {
            printf("_");
        }
        for(y=1; y<=x/2+1; y=y+1)
        {
            printf("%d",y);
        }

        printf("\n");
    }


}
bool mercosul(char x[])
{
    int y= strlen(x);
    int contador = 0;

    char c= x[0];
    

        if( (c>='a' && c<='z') || (c>='A' && c<='Z') )
        {
            contador = contador + 1;
        }

    char d= x[1];
    

        if( (d>='a' && d<='z') || (d>='A' && d<='Z') )
        {
            contador = contador + 1;
        }

    char e= x[2];
    

        if( (e>='a' && e<='z') || (e>='A' && e<='Z') )
        {
            contador = contador + 1;
        }
    
    char f= x[3];
    

        if (f>='0' && f<='9') 
        {
            contador = contador + 1;
        }

    char g= x[4];
    

        if( (g>='a' && g<='z') || (g>='A' && g<='Z') )
        {
            contador = contador + 1;
        }

    char h= x[5];
    

        if (h>='0' && h<='9') 
        {
            contador = contador + 1;
        }

    char i= x[6];
    

        if (i>='0' && i<='9') 
        {
            contador = contador + 1;
        }


        if(contador==7)
        {
            printf("\nPlaca correta!");
        }
        else
        {
            printf("\nPlaca errada!");
        }


    return (true);
}
void questao6()
{
    char x[80];

    printf("\nEntre com uma placa:");
    scanf("%s", x);


    while(strcmp("0000000",x)!=0)
    {
    mercosul(x);
    printf("\nEntre com uma placa:");
    scanf("%s", x);

    }
}

int power(int N, unsigned int D)
{
    if (D == 0)
        return 1;
  
    if (D % 2 == 0)
        return power(N, D / 2)
               * power(N, D / 2);
  
    return N * power(N, D / 2)
           * power(N, D / 2);
}
  
int order(int N)
{
    int r = 0;
  
    
    while (N) {
        r++;
        N = N / 10;
    }
    return r;
}
  

int isArmstrong(int N)
{
    
    int D = order(N);
  
    int temp = N, sum = 0;
  
    
    while (temp) {
        int Ni = temp % 10;
        sum += power(Ni, D);
        temp = temp / 10;
    }
  
    
    if (sum == N)
        return 1;
    else
        return 0;
}
  
void questao7()
{
    int N = 0;
    
    printf("\nEntre com um valor");
    scanf("%d", &N);

    if (isArmstrong(N) == 1)
        printf("\nTrue\n");
    else
        printf("\nFalse\n");
    
}

int main()
{
    int x = 0;

    printf("\nEntre com o numero da questao:");
    scanf("%d", &x);

    switch(x)
    {
    case 1:
        questao1();
    break;
    case 2:
        questao2();
    break;
    case 3:
        questao3();
    break;
    case 4:
        questao4();
    break;
    case 5:
        questao5();
    break;
    case 6:
        questao6();
    break;
    case 7:
        questao7();
    break;
    }

  printf("\nAperte ENTER para terminar");
  getchar();
  getchar();
}
