/*
 *I WANT TO CREATE A SET OF FUNCTIONS WHERE YOU CAN DO 2 REINTERPRET CASTS into a unsignedint and then back into your desired data type and it will do the bitwise operations for you
 * */

#include <stdio.h>
#include <stdint.h>

uint64_t bitClear()
{
	uint64_t bitNumber = 0;
	return bitNumber;
}

uint64_t bitMax()
{
	uint64_t bitNumber = 0;
	return --bitNumber;
}

void bitOutput(uint64_t bitNumber)
{
	uint64_t one = 1;
	for (long unsigned int i = sizeof(uint64_t) - 1; i > 0; i--)
		printf("%llu", ((one << i) & bitNumber) > 0);
	printf("%llu\n", one & bitNumber);
}

void valueOutput(uint64_t bitNumber)
{
	uint64_t one = 1;
	for (long unsigned int i = sizeof(uint64_t) - 1; i > 0; i--)
	printf("%llu", (one << i) & bitNumber);
	
	printf("%llu\n", one & bitNumber);

}

uint64_t bitSet(uint64_t bitNumber, int oneZero, int index)
{
	if(oneZero == 1)
		return bitNumber | (1u << index);
	else
		return bitNumber & (bitMax() - (1u << index));
}

int bitCheck(uint64_t bitNumber, int index)
{return (((1 << index) & bitNumber) > 0);}


