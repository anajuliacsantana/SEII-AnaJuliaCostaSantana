#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

#include "complexos.h"

struct Complexo soma(Complexo numeros[],int n_soma);
void printComplex ( Complexo nums_complexs[],int n);
void printResult(Complexo nums_complexs);
struct Complexo subt(Complexo numeros[],int n_soma);
struct Complexo div(Complexo numeros[],int n_soma);
struct Complexo multiplx(Complexo numeros[],int n_soma);
struct Complexo conversao(Complexo numeros[],int n_soma);

int main () {
    unsigned int N;
    int i;
    printf("Quantos numeros?\n");
	scanf("%u", &N);
    getchar();
    Complexo num_complexo[N], somas;
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
			somas = soma(num_complexo,N);
			printf("O resultado da soma é: ");
			printResult(somas);
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
		printComplex(num_complexo,N);
        break;}

		break;
		
		default:
 	    {
 		if(op!= 7)
 		printf("Operacao invalida!\n");
 		break; }
  }	
}while(op!=7);
     return 0;
}

struct Complexo soma(Complexo numeros[],int n_soma){
	struct Complexo aux_soma = {};
	int i;
	float soma_real = 0;
	float soma_imag = 0;
	for(i = 0 ;i<n_soma;i++){
	aux_soma.real += numeros[i].real;
	aux_soma.imag += numeros[i].imag;
	}
	return aux_soma;
}

void printResult(Complexo nums_complexs){ 
    if(nums_complexs.imag > 0){
	printf("%f + %f j\n",nums_complexs.real,nums_complexs.imag);
	}
	else if(nums_complexs.imag == 0) 
	printf("%f \n",nums_complexs.real);
	else 
	printf("%f %f j\n",nums_complexs.real,nums_complexs.imag);
	}

void printComplex(Complexo nums_complexs[],int n){ 
	int i;
	for(i=0;i<n;i++){
    if(nums_complexs[i].imag > 0){
	printf("Número %d : %f +%fj\n",i+1,nums_complexs[i].real,nums_complexs[i].imag);
	}
	else if(nums_complexs[i].imag == 0) 
	printf("Número %d : %f \n",i+1,nums_complexs[i].real);
	else 
	printf("Número %d : %f %fj\n",i+1,nums_complexs[i].real,nums_complexs[i].imag);
	}
}