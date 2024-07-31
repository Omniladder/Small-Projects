iterationStr = input ("How many Iterations would you like to calculate\n")
iterations = int(iterationStr)

PiSum = 0

neg = 1

for i, j in enumerate([j * 2 + 1 for j in range(iterations)]):
    error = 1 / j * neg # Since it converge the sum of all terms after should be smaller than new term if i'm correct might be wrong
    PiSum += error
    neg *= -1

PiSum *= 4
error = abs(4 * error)

print()
print(f"PI Roughly Equals {PiSum}")
print(f"Margin of Error is +- {error}")
