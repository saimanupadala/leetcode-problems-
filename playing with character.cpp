#include<stdio.h>
int main()
{
	char ch;
	char s[1000];
	char sen[10000];
	scanf(" %c",&ch);
	scanf("%s",s);
	scanf(" %[^\n]",sen); 
	printf("%c\n%s\n%s\n",ch,s,sen);
	return 0;
}
