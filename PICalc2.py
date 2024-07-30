iterationStr = input ("How many Iterations would you like to calculate\n")
iterations = int(iterationStr)

PiSum = 0

neg = 1

for i, j in enumerate([j * 2 + 1 for j in range(iterations)]):
    PiSum += 1 / j * neg
    neg *= -1

PiSum *= 4
print(f"PI Roughly Equals {PiSum}")
