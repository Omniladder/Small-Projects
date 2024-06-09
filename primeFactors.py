import math

num = input("Please Input Numnber you want the prime Facotrization of\n")

number = int(num)


print("The Prime Factors Are: \n")


for i in range(2, int(math.sqrt(number))):
    if i > int(math.sqrt(number)):
        break
    while(number % i == 0):
        print(i)
        number /= i

if number != 1:
    print(int(number))
