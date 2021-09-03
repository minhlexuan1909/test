def numMul(num):
    num = str(num)
    numChar = [int(letter) for letter in num]
    x = 1
    for i in numChar:
        x *= i
    return x

t = int(input())
while t:
    n = int(input())
    numList = [int(num) for num in input().split()]
    numList.sort(key = lambda num: (numMul(num), num))
    numList = [str(num) for num in numList]
    print(' '.join(numList))
    t-=1
