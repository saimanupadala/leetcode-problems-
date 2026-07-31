#include<math.h>
#include<stdio.h>
int main()
{
	double a,b,c,discriminant,root1,root2,realpart,imagpart;
	printf("enter coefficients a,band c:");
	scanf("%lf %lf %lf",&a,&b,&c);
	if(a==0){
		printf("not a qudratic equation(a cannot be 0)");
		return 0;
	}
	discriminant =b*b-4*a*c;
	if(discriminant>0){
		root1=(-b+sqrt(discriminant))/2*a;
		root2=(-b-sqrt(discriminant))/2*a;
		printf("root1=%2lf and root2=%2lf",root1,root2);
	}
		else if(discriminant=0){
			root1=(root2=-b/2*a);
			printf("root1=root2=%2lf",root1);
		}
		else{
			realpart=-b/(2*a);
			imagpart=sqrt(-discriminant)/(2*a);
			printf("root1=%2lf+%2lfi and root2=%2lf-%2lfi",realpart,imagpart,realpart,imagpart);
		}
			return 0;
		}
		
	

