import math

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

t = int(input())
while t:
    numList = [int(num) for num in input().split()]
    a = numList[0]
    b = numList[1]
    numGCD = math.gcd(a,b)
    numGCD = str(numGCD)
    numGCD = [int(num) for num in numGCD]
    numSum = sum(numGCD)
    print({True: 'YES', False: 'NO'}[checkPrime(numSum)])
    t-=1

