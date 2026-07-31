#include<stdio.h>
int main()
{
int a;
float b;
char ch;
char str[101];
printf("enter a number:");
scanf("%d",&a);
printf("enter a floating:");
scanf("%f",&b);
printf("enter a character:");
scanf(" %c",&ch);
printf("enter a string(no spaces):");
scanf("%s",str);
printf("\n you entered: \n");
printf("%d\n %f\n %c\n %s\n",a,b,ch,str);
return 0;
}

