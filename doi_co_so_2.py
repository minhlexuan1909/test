BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


t = int(input())
while t:
    base = int(input())
    num = int(input(), 2)
    print(to_base(num, base))
    t -= 1
