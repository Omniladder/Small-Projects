#include <stdio.h>
#include <math.h>

int main()
{
	int number;
	printf("What do you want to get the prime factors of???\n");
	scanf("%d", &number);

	printf("%d", number);
	
	printf("\n\nThe Prime Numbers Are:\n");
	for(int i = 2; i <= sqrt(number); i++)
	{
		while(number % i == 0)
		{
			printf("%d\n", i);
			number /= i;
		}
	}
	if(number != 1)
	printf("%d\n", number);

	return -1;

}
