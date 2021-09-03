t = int(input())

while t:
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    a.sort()
    b.sort()
    check = True
    for i in range(0, len(a)):
        if (a[i] > b[i]):
            check = False
            break
    print({True: 'YES', False: 'NO'}[check])
    t-=1