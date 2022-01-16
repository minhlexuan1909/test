t = int(input())
BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


while t:
    num, base = [int(x) for x in input().split()]
    print(to_base(num, base))
    t -= 1
