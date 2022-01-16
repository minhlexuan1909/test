def sangNguyenTo():
    l = [1] * 10000
    l[0] = 0
    l[1] = 0
    for i in range(2, 10000):
        if l[i] == 0:
            continue
        for j in range(i * i, 10000, i):
            l[j] = 0
    return l


l = sangNguyenTo()
prime = [i for i in range(0, len(l)) if (l[i] == 1)]

n = int(input())
arr = [int(x) for x in input().split()]

res = 0
for num in arr:
    for i in range(0, len(prime)):
        if num >= prime[i] and num < prime[i + 1]:
            res = max([min([num - prime[i], prime[i + 1] - num]), res])
            break
print(res)
