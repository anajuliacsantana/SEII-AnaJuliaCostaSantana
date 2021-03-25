#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

struct Complexo{
    float real;
    float imag;
};

int main ()
{
    int i;
    cout << "Escolha qual operação"
    Complexo num_complex[i];
    
    cout << "Insira o número, parte real( espaço ou enter), parte imaginária na forma retangular :";
    cin >> num_complex[0].real;
    cin >> num_complex[0].imag;
    printf("Número Complexo 1: %f + %fj \n", num_complex[0].real, num_complex[0].imag);
    printf("Número Complexo 2: %f + %fj\n", num_complex[1].real, num_complex[1].imag);
    // cout <<"Número Complexo 1:  " <<num_complex[0].real<< "," << num_complex[0].imag<< "j" << endl;
    // cout <<"Número Complexo 2: " <<num_complex[1].real <<"," <<num_complex[1].imag << "j" << endl;
    
    return 0;
}
int main(){
	int op ; 
    float vet[50];
    int N = 50;
   *vet=gera_numeros(vet,N, 0.5, 1.5, &random);
    printf("Este programa realiza calculos com 50 numeros gerados aleatoriamente.");
	do{printf("\nEscolha a operacao a ser realizada:\n[1]Somatorio \n[2]Produtorio.\n[3]Mostrar numeros\n[4]Sair\n");
	scanf("%d",&op);
	switch(op){
		case 1:
		
		printf("\nSoma : %f", soma( &vet[0],&vet[0] + N-1 ) );
		break;
	
		case 2:
		
		printf("\nProduto: %g", produto( &vet[0], &vet[0] + N-1) );
		break;
		
		case 3:
		
		{printf("\nNumeros:\n" );
		for(i=0;i<51;i++)
		{printf("%.3f ",vet[i]);
		}}
		break;
		default:
 	    {
 		if(op!=4)
 		printf("Operacao invalida!\n");
 		break;
    }
  }	
}while(op!=4);
return 0 ;
}