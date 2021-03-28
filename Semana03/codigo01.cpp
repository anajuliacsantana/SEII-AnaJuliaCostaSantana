#include <iostream>
#include <string>
#include <conio.h>
#include <math.h>

using namespace std;
#define pi 3.14159265
#include "complexos.h"

void soma(Complexo numeros[],int n_soma);
void printComplex ( Complexo nums_complexs[],int n);
void printResult(Complexo nums_complexs);
void subt(Complexo numeros[],int n);
void div(Complexo numeros[],int n_soma);
void multiplx(Complexo numeros[],int n_soma);
void conversao(Complexo numeros[],int n_soma);
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
	do{printf("\nEscolha a operacao a ser realizada:\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Conversão\n[6]Ver números escolhidos\n[7]Sair\n");
	scanf("%d",&op);
	switch(op){
		case 1:{
			printf("O resultado da soma é: ");
			soma(num_complexo,N);
            break;
              }
           
		case 2:
		{ printf("O resultado da substração é: ");
			subt(num_complexo,N);
			break;
			}
		
		case 3:
			{
			multiplx(num_complexo,N);
			break;
			}
			
		case 4:
			{
			 div(num_complexo,N);
				
				break;}
			
		case 5:
			{
			    conversao(num_complexo,N);
				
				break;}
		
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

void soma(Complexo numeros[],int n_soma){
	struct Complexo aux_soma = {};
	int i;
	for(i = 0 ;i<n_soma;i++){
	aux_soma.real += numeros[i].real;
	aux_soma.imag += numeros[i].imag;
	}
	printResult(aux_soma);
}

void subt(Complexo numeros[],int n){
	struct Complexo aux = {0,0};
	int i;
	aux.real = numeros[0].real;
	aux.imag = numeros[0].imag;
	for(i = 1;i<n;i++){
	aux.real -= numeros[i].real;
	aux.imag -= numeros[i].imag;
	}
	printResult(aux);
}


void div(Complexo numeros[],int n){
	struct Complexo aux = {1,1};
	int i ;
	int op;
	cout<<"O número está na forma polar? Digite 1=sim, 2=não";
	scanf("%d",&op);
	if(op == 2){
		for(i =0;i<n; i++){
			numeros[i].real = sqrtf(powf(numeros[i].imag,2) + powf(numeros[i].real, 2));
			numeros[i].imag = atanf(numeros[i].imag/numeros[i].real);
			}
		}
	for (i=0;i<n;i++){
		aux.real = aux.real/numeros[i].real;
		aux.imag = aux.imag/numeros[i].imag;
		numeros[i].real = cos(numeros[i].imag*pi/180)*numeros[i].real;
		numeros[i].imag = sin(numeros[i].imag*pi/180)*numeros[i].real;
	}
		aux.real = cos(aux.imag*pi/180)*aux.real;
		aux.imag = sin(aux.imag*pi/180)*aux.real;
		printResult(aux);
}

void multiplx(Complexo numeros[],int n){
	struct Complexo aux = {1,1};
	int i ;
	int op;
	cout<<"O número está na forma polar? Digite 1=sim, 2=não \n";
	scanf("%d",&op);
	if(op == 2){
		for(i =0;i<n; i++){
		numeros[i].real = sqrtf(powf(numeros[i].imag,2) + powf(numeros[i].real, 2));
		numeros[i].imag = atanf((numeros[i].imag/numeros[i].real)*pi/180);
	}
	}
	for (i=0;i<n;i++){
		aux.real = aux.real*numeros[i].real;
		aux.imag = aux.imag*numeros[i].imag;
		numeros[i].real = cos(numeros[i].imag*pi/180)*numeros[i].real;
		numeros[i].imag = sin(numeros[i].imag*pi/180)*numeros[i].real;		
	}
		aux.real = cos(aux.imag*pi/180)*aux.real;
		aux.imag = sin(aux.imag*pi/180)*aux.real;
		printResult(aux);
}


void conversao(Complexo numeros[],int n){
	struct Complexo auxiliar[n] = {};
	int i,op;
	do{
	cout<<"Selecione o tipo de conversão:\n[1]Retangular para polar;\n[2]Polar para retangular.\n[3]Sair";
	scanf("%d",&op);
	switch(op){
		case 1: {	
		for(i =0;i<n; i++){
		auxiliar[i].real = sqrtf(powf(numeros[i].imag,2) + powf(numeros[i].real, 2));
		auxiliar[i].imag = atanf((numeros[i].imag/numeros[i].real)*pi/180);
			}
		for(i=0;i<n;i++){
    	if(auxiliar[i].imag > 0){
		printf("Número %d : %f /%f\n",i+1,auxiliar[i].real,auxiliar[i].imag);
	}
		else if(auxiliar[i].imag == 0) 
		printf("Número %d : %f \n",i+1,auxiliar[i].real);
		else 
		printf("Número %d : %f /%f\n",i+1,auxiliar[i].real,auxiliar[i].imag);
	}
			break;}
		case 2 :
		{	for(i =0;i<n; i++){
			auxiliar[i].real = cos(numeros[i].imag*pi/180)*numeros[i].real;
			auxiliar[i].imag = sin(numeros[i].imag*pi/180)*numeros[i].real;}
			printComplex( auxiliar,n);
			break;}

		break;
		default:
 	    {
 		if(op!= 3)
 		printf("Operacao invalida!\n");
 		break; }	
	}
		}while(op!=3);
}


void printResult(Complexo nums_complexs){ 
    if(nums_complexs.imag > 0){
	printf("%f + %fj\n",nums_complexs.real,nums_complexs.imag);
	}
	else if(nums_complexs.imag == 0) 
	printf("%f \n",nums_complexs.real);
	else 
	printf("%f %fj\n",nums_complexs.real,nums_complexs.imag);
	}

void printComplex(Complexo nums_complexs[],int n){ 
	int i;
	for(i=0;i<n;i++){
    if(nums_complexs[i].imag > 0){
	printf("Número %d : %f + %fj\n",i+1,nums_complexs[i].real,nums_complexs[i].imag);
	}
	else if(nums_complexs[i].imag == 0) 
	printf("Número %d : %f \n",i+1,nums_complexs[i].real);
	else 
	printf("Número %d : %f %fj\n",i+1,nums_complexs[i].real,nums_complexs[i].imag);
	}
}

