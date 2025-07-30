'''
    Collects a Listof integers that sum to given int
'''
sumToInt = int(input("List the Integer in question "))
array = [i for i in range(sumToInt)][1:]
subarray = []

for element in array:
    subarray.append(element)

    if sum(subarray) == sumToInt:
        print(subarray)

    while sum(subarray) > sumToInt:
        subarray = subarray[1:]

