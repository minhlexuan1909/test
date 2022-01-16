t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    check = True
    for i in range(0, len(a)):
        if a[i] > b[i]:
            check = False
            break
    print({True: "YES", False: "NO"}[check])
    t -= 1
