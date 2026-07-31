#include<stdio.h>
int main()
{
	int a=2,b=3,c=4;
	printf("%d \n ",(a<b&&b>c));
	printf("%d \n",(a<b||b>c));
	printf("%d \n",!(a<b&&b>c));
	return 0;
}
