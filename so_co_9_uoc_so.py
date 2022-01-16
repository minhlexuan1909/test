import math


def sangNguyenTo():
    l = [1] * 32000
    l[0] = 0
    l[1] = 0
    for i in range(2, 32000):
        if l[i] == 0:
            continue
        for j in range(i * i, 32000, i):
            l[j] = 0
    return l


prime = []
prime = sangNguyenTo()
n = int(input())
count = 0
for i in range(2, int(math.sqrt(n)) + 1):
    if i ** 8 <= n and prime[i] == 1:
        count += 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0 and j != int(i / j) and prime[j] == 1 and prime[int(i / j)] == 1:
            count += 1
            break

print(count)
