t = int(input())

while t:
    num = input()
    check = True
    for i in range(0, len(num)):
        if (i % 2 == 0 and int(num[i]) % 2 != 0) or (
            i % 2 != 0 and int(num[i]) % 2 == 0
        ):
            print("NO")

            check = False
            break
    if check:
        print("YES")

    t -= 1
