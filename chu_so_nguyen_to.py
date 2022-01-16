import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


t = int(input())

while t:
    s = input()
    check = True
    if not isPrime(len(s)):
        check = False
    else:
        countPrime = 0
        countNotPrime = 0
        for char in s:
            if isPrime(int(char)):
                countPrime += 1
            else:
                countNotPrime += 1
        if countNotPrime >= countPrime:
            check = False
    print({True: "YES", False: "NO"}[check])
    t -= 1
