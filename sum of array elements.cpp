#include<stdio.h>
int main()
{
	int n,sum=0;
	printf("enter array size \n");
	scanf("%d",&n);
	int arr[n];
	printf("enter array elements \n");
	for(nint i=0;i<=n;i++)
{
	scanf("%d,&arr[i]");
	}	
	for(int i=0;i<n;i++)
	{
		sum+=arr[i];
	}
	printf("%d",sum);
	return 0;
}
