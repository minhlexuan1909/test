import math


t = int(input())
while t:
    n = int(input())
    n *= 2
    count = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and (n / i - (i - 1)) % 2 == 0:
            count += 1
    print(count)
    t -= 1
