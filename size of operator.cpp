#include<stdio.h>
int main()
{
	int  x=50;
	printf("size of the variable x is %zu",sizeof(x));
	printf("\n size of the integer data type is %zu",sizeof(int));
	printf("\n size of the character data type is %zu",sizeof(char));
	printf("\n size of the floating data type is %zu\n",sizeof("flaot"));
	printf("the address of x is %p\n ",(void*)&x);
	return 0;
}
