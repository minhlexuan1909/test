def checkNum(num):
    num = str(num);
    if len(num) % 2 != 0 or num != num[::-1]:
        return False
    # Chuyen num tu str -> list
    num = [int(i) for i in num]
    for i in num:
        if i % 2 != 0:
            return False
    return True

t = int(input())
while t:
    n = int(input())
    list = [str(num) for num in range(10, n) if checkNum(num)]
    print(' '.join(list))
    t-=1