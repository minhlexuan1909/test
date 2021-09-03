import math

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

n = int(input())
numList = input().split()
numed = []

for num in numList:
    if num not in numed:
        if checkPrime(int(num)):
            print(f'{num} {numList.count(num)}')
        numed.append(num)
        