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
    num = int(s[-4::])
    print({True: "YES", False: "NO"}[isPrime(num)])

    t -= 1
