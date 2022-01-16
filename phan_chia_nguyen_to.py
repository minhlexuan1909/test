import math


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())

arr = input().split()
arrSet = list(set([int(x) for x in arr]))
arrSet.sort(key=lambda x: arr.index(str(x)))

sumArr = sum(arrSet)
sum = 0
check = True
for i in range(0, len(arrSet)):
    sum += arrSet[i]
    if isPrime(sum) and isPrime(sumArr - sum):
        print(i)
        check = False
        break

if check:
    print("NOT FOUND")
