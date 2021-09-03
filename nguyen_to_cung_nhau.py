import math

n = int(input())
numList = [int(num) for num in input().split()]
numList.sort()

for i in range(0, len(numList)):
    for j in range(i+1, len(numList)):
        if (math.gcd(numList[i], numList[j]) == 1):
            print(numList[i], numList[j])