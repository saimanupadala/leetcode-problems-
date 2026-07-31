#nclude<stdio.h>
int main()
{
	int x,y,i;
	printf("enter x,y values");
	scanf("%d",&x,&y);
	for(i=x;i<=y;i++)
	{
	
	if(i>=1&&i<=9)
	{
			if(i==1)printf("one")
		else if(i==2)printf("two")
		else if(i==3)printf("three")
		else if(i==4)printf("four")
		else if(i==5)printf("five")
		else if(i==6)printf("six")
		else if(i==7)printf("seven")
		else if(i==8)printf("eight")
		else if(i==9)printf("nine")
	}
	else
	{
		if(i%2==0)
		printf("even");
		else
		{
		printf("odd");
			}
	}
}
return 0;
}
		

