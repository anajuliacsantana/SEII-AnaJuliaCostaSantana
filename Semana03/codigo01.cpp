#include <iostream>
#include <string>
#include <conio.h>


using namespace std;
#include "complexos.h"

float soma(complexo[],int num_som,int param);
int main (){
    unsigned int N;
    int i;
    printf("Quantos numeros?\n");
	scanf("%u", &N);
    getchar();
    Complexo num_complex[N];
    Complexo s,sub,mult,div,conv;
    cout << "Insira o número, parte real( espaço ou enter),parte imaginária na forma retangular:\n ";
    for(i=0;i<N;i++)
	{   printf("Número %u: \n", i+1);
		cin >> num_complex[i].real;
        cin >> num_complex[i].imag;
		}
    int op; 
    printf("Este programa realiza operações com números complexos");
	do{printf("\nEscolha a operacao a ser realizada:\n[1]Soma\n[2]Subtração\n[3Multiplicação\n[4]Divisão\n[5]Conversão\n[6]Ver números escolhidos\n[7]Sair\n");
	scanf("%d",&op);
	switch(op){
		case 1:{
    for(i=0;i<N;i++){
        s = soma(num_complex[i], i,N);}
        printComplex(s,1); 
                }
             }
        }
        
		case 2:
		{ 
			break;
			}
		
		case 3:
			{break;}
			
		case 4:
			{break;}
			
		case 5:
			{break;}
		
        case 6:
        { for(i=0;i<N;i++){
            printComplex(num_complex[i],i);
        }	
        break;}

		break;
		
		default:
 	    {
 		if(op!=7)
 		printf("Operacao invalida!\n");
 		break;
    }
  }	
}while(op!=7);
 
    return 0;
}


complexo soma(complexo a[],int num_som,int param){
    complexo aux_soma;
       do {aux_soma.real =  aux_soma.real + a[ num_som].real;
        aux_soma.imag = aux_soma.imag + a[i].imag; 
   }while(i<param)
   return aux_soma;
}

complexo produto(complexo z, complexo w){

    complexo aux_mult;

    aux_mult.real = z.real * w.real - z.imag * w.imag;
    aux_mult.imag = z.real * w.imag + z.imag * w.real;

    return aux_mult;
}


void printComplex(struct complexo, int n)
            if (num_complex.imag > 0)
            {
            printf("Número Complexo %d: %f + %fj \n",n+1, num_complex[i].real, num_complex[i].imag);
            }
            else
            printf("Número Complexo %d: %f %fj \n",n+1, num_complex[i].real, num_complex[i].imag);
        // cout <<"Número Complexo 1:  " <<num_complex[0].real<< "," << num_complex[0].imag<< "j" << endl; 
     }