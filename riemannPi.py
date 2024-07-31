import math
num_of_iter = 1000000
MY_PI = 0
dx = 2.0/num_of_iter
for i in range(num_of_iter):#gets riemann sum of half circle
    MY_PI += dx * math.sqrt((-1 * ((-1 + dx * i) * (-1 + dx * i))) + 1) 
    print(i)    
MY_PI *= 2 #since we take riemann sum of half circle
print("PI Approximately Equals ")
print(MY_PI)
print("Margin of Error is +-")
print(2 * 2 * dx) # I eblieve this is how you calculate Margin of Error 2 = size of circle and 2 is due too pi being multiplied by 2
