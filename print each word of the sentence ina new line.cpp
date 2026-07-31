#include<stdio.h>
int main()
{
	char str[100];
	printf("Enter a sentence:");
	fgets(str,sizeof(str),stdin);
	printf("words in the sentence are:\n");
	for(int i=0;str[i]!='\0';i++)
	{
		if (str[i]=='0')
		printf("\n");
		else
		printf("%c",str[i]);
	}
	return 0;
}

