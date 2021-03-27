#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

#include "complexos.h"


int main () {
    unsigned int N;
    int i;
    printf("Quantos numeros?\n");
	scanf("%u", &N);
    getchar();
    Complexo num_complexo[N];
    cout << "Insira o número, parte real( espaço ou enter),parte imaginária na forma retangular:\n ";
    for(i=0;i<N;i++)
	{   printf("Número %u: \n", i+1);
		cin >> num_complexo[i].real;
        cin >> num_complexo[i].imag;
		}
    int op; 
    printf("Este programa realiza operações com números complexos");
	do{printf("\nEscolha a operacao a ser realizada:\n[1]Soma\n[2]Subtração\n[3Multiplicação\n[4]Divisão\n[5]Conversão\n[6]Ver números escolhidos\n[7]Sair\n");
	scanf("%d",&op);
	switch(op){
		case 1:{

            break;
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
        { 
        break;}

		break;
		
		default:
 	    {
 		if(op!= 7)
 		printf("Operacao invalida!\n");
 		break;
    }
  }	
}while(op!=7);
     return 0;
}


