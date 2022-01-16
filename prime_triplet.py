t = int(input())

prime = []
prime.append(2)


def sangNguyenTo():
    l = [1] * 100001
    l[0] = 0
    l[1] = 0
    for i in range(2, 100001):
        if l[i] == 0:
            continue
        for j in range(i * i, 100001, i):
            l[j] = 0
    return l


l = sangNguyenTo()
# for i in range(3, 100001):
#     check = True
#     for num in prime:
#         if i % num == 0:
#             check = False
#             break
#     if check:
#         prime.append(i)
for i in range(2, 100001):
    if l[i] == 1:
        prime.append(i)

while t:
    n = int(input())
    count = 0
    i = 2
    while i < len(prime) and prime[i] < n:
        if (prime[i] - prime[i - 1] == 2 and prime[i] - prime[i - 2] == 6) or (
            prime[i] - prime[i - 1] == 4 and prime[i] - prime[i - 2] == 6
        ):
            count += 1
        i += 1
    print(count)
    t -= 1
