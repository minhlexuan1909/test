t = int(input())

while t:
    num = input()
    count = 0
    check = True
    while int(num) % 7 != 0:
        num = str(int(num) + int(str(num)[::-1]))
        count += 1
        if count == 1001:
            check = False
            break
    if check:
        print(num)
    else:
        print(-1)
    t -= 1
