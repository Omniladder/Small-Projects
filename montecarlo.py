n = 5000 # Higher this variable more accurate the approximation is 

count = 0

for x in range(n):
    for y in range(n):
        if ((x / n)**2 + (y / n)**2)**(1/2) <= 1:
            count += 1

print("Approximation of PI", 4* count /  n ** 2)