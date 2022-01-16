t = int(input())


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


prime = sangNguyenTo()
while t:
    s = input()
    check = True
    for i in range(0, len(s)):
        if (prime[i] == 1 and prime[int(s[i])] != 1) or (
            prime[i] != 1 and prime[int(s[i])] == 1
        ):
            check = False
            break
    print({True: "YES", False: "NO"}[check])
    t -= 1

# 2
# 14239567
# 2314514535353
