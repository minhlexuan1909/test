import math
t = int(input())

while t:
    n = int(input())
    resString = "1"
    for num in range(2, int(math.sqrt(n))+1):
        count = 0
        while (n%num == 0):
            count+=1
            n /= num
        if count:
            resString += f" * {num}^{count}"
    if (n > 1):
        resString += f" * {int(n)}^{1}"
    print(resString)
    t-=1