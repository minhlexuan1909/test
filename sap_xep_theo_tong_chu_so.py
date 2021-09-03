def sumNum(num):
    num = str(num)
    num = [int(letter) for letter in num]
    return sum(num)

t = int(input())
while t:
    n = int(input())
    numList = [int(num) for num in input().split()]
    numList.sort(key = lambda num: (sumNum(num),num))
    numList = [str(num) for num in numList]
    print(' '.join(numList))
    t-=1