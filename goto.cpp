#include<stdio.h>
int main(){
	goto print;
	printf("go to example");
	print:
		printf("this is label");
		return 0;
}
