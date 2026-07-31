#include<stdio.h>
int main(){
	int n=1;
	print:
		printf("%d",n);
		n++;
		if(n<=10)
		goto print;
		return 0;	
}
